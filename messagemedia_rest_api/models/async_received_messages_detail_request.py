# coding: utf-8

"""
    MessageMedia REST API

    Australia's Leading Messaging Solutions for Business and Enterprise.

    OpenAPI spec version: 1.0.0
    Contact: support@messagemedia.com

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class AsyncReceivedMessagesDetailRequest(object):
    """
    Do not edit the class manually.
    """
    def __init__(self, start_date=None, end_date=None, sort_by=None, sort_direction=None, timezone=None, accounts=None, destination_address_country=None, destination_address=None, message_format=None, metadata_key=None, metadata_value=None, source_address_country=None, source_address=None, action=None, delivery_options=None):
        """
        AsyncReceivedMessagesDetailRequest - a model

        :param dict types: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.types = {
            'start_date': 'StartDateBody',
            'end_date': 'EndDateBody',
            'sort_by': 'str',
            'sort_direction': 'SortDirectionBody',
            'timezone': 'TimezoneBody',
            'accounts': 'AccountsBody',
            'destination_address_country': 'DestinationAddressCountryBody',
            'destination_address': 'DestinationAddressBody',
            'message_format': 'MessageFormatBody',
            'metadata_key': 'MetadataKeyBody',
            'metadata_value': 'MetadataValueBody',
            'source_address_country': 'SourceAddressCountryBody',
            'source_address': 'SourceAddressBody',
            'action': 'ActionBody',
            'delivery_options': 'DeliveryOptionsBody'
        }

        self.attribute_map = {
            'start_date': 'start_date',
            'end_date': 'end_date',
            'sort_by': 'sort_by',
            'sort_direction': 'sort_direction',
            'timezone': 'timezone',
            'accounts': 'accounts',
            'destination_address_country': 'destination_address_country',
            'destination_address': 'destination_address',
            'message_format': 'message_format',
            'metadata_key': 'metadata_key',
            'metadata_value': 'metadata_value',
            'source_address_country': 'source_address_country',
            'source_address': 'source_address',
            'action': 'action',
            'delivery_options': 'delivery_options'
        }

        self._start_date = start_date
        self._end_date = end_date
        self._sort_by = sort_by
        self._sort_direction = sort_direction
        self._timezone = timezone
        self._accounts = accounts
        self._destination_address_country = destination_address_country
        self._destination_address = destination_address
        self._message_format = message_format
        self._metadata_key = metadata_key
        self._metadata_value = metadata_value
        self._source_address_country = source_address_country
        self._source_address = source_address
        self._action = action
        self._delivery_options = delivery_options

    @property
    def start_date(self):
        """
        Gets the start_date of this AsyncReceivedMessagesDetailRequest.


        :return: The start_date of this AsyncReceivedMessagesDetailRequest.
        :rtype: StartDateBody
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this AsyncReceivedMessagesDetailRequest.


        :param start_date: The start_date of this AsyncReceivedMessagesDetailRequest.
        :type: StartDateBody
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this AsyncReceivedMessagesDetailRequest.


        :return: The end_date of this AsyncReceivedMessagesDetailRequest.
        :rtype: EndDateBody
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this AsyncReceivedMessagesDetailRequest.


        :param end_date: The end_date of this AsyncReceivedMessagesDetailRequest.
        :type: EndDateBody
        """

        self._end_date = end_date

    @property
    def sort_by(self):
        """
        Gets the sort_by of this AsyncReceivedMessagesDetailRequest.
        Field to sort results set by

        :return: The sort_by of this AsyncReceivedMessagesDetailRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """
        Sets the sort_by of this AsyncReceivedMessagesDetailRequest.
        Field to sort results set by

        :param sort_by: The sort_by of this AsyncReceivedMessagesDetailRequest.
        :type: str
        """
        allowed_values = ["ACCOUNT", "ACTION", "DESTINATION_ADDRESS", "DESTINATION_ADDRESS_COUNTRY", "FORMAT", "SOURCE_ADDRESS", "SOURCE_ADDRESS_COUNTRY", "TIMESTAMP"]
        if sort_by not in allowed_values:
            raise ValueError(
                "Invalid value for `sort_by` ({0}), must be one of {1}"
                .format(sort_by, allowed_values)
            )

        self._sort_by = sort_by

    @property
    def sort_direction(self):
        """
        Gets the sort_direction of this AsyncReceivedMessagesDetailRequest.


        :return: The sort_direction of this AsyncReceivedMessagesDetailRequest.
        :rtype: SortDirectionBody
        """
        return self._sort_direction

    @sort_direction.setter
    def sort_direction(self, sort_direction):
        """
        Sets the sort_direction of this AsyncReceivedMessagesDetailRequest.


        :param sort_direction: The sort_direction of this AsyncReceivedMessagesDetailRequest.
        :type: SortDirectionBody
        """

        self._sort_direction = sort_direction

    @property
    def timezone(self):
        """
        Gets the timezone of this AsyncReceivedMessagesDetailRequest.


        :return: The timezone of this AsyncReceivedMessagesDetailRequest.
        :rtype: TimezoneBody
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this AsyncReceivedMessagesDetailRequest.


        :param timezone: The timezone of this AsyncReceivedMessagesDetailRequest.
        :type: TimezoneBody
        """

        self._timezone = timezone

    @property
    def accounts(self):
        """
        Gets the accounts of this AsyncReceivedMessagesDetailRequest.


        :return: The accounts of this AsyncReceivedMessagesDetailRequest.
        :rtype: AccountsBody
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """
        Sets the accounts of this AsyncReceivedMessagesDetailRequest.


        :param accounts: The accounts of this AsyncReceivedMessagesDetailRequest.
        :type: AccountsBody
        """

        self._accounts = accounts

    @property
    def destination_address_country(self):
        """
        Gets the destination_address_country of this AsyncReceivedMessagesDetailRequest.


        :return: The destination_address_country of this AsyncReceivedMessagesDetailRequest.
        :rtype: DestinationAddressCountryBody
        """
        return self._destination_address_country

    @destination_address_country.setter
    def destination_address_country(self, destination_address_country):
        """
        Sets the destination_address_country of this AsyncReceivedMessagesDetailRequest.


        :param destination_address_country: The destination_address_country of this AsyncReceivedMessagesDetailRequest.
        :type: DestinationAddressCountryBody
        """

        self._destination_address_country = destination_address_country

    @property
    def destination_address(self):
        """
        Gets the destination_address of this AsyncReceivedMessagesDetailRequest.


        :return: The destination_address of this AsyncReceivedMessagesDetailRequest.
        :rtype: DestinationAddressBody
        """
        return self._destination_address

    @destination_address.setter
    def destination_address(self, destination_address):
        """
        Sets the destination_address of this AsyncReceivedMessagesDetailRequest.


        :param destination_address: The destination_address of this AsyncReceivedMessagesDetailRequest.
        :type: DestinationAddressBody
        """

        self._destination_address = destination_address

    @property
    def message_format(self):
        """
        Gets the message_format of this AsyncReceivedMessagesDetailRequest.


        :return: The message_format of this AsyncReceivedMessagesDetailRequest.
        :rtype: MessageFormatBody
        """
        return self._message_format

    @message_format.setter
    def message_format(self, message_format):
        """
        Sets the message_format of this AsyncReceivedMessagesDetailRequest.


        :param message_format: The message_format of this AsyncReceivedMessagesDetailRequest.
        :type: MessageFormatBody
        """

        self._message_format = message_format

    @property
    def metadata_key(self):
        """
        Gets the metadata_key of this AsyncReceivedMessagesDetailRequest.


        :return: The metadata_key of this AsyncReceivedMessagesDetailRequest.
        :rtype: MetadataKeyBody
        """
        return self._metadata_key

    @metadata_key.setter
    def metadata_key(self, metadata_key):
        """
        Sets the metadata_key of this AsyncReceivedMessagesDetailRequest.


        :param metadata_key: The metadata_key of this AsyncReceivedMessagesDetailRequest.
        :type: MetadataKeyBody
        """

        self._metadata_key = metadata_key

    @property
    def metadata_value(self):
        """
        Gets the metadata_value of this AsyncReceivedMessagesDetailRequest.


        :return: The metadata_value of this AsyncReceivedMessagesDetailRequest.
        :rtype: MetadataValueBody
        """
        return self._metadata_value

    @metadata_value.setter
    def metadata_value(self, metadata_value):
        """
        Sets the metadata_value of this AsyncReceivedMessagesDetailRequest.


        :param metadata_value: The metadata_value of this AsyncReceivedMessagesDetailRequest.
        :type: MetadataValueBody
        """

        self._metadata_value = metadata_value

    @property
    def source_address_country(self):
        """
        Gets the source_address_country of this AsyncReceivedMessagesDetailRequest.


        :return: The source_address_country of this AsyncReceivedMessagesDetailRequest.
        :rtype: SourceAddressCountryBody
        """
        return self._source_address_country

    @source_address_country.setter
    def source_address_country(self, source_address_country):
        """
        Sets the source_address_country of this AsyncReceivedMessagesDetailRequest.


        :param source_address_country: The source_address_country of this AsyncReceivedMessagesDetailRequest.
        :type: SourceAddressCountryBody
        """

        self._source_address_country = source_address_country

    @property
    def source_address(self):
        """
        Gets the source_address of this AsyncReceivedMessagesDetailRequest.


        :return: The source_address of this AsyncReceivedMessagesDetailRequest.
        :rtype: SourceAddressBody
        """
        return self._source_address

    @source_address.setter
    def source_address(self, source_address):
        """
        Sets the source_address of this AsyncReceivedMessagesDetailRequest.


        :param source_address: The source_address of this AsyncReceivedMessagesDetailRequest.
        :type: SourceAddressBody
        """

        self._source_address = source_address

    @property
    def action(self):
        """
        Gets the action of this AsyncReceivedMessagesDetailRequest.


        :return: The action of this AsyncReceivedMessagesDetailRequest.
        :rtype: ActionBody
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this AsyncReceivedMessagesDetailRequest.


        :param action: The action of this AsyncReceivedMessagesDetailRequest.
        :type: ActionBody
        """

        self._action = action

    @property
    def delivery_options(self):
        """
        Gets the delivery_options of this AsyncReceivedMessagesDetailRequest.


        :return: The delivery_options of this AsyncReceivedMessagesDetailRequest.
        :rtype: DeliveryOptionsBody
        """
        return self._delivery_options

    @delivery_options.setter
    def delivery_options(self, delivery_options):
        """
        Sets the delivery_options of this AsyncReceivedMessagesDetailRequest.


        :param delivery_options: The delivery_options of this AsyncReceivedMessagesDetailRequest.
        :type: DeliveryOptionsBody
        """

        self._delivery_options = delivery_options

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
