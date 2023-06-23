#!/usr/bin/env python3

import sys
import typing
from dataclasses import dataclass
from arcaflow_plugin_sdk import plugin, validation


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


@plugin.step(
    id="hello-world",
    name="Hello world!",
    description="Says hello :)",
    outputs={"success": SuccessOutput, "error": ErrorOutput},
)
def hello_world(
    params: InputParams,
) -> typing.Tuple[str, typing.Union[SuccessOutput, ErrorOutput]]:
    """The function is the implementation for the step. It needs the decorator
    above to make it into a step. The type hints for the params are required.

    :param params:

    :return: the string identifying which output it is, as well the output
        structure
    """

    return "success", SuccessOutput("Hello, {}!".format(params.name))


if __name__ == "__main__":
    sys.exit(
        plugin.run(
            plugin.build_schema(
                # List your step functions here:
                hello_world,
            )
        )
    )
