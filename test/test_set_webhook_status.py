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
from whatsapp.models.set_webhook_status import SetWebhookStatus  # noqa: E501
from whatsapp.rest import ApiException


class TestSetWebhookStatus(unittest.TestCase):
    """SetWebhookStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSetWebhookStatus(self):
        """Test SetWebhookStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = whatsapp.models.set_webhook_status.SetWebhookStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
