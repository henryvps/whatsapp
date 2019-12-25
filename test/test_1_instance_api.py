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
from whatsapp.api.1_instance_api import 1InstanceApi  # noqa: E501
from whatsapp.rest import ApiException


class Test1InstanceApi(unittest.TestCase):
    """1InstanceApi unit test stubs"""

    def setUp(self):
        self.api = whatsapp.api.1_instance_api.1InstanceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_expiry(self):
        """Test case for expiry

        Updates the QR code after its expired  # noqa: E501
        """
        pass

    def test_get_qr_code(self):
        """Test case for get_qr_code

        Direct link to QR-code in the form of an image, not base64.  # noqa: E501
        """
        pass

    def test_get_settings(self):
        """Test case for get_settings

        Get settings  # noqa: E501
        """
        pass

    def test_get_status(self):
        """Test case for get_status

        Get the account status and QR code for authorization.  # noqa: E501
        """
        pass

    def test_logout(self):
        """Test case for logout

        Logout from WhatsApp Web to get new QR code.  # noqa: E501
        """
        pass

    def test_reboot(self):
        """Test case for reboot

        Reboot your whatsapp instance.  # noqa: E501
        """
        pass

    def test_retry(self):
        """Test case for retry

        Repeat the manual synchronization attempt with the device  # noqa: E501
        """
        pass

    def test_set_settings(self):
        """Test case for set_settings

        Set settings  # noqa: E501
        """
        pass

    def test_takeover(self):
        """Test case for takeover

        Returns the active session if the device has connected another instance of Web WhatsApp  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
