# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .influx_details import InfluxDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InfluxDetailsV1v8(InfluxDetails):
    """
    Influx details for V_1_8.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InfluxDetailsV1v8 object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_anomaly_detection.models.InfluxDetailsV1v8.influx_version` attribute
        of this class is ``V_1_8`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param influx_version:
            The value to assign to the influx_version property of this InfluxDetailsV1v8.
            Allowed values for this property are: "V_1_8", "V_2_0"
        :type influx_version: str

        :param database_name:
            The value to assign to the database_name property of this InfluxDetailsV1v8.
        :type database_name: str

        :param retention_policy_name:
            The value to assign to the retention_policy_name property of this InfluxDetailsV1v8.
        :type retention_policy_name: str

        """
        self.swagger_types = {
            'influx_version': 'str',
            'database_name': 'str',
            'retention_policy_name': 'str'
        }

        self.attribute_map = {
            'influx_version': 'influxVersion',
            'database_name': 'databaseName',
            'retention_policy_name': 'retentionPolicyName'
        }

        self._influx_version = None
        self._database_name = None
        self._retention_policy_name = None
        self._influx_version = 'V_1_8'

    @property
    def database_name(self):
        """
        **[Required]** Gets the database_name of this InfluxDetailsV1v8.
        DB Name for influx connection


        :return: The database_name of this InfluxDetailsV1v8.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this InfluxDetailsV1v8.
        DB Name for influx connection


        :param database_name: The database_name of this InfluxDetailsV1v8.
        :type: str
        """
        self._database_name = database_name

    @property
    def retention_policy_name(self):
        """
        Gets the retention_policy_name of this InfluxDetailsV1v8.
        retention policy is how long the bucket would last


        :return: The retention_policy_name of this InfluxDetailsV1v8.
        :rtype: str
        """
        return self._retention_policy_name

    @retention_policy_name.setter
    def retention_policy_name(self, retention_policy_name):
        """
        Sets the retention_policy_name of this InfluxDetailsV1v8.
        retention policy is how long the bucket would last


        :param retention_policy_name: The retention_policy_name of this InfluxDetailsV1v8.
        :type: str
        """
        self._retention_policy_name = retention_policy_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
