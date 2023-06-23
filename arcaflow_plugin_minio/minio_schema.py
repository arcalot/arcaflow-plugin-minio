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
            "Time in seconds that the PCP plugin runs before being forceably stopped"
        ),
    ]


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
