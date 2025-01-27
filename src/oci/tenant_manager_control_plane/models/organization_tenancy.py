# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OrganizationTenancy(object):
    """
    The information about the OrganizationTenancy.
    """

    #: A constant which can be used with the lifecycle_state property of a OrganizationTenancy.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OrganizationTenancy.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OrganizationTenancy.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OrganizationTenancy.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OrganizationTenancy.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a OrganizationTenancy.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the role property of a OrganizationTenancy.
    #: This constant has a value of "PARENT"
    ROLE_PARENT = "PARENT"

    #: A constant which can be used with the role property of a OrganizationTenancy.
    #: This constant has a value of "CHILD"
    ROLE_CHILD = "CHILD"

    #: A constant which can be used with the role property of a OrganizationTenancy.
    #: This constant has a value of "NONE"
    ROLE_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new OrganizationTenancy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tenancy_id:
            The value to assign to the tenancy_id property of this OrganizationTenancy.
        :type tenancy_id: str

        :param name:
            The value to assign to the name property of this OrganizationTenancy.
        :type name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OrganizationTenancy.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETED", "FAILED", "DELETING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param role:
            The value to assign to the role property of this OrganizationTenancy.
            Allowed values for this property are: "PARENT", "CHILD", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        :param time_joined:
            The value to assign to the time_joined property of this OrganizationTenancy.
        :type time_joined: datetime

        :param time_left:
            The value to assign to the time_left property of this OrganizationTenancy.
        :type time_left: datetime

        :param is_approved_for_transfer:
            The value to assign to the is_approved_for_transfer property of this OrganizationTenancy.
        :type is_approved_for_transfer: bool

        """
        self.swagger_types = {
            'tenancy_id': 'str',
            'name': 'str',
            'lifecycle_state': 'str',
            'role': 'str',
            'time_joined': 'datetime',
            'time_left': 'datetime',
            'is_approved_for_transfer': 'bool'
        }

        self.attribute_map = {
            'tenancy_id': 'tenancyId',
            'name': 'name',
            'lifecycle_state': 'lifecycleState',
            'role': 'role',
            'time_joined': 'timeJoined',
            'time_left': 'timeLeft',
            'is_approved_for_transfer': 'isApprovedForTransfer'
        }

        self._tenancy_id = None
        self._name = None
        self._lifecycle_state = None
        self._role = None
        self._time_joined = None
        self._time_left = None
        self._is_approved_for_transfer = None

    @property
    def tenancy_id(self):
        """
        **[Required]** Gets the tenancy_id of this OrganizationTenancy.
        OCID of the tenancy.


        :return: The tenancy_id of this OrganizationTenancy.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this OrganizationTenancy.
        OCID of the tenancy.


        :param tenancy_id: The tenancy_id of this OrganizationTenancy.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def name(self):
        """
        Gets the name of this OrganizationTenancy.
        Name of the tenancy.


        :return: The name of this OrganizationTenancy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrganizationTenancy.
        Name of the tenancy.


        :param name: The name of this OrganizationTenancy.
        :type: str
        """
        self._name = name

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this OrganizationTenancy.
        Lifecycle state of the OrganizationTenancy.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETED", "FAILED", "DELETING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OrganizationTenancy.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OrganizationTenancy.
        Lifecycle state of the OrganizationTenancy.


        :param lifecycle_state: The lifecycle_state of this OrganizationTenancy.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETED", "FAILED", "DELETING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def role(self):
        """
        Gets the role of this OrganizationTenancy.
        Role of the OrganizationTenancy.

        Allowed values for this property are: "PARENT", "CHILD", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this OrganizationTenancy.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this OrganizationTenancy.
        Role of the OrganizationTenancy.


        :param role: The role of this OrganizationTenancy.
        :type: str
        """
        allowed_values = ["PARENT", "CHILD", "NONE"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def time_joined(self):
        """
        Gets the time_joined of this OrganizationTenancy.
        Date-time when this tenancy joined the organization.


        :return: The time_joined of this OrganizationTenancy.
        :rtype: datetime
        """
        return self._time_joined

    @time_joined.setter
    def time_joined(self, time_joined):
        """
        Sets the time_joined of this OrganizationTenancy.
        Date-time when this tenancy joined the organization.


        :param time_joined: The time_joined of this OrganizationTenancy.
        :type: datetime
        """
        self._time_joined = time_joined

    @property
    def time_left(self):
        """
        Gets the time_left of this OrganizationTenancy.
        Date-time when this tenancy left the organization.


        :return: The time_left of this OrganizationTenancy.
        :rtype: datetime
        """
        return self._time_left

    @time_left.setter
    def time_left(self, time_left):
        """
        Sets the time_left of this OrganizationTenancy.
        Date-time when this tenancy left the organization.


        :param time_left: The time_left of this OrganizationTenancy.
        :type: datetime
        """
        self._time_left = time_left

    @property
    def is_approved_for_transfer(self):
        """
        Gets the is_approved_for_transfer of this OrganizationTenancy.
        Flag to indicate the tenancy is approved for transfer to another organization.


        :return: The is_approved_for_transfer of this OrganizationTenancy.
        :rtype: bool
        """
        return self._is_approved_for_transfer

    @is_approved_for_transfer.setter
    def is_approved_for_transfer(self, is_approved_for_transfer):
        """
        Sets the is_approved_for_transfer of this OrganizationTenancy.
        Flag to indicate the tenancy is approved for transfer to another organization.


        :param is_approved_for_transfer: The is_approved_for_transfer of this OrganizationTenancy.
        :type: bool
        """
        self._is_approved_for_transfer = is_approved_for_transfer

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
