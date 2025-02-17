# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FlexV1KeysPost200ResponseDer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'format': 'str',
        'algorithm': 'str',
        'public_key': 'str'
    }

    attribute_map = {
        'format': 'format',
        'algorithm': 'algorithm',
        'public_key': 'publicKey'
    }

    def __init__(self, format=None, algorithm=None, public_key=None):
        """
        FlexV1KeysPost200ResponseDer - a model defined in Swagger
        """

        self._format = None
        self._algorithm = None
        self._public_key = None

        if format is not None:
          self.format = format
        if algorithm is not None:
          self.algorithm = algorithm
        if public_key is not None:
          self.public_key = public_key

    @property
    def format(self):
        """
        Gets the format of this FlexV1KeysPost200ResponseDer.
        Specifies the format of the public key; currently X.509.

        :return: The format of this FlexV1KeysPost200ResponseDer.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this FlexV1KeysPost200ResponseDer.
        Specifies the format of the public key; currently X.509.

        :param format: The format of this FlexV1KeysPost200ResponseDer.
        :type: str
        """

        self._format = format

    @property
    def algorithm(self):
        """
        Gets the algorithm of this FlexV1KeysPost200ResponseDer.
        Algorithm used to encrypt the public key.

        :return: The algorithm of this FlexV1KeysPost200ResponseDer.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """
        Sets the algorithm of this FlexV1KeysPost200ResponseDer.
        Algorithm used to encrypt the public key.

        :param algorithm: The algorithm of this FlexV1KeysPost200ResponseDer.
        :type: str
        """

        self._algorithm = algorithm

    @property
    def public_key(self):
        """
        Gets the public_key of this FlexV1KeysPost200ResponseDer.
        Base64 encoded public key value.

        :return: The public_key of this FlexV1KeysPost200ResponseDer.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this FlexV1KeysPost200ResponseDer.
        Base64 encoded public key value.

        :param public_key: The public_key of this FlexV1KeysPost200ResponseDer.
        :type: str
        """

        self._public_key = public_key

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
        if not isinstance(other, FlexV1KeysPost200ResponseDer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
