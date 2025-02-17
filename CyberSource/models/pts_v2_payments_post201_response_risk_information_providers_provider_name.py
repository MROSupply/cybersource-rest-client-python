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


class PtsV2PaymentsPost201ResponseRiskInformationProvidersProviderName(object):
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
        'field_name': 'list[str]',
        'field_value': 'list[str]'
    }

    attribute_map = {
        'field_name': 'fieldName',
        'field_value': 'fieldValue'
    }

    def __init__(self, field_name=None, field_value=None):
        """
        PtsV2PaymentsPost201ResponseRiskInformationProvidersProviderName - a model defined in Swagger
        """

        self._field_name = None
        self._field_value = None

        if field_name is not None:
          self.field_name = field_name
        if field_value is not None:
          self.field_value = field_value

    @property
    def field_name(self):
        """
        Gets the field_name of this PtsV2PaymentsPost201ResponseRiskInformationProvidersProviderName.

        :return: The field_name of this PtsV2PaymentsPost201ResponseRiskInformationProvidersProviderName.
        :rtype: list[str]
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this PtsV2PaymentsPost201ResponseRiskInformationProvidersProviderName.

        :param field_name: The field_name of this PtsV2PaymentsPost201ResponseRiskInformationProvidersProviderName.
        :type: list[str]
        """

        self._field_name = field_name

    @property
    def field_value(self):
        """
        Gets the field_value of this PtsV2PaymentsPost201ResponseRiskInformationProvidersProviderName.

        :return: The field_value of this PtsV2PaymentsPost201ResponseRiskInformationProvidersProviderName.
        :rtype: list[str]
        """
        return self._field_value

    @field_value.setter
    def field_value(self, field_value):
        """
        Sets the field_value of this PtsV2PaymentsPost201ResponseRiskInformationProvidersProviderName.

        :param field_value: The field_value of this PtsV2PaymentsPost201ResponseRiskInformationProvidersProviderName.
        :type: list[str]
        """

        self._field_value = field_value

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseRiskInformationProvidersProviderName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
