#!/usr/bin/env python3

import typing
from dataclasses import dataclass
from arcaflow_plugin_sdk import schema


@dataclass
class InputParams:
    run_duration: typing.Annotated[
        int,
        schema.name("run duration"),
        schema.description(
            "Time in seconds that the MinIO plugin runs before being forceably stopped"
        ),
    ]
    minio_user: typing.Annotated[
        typing.Optional[str],
        schema.name("MinIO username"),
        schema.description("The MinIO server username"),
    ] = None
    minio_password: typing.Annotated[
        typing.Optional[str],
        schema.name("MinIO password"),
        schema.description("The MinIO server password"),
    ] = None
    bucket_name: typing.Annotated[
        typing.Optional[str],
        schema.name("bucket name"),
        schema.description("Name for object bucket"),
    ] = "arca-bucket"


@dataclass
class SuccessOutput:
    access_key: typing.Annotated[
        str,
        schema.name("access key"),
        schema.description("The MinIO server access key (user)"),
    ]
    secret_key: typing.Annotated[
        str,
        schema.name("secret key"),
        schema.description("The MinIO server access secret (password)"),
    ]


@dataclass
class ErrorOutput:
    error: str
