#!/usr/bin/env python3
import unittest
import arcaflow_plugin_minio
from arcaflow_plugin_sdk import plugin


class HelloWorldTest(unittest.TestCase):
    @staticmethod
    def test_serialization():
        plugin.test_object_serialization(
            arcaflow_plugin_minio.InputParams("John Doe")
        )

        plugin.test_object_serialization(
            arcaflow_plugin_minio.SuccessOutput("Hello, world!")
        )

        plugin.test_object_serialization(
            arcaflow_plugin_minio.ErrorOutput(error="This is an error")
        )

    def test_functional(self):
        input = arcaflow_plugin_minio.InputParams(name="Example Joe")

        output_id, output_data = arcaflow_plugin_minio.hello_world(input)

        # The example plugin always returns an error:
        self.assertEqual("success", output_id)
        self.assertEqual(
            output_data,
            arcaflow_plugin_minio.SuccessOutput("Hello, Example Joe!")
        )


if __name__ == "__main__":
    unittest.main()
