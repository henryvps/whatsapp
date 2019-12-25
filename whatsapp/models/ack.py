# coding: utf-8

"""
    Chat API SDK

    The SDK allows you to receive and send messages through your WhatsApp account. [Sign up now](https://app.chat-api.com/)  The Chat API is based on the WhatsApp WEB protocol and excludes the ban both when using libraries from mgp25 and the like. Despite this, your account can be banned by anti-spam system WhatsApp after several clicking the \"block\" button.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: sale@chat-api.com
    Generated by: https://openapi-generator.tech
"""


import pprint  # noqa: F401
import re  # noqa: F401

import six  # noqa: F401

from whatsapp.exceptions import (  # noqa: F401
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
)
from whatsapp.model_utils import (  # noqa: F401
    ModelNormal,
    ModelSimple,
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    get_simple_class,
    int,
    model_to_dict,
    none_type,
    str,
    type_error_message,
    validate_and_convert_types
)


class Ack(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      openapi_types (dict): The key is attribute name
          and the value is attribute type.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('status',): {
            'DELIVERED': "delivered",
            'VIEWED': "viewed",
        },
    }

    attribute_map = {
        'id': 'id',  # noqa: E501
        'queue_number': 'queueNumber',  # noqa: E501
        'chat_id': 'chatId',  # noqa: E501
        'status': 'status'  # noqa: E501
    }

    openapi_types = {
        'id': (str,),  # noqa: E501
        'queue_number': (int,),  # noqa: E501
        'chat_id': (str,),  # noqa: E501
        'status': (str,),  # noqa: E501
    }

    validations = {
    }

    additional_properties_type = None

    discriminator = None

    def __init__(self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs):  # noqa: E501
        """Ack - a model defined in OpenAPI


        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _from_server (bool): True if the data is from the server
                                False if the data is from the client (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            id (str): unique id. [optional]  # noqa: E501
            queue_number (int): message id in queue. [optional]  # noqa: E501
            chat_id (str): chat ID. [optional]  # noqa: E501
            status (str): type of the message status. [optional]  # noqa: E501
        """
        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        for var_name, var_value in six.iteritems(kwargs):
            self.__set_item(var_name, var_value)

    def __set_item(self, name, value):
        path_to_item = []
        if self._path_to_item:
            path_to_item.extend(self._path_to_item)
        path_to_item.append(name)

        if name in self.openapi_types:
            required_types_mixed = self.openapi_types[name]
        elif self.additional_properties_type is None:
            raise ApiKeyError(
                "{0} has no key '{1}'".format(type(self).__name__, name),
                path_to_item
            )
        elif self.additional_properties_type is not None:
            required_types_mixed = self.additional_properties_type

        if get_simple_class(name) != str:
            error_msg = type_error_message(
                var_name=name,
                var_value=name,
                valid_classes=(str,),
                key_type=True
            )
            raise ApiTypeError(
                error_msg,
                path_to_item=path_to_item,
                valid_classes=(str,),
                key_type=True
            )

        if self._check_type:
            value = validate_and_convert_types(
                value, required_types_mixed, path_to_item, self._from_server,
                self._check_type, configuration=self._configuration)
        if (name,) in self.allowed_values:
            check_allowed_values(
                self.allowed_values,
                (name,),
                value
            )
        if (name,) in self.validations:
            check_validations(
                self.validations,
                (name,),
                value
            )
        self._data_store[name] = value

    def __get_item(self, name):
        if name in self._data_store:
            return self._data_store[name]

        path_to_item = []
        if self._path_to_item:
            path_to_item.extend(self._path_to_item)
        path_to_item.append(name)
        raise ApiKeyError(
            "{0} has no key '{1}'".format(type(self).__name__, name),
            [name]
        )

    def __setitem__(self, name, value):
        """this allows us to set values with instance[field_name] = val"""
        self.__set_item(name, value)

    def __getitem__(self, name):
        """this allows us to get a value with val = instance[field_name]"""
        return self.__get_item(name)

    @property
    def id(self):
        """Gets the id of this Ack.  # noqa: E501
        unique id  # noqa: E501

        Returns:
            (str): The id of this Ack.  # noqa: E501
        """
        return self.__get_item('id')

    @id.setter
    def id(self, value):
        """Sets the id of this Ack.  # noqa: E501
        unique id  # noqa: E501
        """
        return self.__set_item('id', value)

    @property
    def queue_number(self):
        """Gets the queue_number of this Ack.  # noqa: E501
        message id in queue  # noqa: E501

        Returns:
            (int): The queue_number of this Ack.  # noqa: E501
        """
        return self.__get_item('queue_number')

    @queue_number.setter
    def queue_number(self, value):
        """Sets the queue_number of this Ack.  # noqa: E501
        message id in queue  # noqa: E501
        """
        return self.__set_item('queue_number', value)

    @property
    def chat_id(self):
        """Gets the chat_id of this Ack.  # noqa: E501
        chat ID  # noqa: E501

        Returns:
            (str): The chat_id of this Ack.  # noqa: E501
        """
        return self.__get_item('chat_id')

    @chat_id.setter
    def chat_id(self, value):
        """Sets the chat_id of this Ack.  # noqa: E501
        chat ID  # noqa: E501
        """
        return self.__set_item('chat_id', value)

    @property
    def status(self):
        """Gets the status of this Ack.  # noqa: E501
        type of the message status  # noqa: E501

        Returns:
            (str): The status of this Ack.  # noqa: E501
        """
        return self.__get_item('status')

    @status.setter
    def status(self, value):
        """Sets the status of this Ack.  # noqa: E501
        type of the message status  # noqa: E501
        """
        return self.__set_item('status', value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        return model_to_dict(self, serialize=False)

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Ack):
            return False

        if not set(self._data_store.keys()) == set(other._data_store.keys()):
            return False
        for _var_name, this_val in six.iteritems(self._data_store):
            that_val = other._data_store[_var_name]
            types = set()
            types.add(this_val.__class__)
            types.add(that_val.__class__)
            vals_equal = this_val == that_val
            if (not six.PY3 and
                    len(types) == 2 and unicode in types):  # noqa: F821
                vals_equal = (
                    this_val.encode('utf-8') == that_val.encode('utf-8')
                )
            if not vals_equal:
                return False
        return True

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
