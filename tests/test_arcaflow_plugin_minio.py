#!/usr/bin/env python3

import unittest
import minio_plugin
from arcaflow_plugin_sdk import plugin


class minioTest(unittest.TestCase):
    @staticmethod
    def test_serialization():
        plugin.test_object_serialization(
            minio_plugin.InputParams(
                run_duration=3,
                minio_user="foo",
                minio_password="bartholomew",
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
        input = minio_plugin.InputParams(
            run_duration=3,
            minio_user="foo",
            minio_password="bartholomew",
        )

        output_id, output_data = minio_plugin.minio(input)

        self.assertEqual("success", output_id)
        self.assertIsInstance(output_data.access_key, str)
        self.assertIsInstance(output_data.secret_key, str)


if __name__ == "__main__":
    unittest.main()
