# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAssetSummary(object):
    """
    Summary of the DataAsset.
    """

    #: A constant which can be used with the data_source_type property of a DataAssetSummary.
    #: This constant has a value of "ORACLE_OBJECT_STORAGE"
    DATA_SOURCE_TYPE_ORACLE_OBJECT_STORAGE = "ORACLE_OBJECT_STORAGE"

    #: A constant which can be used with the data_source_type property of a DataAssetSummary.
    #: This constant has a value of "ORACLE_ATP"
    DATA_SOURCE_TYPE_ORACLE_ATP = "ORACLE_ATP"

    #: A constant which can be used with the data_source_type property of a DataAssetSummary.
    #: This constant has a value of "INFLUX"
    DATA_SOURCE_TYPE_INFLUX = "INFLUX"

    def __init__(self, **kwargs):
        """
        Initializes a new DataAssetSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DataAssetSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DataAssetSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this DataAssetSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DataAssetSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this DataAssetSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DataAssetSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DataAssetSummary.
        :type lifecycle_state: str

        :param project_id:
            The value to assign to the project_id property of this DataAssetSummary.
        :type project_id: str

        :param data_source_type:
            The value to assign to the data_source_type property of this DataAssetSummary.
            Allowed values for this property are: "ORACLE_OBJECT_STORAGE", "ORACLE_ATP", "INFLUX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_source_type: str

        :param private_endpoint_id:
            The value to assign to the private_endpoint_id property of this DataAssetSummary.
        :type private_endpoint_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DataAssetSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DataAssetSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DataAssetSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'project_id': 'str',
            'data_source_type': 'str',
            'private_endpoint_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'project_id': 'projectId',
            'data_source_type': 'dataSourceType',
            'private_endpoint_id': 'privateEndpointId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._project_id = None
        self._data_source_type = None
        self._private_endpoint_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DataAssetSummary.
        Unique identifier that is immutable on creation


        :return: The id of this DataAssetSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DataAssetSummary.
        Unique identifier that is immutable on creation


        :param id: The id of this DataAssetSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DataAssetSummary.
        Compartment Identifier


        :return: The compartment_id of this DataAssetSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DataAssetSummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this DataAssetSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DataAssetSummary.
        DataAsset Identifier, can be renamed


        :return: The display_name of this DataAssetSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DataAssetSummary.
        DataAsset Identifier, can be renamed


        :param display_name: The display_name of this DataAssetSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this DataAssetSummary.
        A short description of the Ai data asset


        :return: The description of this DataAssetSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DataAssetSummary.
        A short description of the Ai data asset


        :param description: The description of this DataAssetSummary.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DataAssetSummary.
        The time the the DataAsset was created. An RFC3339 formatted datetime string


        :return: The time_created of this DataAssetSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DataAssetSummary.
        The time the the DataAsset was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this DataAssetSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DataAssetSummary.
        The time the the DataAsset was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this DataAssetSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DataAssetSummary.
        The time the the DataAsset was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this DataAssetSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DataAssetSummary.
        The current state of the data asset.


        :return: The lifecycle_state of this DataAssetSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DataAssetSummary.
        The current state of the data asset.


        :param lifecycle_state: The lifecycle_state of this DataAssetSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this DataAssetSummary.
        Unique identifier for a project that is immutable on creation


        :return: The project_id of this DataAssetSummary.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this DataAssetSummary.
        Unique identifier for a project that is immutable on creation


        :param project_id: The project_id of this DataAssetSummary.
        :type: str
        """
        self._project_id = project_id

    @property
    def data_source_type(self):
        """
        **[Required]** Gets the data_source_type of this DataAssetSummary.
        Data source type where actually data asset is being stored

        Allowed values for this property are: "ORACLE_OBJECT_STORAGE", "ORACLE_ATP", "INFLUX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_source_type of this DataAssetSummary.
        :rtype: str
        """
        return self._data_source_type

    @data_source_type.setter
    def data_source_type(self, data_source_type):
        """
        Sets the data_source_type of this DataAssetSummary.
        Data source type where actually data asset is being stored


        :param data_source_type: The data_source_type of this DataAssetSummary.
        :type: str
        """
        allowed_values = ["ORACLE_OBJECT_STORAGE", "ORACLE_ATP", "INFLUX"]
        if not value_allowed_none_or_none_sentinel(data_source_type, allowed_values):
            data_source_type = 'UNKNOWN_ENUM_VALUE'
        self._data_source_type = data_source_type

    @property
    def private_endpoint_id(self):
        """
        Gets the private_endpoint_id of this DataAssetSummary.
        OCID of Private Endpoint.


        :return: The private_endpoint_id of this DataAssetSummary.
        :rtype: str
        """
        return self._private_endpoint_id

    @private_endpoint_id.setter
    def private_endpoint_id(self, private_endpoint_id):
        """
        Sets the private_endpoint_id of this DataAssetSummary.
        OCID of Private Endpoint.


        :param private_endpoint_id: The private_endpoint_id of this DataAssetSummary.
        :type: str
        """
        self._private_endpoint_id = private_endpoint_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DataAssetSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DataAssetSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DataAssetSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DataAssetSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DataAssetSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DataAssetSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DataAssetSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DataAssetSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DataAssetSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DataAssetSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DataAssetSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DataAssetSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
