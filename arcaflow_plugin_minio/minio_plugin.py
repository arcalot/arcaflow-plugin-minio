#!/usr/bin/env python3

import sys
import typing
import subprocess
from arcaflow_plugin_sdk import plugin
from minio_schema import (
    InputParams,
    SuccessOutput,
    ErrorOutput,
)


@plugin.step(
    id="minio",
    name="MinIO",
    description="Runs the MinIO server and sets up a bucket",
    outputs={"success": SuccessOutput, "error": ErrorOutput},
)
def minio(
    params: InputParams,
) -> typing.Tuple[str, typing.Union[SuccessOutput, ErrorOutput]]:
    
    # Start the MinIO server
    minio_cmd = [
        "/usr/local/bin/minio",
        "server",
        "start",
    ]
    try:
        subprocess.Popen(
            minio_cmd,
            # stderr=subprocess.STDOUT,
            text=True,

        )
        print("==> MinIO server started")
    except subprocess.CalledProcessError as error:
        return "error", ErrorOutput(
            "{} failed with return code {}:\n{}".format(
                error.cmd[0], error.returncode, error.output
            )
        )

    return "success", SuccessOutput("TODO message")


if __name__ == "__main__":
    sys.exit(
        plugin.run(
            plugin.build_schema(
                minio,
            )
        )
    )
