# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoScalingConfiguration(object):
    """
    The information about the autoscale configuration.
    """

    #: A constant which can be used with the lifecycle_state property of a AutoScalingConfiguration.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AutoScalingConfiguration.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AutoScalingConfiguration.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AutoScalingConfiguration.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AutoScalingConfiguration.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AutoScalingConfiguration.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AutoScalingConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AutoScalingConfiguration.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AutoScalingConfiguration.
        :type display_name: str

        :param node_type:
            The value to assign to the node_type property of this AutoScalingConfiguration.
        :type node_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutoScalingConfiguration.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this AutoScalingConfiguration.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AutoScalingConfiguration.
        :type time_updated: datetime

        :param policy:
            The value to assign to the policy property of this AutoScalingConfiguration.
        :type policy: oci.bds.models.AutoScalePolicy

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'node_type': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'policy': 'AutoScalePolicy'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'node_type': 'nodeType',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'policy': 'policy'
        }

        self._id = None
        self._display_name = None
        self._node_type = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._policy = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutoScalingConfiguration.
        The unique identifier for the autoscale configuration.


        :return: The id of this AutoScalingConfiguration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutoScalingConfiguration.
        The unique identifier for the autoscale configuration.


        :param id: The id of this AutoScalingConfiguration.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AutoScalingConfiguration.
        A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.


        :return: The display_name of this AutoScalingConfiguration.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AutoScalingConfiguration.
        A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.


        :param display_name: The display_name of this AutoScalingConfiguration.
        :type: str
        """
        self._display_name = display_name

    @property
    def node_type(self):
        """
        **[Required]** Gets the node_type of this AutoScalingConfiguration.
        A node type that is managed by an autoscale configuration. The only supported type is WORKER.


        :return: The node_type of this AutoScalingConfiguration.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """
        Sets the node_type of this AutoScalingConfiguration.
        A node type that is managed by an autoscale configuration. The only supported type is WORKER.


        :param node_type: The node_type of this AutoScalingConfiguration.
        :type: str
        """
        self._node_type = node_type

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AutoScalingConfiguration.
        The state of the autoscale configuration.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AutoScalingConfiguration.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AutoScalingConfiguration.
        The state of the autoscale configuration.


        :param lifecycle_state: The lifecycle_state of this AutoScalingConfiguration.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AutoScalingConfiguration.
        The time the cluster was created, shown as an RFC 3339 formatted datetime string.


        :return: The time_created of this AutoScalingConfiguration.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AutoScalingConfiguration.
        The time the cluster was created, shown as an RFC 3339 formatted datetime string.


        :param time_created: The time_created of this AutoScalingConfiguration.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AutoScalingConfiguration.
        The time the autoscale configuration was updated, shown as an RFC 3339 formatted datetime string.


        :return: The time_updated of this AutoScalingConfiguration.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AutoScalingConfiguration.
        The time the autoscale configuration was updated, shown as an RFC 3339 formatted datetime string.


        :param time_updated: The time_updated of this AutoScalingConfiguration.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def policy(self):
        """
        **[Required]** Gets the policy of this AutoScalingConfiguration.

        :return: The policy of this AutoScalingConfiguration.
        :rtype: oci.bds.models.AutoScalePolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this AutoScalingConfiguration.

        :param policy: The policy of this AutoScalingConfiguration.
        :type: oci.bds.models.AutoScalePolicy
        """
        self._policy = policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
