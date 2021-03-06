# coding: utf-8

"""
    CloudEmotion API v1

    CrowdEmotion API

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

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


class User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, num_id=None, uuid=None, email_address=None, first_name=None, last_name=None, role=None, username=None, group_id=None, company_id=None, verified=None, enabled=None):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'num_id': 'int',
            'uuid': 'str',
            'email_address': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'role': 'str',
            'username': 'str',
            'group_id': 'int',
            'company_id': 'int',
            'verified': 'bool',
            'enabled': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'num_id': 'numId',
            'uuid': 'uuid',
            'email_address': 'emailAddress',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'role': 'role',
            'username': 'username',
            'group_id': 'group_id',
            'company_id': 'company_id',
            'verified': 'verified',
            'enabled': 'enabled'
        }

        self._id = id
        self._num_id = num_id
        self._uuid = uuid
        self._email_address = email_address
        self._first_name = first_name
        self._last_name = last_name
        self._role = role
        self._username = username
        self._group_id = group_id
        self._company_id = company_id
        self._verified = verified
        self._enabled = enabled

    @property
    def id(self):
        """
        Gets the id of this User.
        

        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.
        

        :param id: The id of this User.
        :type: int
        """

        self._id = id

    @property
    def num_id(self):
        """
        Gets the num_id of this User.
        

        :return: The num_id of this User.
        :rtype: int
        """
        return self._num_id

    @num_id.setter
    def num_id(self, num_id):
        """
        Sets the num_id of this User.
        

        :param num_id: The num_id of this User.
        :type: int
        """

        self._num_id = num_id

    @property
    def uuid(self):
        """
        Gets the uuid of this User.
        

        :return: The uuid of this User.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this User.
        

        :param uuid: The uuid of this User.
        :type: str
        """

        self._uuid = uuid

    @property
    def email_address(self):
        """
        Gets the email_address of this User.
        

        :return: The email_address of this User.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this User.
        

        :param email_address: The email_address of this User.
        :type: str
        """

        self._email_address = email_address

    @property
    def first_name(self):
        """
        Gets the first_name of this User.
        

        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this User.
        

        :param first_name: The first_name of this User.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this User.
        

        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this User.
        

        :param last_name: The last_name of this User.
        :type: str
        """

        self._last_name = last_name

    @property
    def role(self):
        """
        Gets the role of this User.
        

        :return: The role of this User.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this User.
        

        :param role: The role of this User.
        :type: str
        """

        self._role = role

    @property
    def username(self):
        """
        Gets the username of this User.
        

        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this User.
        

        :param username: The username of this User.
        :type: str
        """

        self._username = username

    @property
    def group_id(self):
        """
        Gets the group_id of this User.
        

        :return: The group_id of this User.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this User.
        

        :param group_id: The group_id of this User.
        :type: int
        """

        self._group_id = group_id

    @property
    def company_id(self):
        """
        Gets the company_id of this User.
        

        :return: The company_id of this User.
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """
        Sets the company_id of this User.
        

        :param company_id: The company_id of this User.
        :type: int
        """

        self._company_id = company_id

    @property
    def verified(self):
        """
        Gets the verified of this User.
        

        :return: The verified of this User.
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """
        Sets the verified of this User.
        

        :param verified: The verified of this User.
        :type: bool
        """

        self._verified = verified

    @property
    def enabled(self):
        """
        Gets the enabled of this User.
        

        :return: The enabled of this User.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this User.
        

        :param enabled: The enabled of this User.
        :type: bool
        """

        self._enabled = enabled

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
