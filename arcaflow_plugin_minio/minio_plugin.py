#!/usr/bin/env python3

import string
import random
import os
import sys
import typing
import subprocess
from time import sleep
from minio import Minio

from arcaflow_plugin_sdk import plugin
from minio_schema import (
    InputParams,
    SuccessOutput,
    ErrorOutput,
)


def get_random_string(length):
    random_str = "".join(random.choices(string.ascii_lowercase, k=length))
    return random_str


@plugin.step(
    id="minio",
    name="MinIO",
    description="Runs the MinIO server and sets up a bucket",
    outputs={"success": SuccessOutput, "error": ErrorOutput},
)
def minio(
    params: InputParams,
) -> typing.Tuple[str, typing.Union[SuccessOutput, ErrorOutput]]:

    # Set the access and secret keys
    minio_user = get_random_string(8)
    minio_password = get_random_string(8)

    os.environ["MINIO_ROOT_USER"] = minio_user
    os.environ["MINIO_ROOT_PASSWORD"] = minio_password

    # Start the MinIO server
    minio_cmd = [
        "/usr/local/bin/minio",
        "server",
        "/arca-bucket",
    ]
    try:
        subprocess.Popen(
            minio_cmd,
            text=True,
        )
        print("==> MinIO server started")
    except subprocess.CalledProcessError as error:
        return "error", ErrorOutput(
            "{} failed with return code {}:\n{}".format(
                error.cmd[0], error.returncode, error.output
            )
        )

    # Create the bucket
    client = Minio(
        "127.0.0.1:9000",
        access_key=minio_user,
        secret_key=minio_password,
        secure=False,
    )

    client.make_bucket("arca-bucket")

    print("==> arca-bucket created")

    # Note -- Timeout is a temporary workaround until the parallelization
    # functionality of the workflow engine is complete.
    print("==> Waiting for timeout...")

    sleep(params.run_duration)

    return "success", SuccessOutput(minio_user, minio_password)


if __name__ == "__main__":
    sys.exit(
        plugin.run(
            plugin.build_schema(
                minio,
            )
        )
    )
