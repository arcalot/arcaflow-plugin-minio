#!/usr/bin/env python3

import typing
from dataclasses import dataclass
from arcaflow_plugin_sdk import validation


@dataclass
class InputParams:
    run_duration: int


@dataclass
class SuccessOutput:
    access_key: str
    secret_key: str


@dataclass
class ErrorOutput:
    error: str
