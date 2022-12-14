# -*- coding: utf-8 -*-
"""Serializers models for customerdataapi."""

from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from customerdataapi.models import CustomerData


class CustomerDataSerializer(serializers.ModelSerializer):
    """A simple serializer for our CustomerData model"""

    id = serializers.ReadOnlyField()  # pylint: disable=invalid-name
    data = serializers.JSONField()

    class Meta:
        """Meta class for ModelSerializer instance"""

        model = CustomerData
        fields = ('id', 'data')
