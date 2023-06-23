#!/usr/bin/env python3

import typing
from dataclasses import dataclass
from arcaflow_plugin_sdk import validation


@dataclass
class InputParams:
    """
    This is the data structure for the input parameters of the step defined
    below.
    """

    name: typing.Annotated[str, validation.min(1)]


@dataclass
class SuccessOutput:
    """
    This is the output data structure for the success case.
    """

    message: str


@dataclass
class ErrorOutput:
    """
    This is the output data structure in the error  case.
    """

    error: str
