# whatsapp.4WebhooksApi

All URIs are relative to *https://api.chat-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**set_webhook**](4WebhooksApi.md#set_webhook) | **POST** /webhook | Sets the URL for receiving webhook


# **set_webhook**
> SetWebhookStatus set_webhook(webhook_url)

Sets the URL for receiving webhook

Sets the URL for receiving webhook notifications of new messages and message delivery events (ack).  **API responses in \"Callbacks\" tab**

### Example

* Api Key Authentication (instanceId):
```python
from __future__ import print_function
import time
import whatsapp
from whatsapp.rest import ApiException
from pprint import pprint
configuration = whatsapp.Configuration()
# Configure API key authorization: instanceId
configuration.api_key['instanceId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['instanceId'] = 'Bearer'
configuration = whatsapp.Configuration()
# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Defining host is optional and default to https://api.chat-api.com
configuration.host = "https://api.chat-api.com"
# Create an instance of the API class
api_instance = whatsapp.4WebhooksApi(whatsapp.ApiClient(configuration))
webhook_url = whatsapp.WebhookUrl() # WebhookUrl | 

try:
    # Sets the URL for receiving webhook
    api_response = api_instance.set_webhook(webhook_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling 4WebhooksApi->set_webhook: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import whatsapp
from whatsapp.rest import ApiException
from pprint import pprint
configuration = whatsapp.Configuration()
# Configure API key authorization: instanceId
configuration.api_key['instanceId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['instanceId'] = 'Bearer'
configuration = whatsapp.Configuration()
# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Defining host is optional and default to https://api.chat-api.com
configuration.host = "https://api.chat-api.com"
# Create an instance of the API class
api_instance = whatsapp.4WebhooksApi(whatsapp.ApiClient(configuration))
webhook_url = whatsapp.WebhookUrl() # WebhookUrl | 

try:
    # Sets the URL for receiving webhook
    api_response = api_instance.set_webhook(webhook_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling 4WebhooksApi->set_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_url** | [**WebhookUrl**](WebhookUrl.md)|  |

### Return type

[**SetWebhookStatus**](SetWebhookStatus.md)

### Authorization

[instanceId](../README.md#instanceId), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server response example |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

