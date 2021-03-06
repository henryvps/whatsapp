# coding: utf-8

"""
    Chat API SDK

    The SDK allows you to receive and send messages through your WhatsApp account. [Sign up now](https://app.chat-api.com/)  The Chat API is based on the WhatsApp WEB protocol and excludes the ban both when using libraries from mgp25 and the like. Despite this, your account can be banned by anti-spam system WhatsApp after several clicking the \"block\" button.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: sale@chat-api.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import whatsapp
from whatsapp.api.testing_api import TestingApi  # noqa: E501
from whatsapp.rest import ApiException


class TestTestingApi(unittest.TestCase):
    """TestingApi unit test stubs"""

    def setUp(self):
        self.api = whatsapp.api.testing_api.TestingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_instance_statuses(self):
        """Test case for instance_statuses

        Returns instance status changes history.  # noqa: E501
        """
        pass

    def test_webhook_statuses(self):
        """Test case for webhook_statuses

        Returns webhook status for message.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
