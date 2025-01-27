# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DevopsCodeRepositoryFilterAttributes(object):
    """
    Attributes to filter Devops Code Repository events
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DevopsCodeRepositoryFilterAttributes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param head_ref:
            The value to assign to the head_ref property of this DevopsCodeRepositoryFilterAttributes.
        :type head_ref: str

        """
        self.swagger_types = {
            'head_ref': 'str'
        }

        self.attribute_map = {
            'head_ref': 'headRef'
        }

        self._head_ref = None

    @property
    def head_ref(self):
        """
        Gets the head_ref of this DevopsCodeRepositoryFilterAttributes.
        Branch for push event


        :return: The head_ref of this DevopsCodeRepositoryFilterAttributes.
        :rtype: str
        """
        return self._head_ref

    @head_ref.setter
    def head_ref(self, head_ref):
        """
        Sets the head_ref of this DevopsCodeRepositoryFilterAttributes.
        Branch for push event


        :param head_ref: The head_ref of this DevopsCodeRepositoryFilterAttributes.
        :type: str
        """
        self._head_ref = head_ref

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
