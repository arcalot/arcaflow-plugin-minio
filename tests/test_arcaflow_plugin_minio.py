#!/usr/bin/env python3

import unittest
import minio_plugin
from minio import Minio
import io
from time import sleep
from multiprocessing.pool import ThreadPool
from arcaflow_plugin_sdk import plugin


def run_minio_server():
    input = minio_plugin.InputParams(
        run_duration=5,
        minio_user="foo",
        minio_password="bartholomew",
        bucket_name="mybucket",
    )
    return minio_plugin.minio(input)


class minioTest(unittest.TestCase):
    @staticmethod
    def test_serialization():
        plugin.test_object_serialization(
            minio_plugin.InputParams(
                run_duration=3,
                minio_user="foo",
                minio_password="bartholomew",
                bucket_name="mybucket",
            )
        )

        plugin.test_object_serialization(
            minio_plugin.SuccessOutput(
                access_key="abcdefgh",
                secret_key="ijklmnop",
            )
        )

        plugin.test_object_serialization(
            minio_plugin.ErrorOutput(error="This is an error")
        )

    def test_functional(self):
        pool = ThreadPool(processes=1)

        minio_server = pool.apply_async(run_minio_server)

        client = Minio(
            "127.0.0.1:9000",
            access_key="foo",
            secret_key="bartholomew",
            secure=False,
        )

        while not client.bucket_exists("mybucket"):
            print("Waiting for bucket ...")
            sleep(1)

        obj_result = client.put_object(
            "mybucket",
            "myobject",
            io.BytesIO(b"hello"),
            5,
        )
        print(
            f"Created {obj_result.object_name} object; etag: {obj_result.etag}, "
            f"version-id: {obj_result.version_id}"
        )

        output_id, output_data = minio_server.get()

        self.assertEqual("success", output_id)
        self.assertEqual("foo", output_data.access_key)
        self.assertEqual("bartholomew", output_data.secret_key)


if __name__ == "__main__":
    unittest.main()
