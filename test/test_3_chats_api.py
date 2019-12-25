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
from whatsapp.api.chats_api import ChatsApi  # noqa: E501
from whatsapp.rest import ApiException


class TestChatsApi(unittest.TestCase):
    """ChatsApi unit test stubs"""

    def setUp(self):
        self.api = whatsapp.api.chats_api.ChatsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_group_participant(self):
        """Test case for add_group_participant

        Adding participant to a group  # noqa: E501
        """
        pass

    def test_demote_group_participant(self):
        """Test case for demote_group_participant

        Demote group participant  # noqa: E501
        """
        pass

    def test_get_chats(self):
        """Test case for get_chats

        Get the chat list.  # noqa: E501
        """
        pass

    def test_group(self):
        """Test case for group

        Creates a group and sends the message to the created group.  # noqa: E501
        """
        pass

    def test_promote_group_participant(self):
        """Test case for promote_group_participant

        Make participant in the group an administrator  # noqa: E501
        """
        pass

    def test_read_chat(self):
        """Test case for read_chat

        Open chat for reading messages  # noqa: E501
        """
        pass

    def test_remove_group_participant(self):
        """Test case for remove_group_participant

        Remove participant from a group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
