#!/usr/bin/env python3
import unittest
import arcaflow_plugin_template_python
from arcaflow_plugin_sdk import plugin


class HelloWorldTest(unittest.TestCase):
    @staticmethod
    def test_serialization():
        plugin.test_object_serialization(
            arcaflow_plugin_template_python.InputParams("John Doe")
        )

        plugin.test_object_serialization(
            arcaflow_plugin_template_python.SuccessOutput("Hello, world!")
        )

        plugin.test_object_serialization(
            arcaflow_plugin_template_python.ErrorOutput(error="This is an error")
        )

    def test_functional(self):
        input = arcaflow_plugin_template_python.InputParams(name="Example Joe")

        output_id, output_data = arcaflow_plugin_template_python.hello_world(input)

        # The example plugin always returns an error:
        self.assertEqual("success", output_id)
        self.assertEqual(
            output_data,
            arcaflow_plugin_template_python.SuccessOutput("Hello, Example Joe!")
        )


if __name__ == "__main__":
    unittest.main()
