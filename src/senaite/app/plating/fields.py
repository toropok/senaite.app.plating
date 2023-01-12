# -*- coding: utf-8 -*-

from Products.Archetypes.Field import LinesField
from Products.Archetypes.atapi import StringField
from Products.Archetypes.atapi import ReferenceField
from Products.Archetypes.atapi import ComputedField
from archetypes.schemaextender.field import ExtensionField

from senaite.core.browser.fields.records import RecordsField
from senaite.core.browser.fields.datetime import DateTimeField

from senaite.core.schema import UIDReferenceField

from zope.interface import implementer

from senaite.app.plating.interfaces import IPlateUIDReferenceField


class ExtRecordsField(ExtensionField, RecordsField):
    """Extended Records Field
    """


class ExtLinesField(ExtensionField, LinesField):
    """Extended Lines Field
    """


class ExtStringField(ExtensionField, StringField):
    """Extended String Field
    """


class ExtReferenceField(ExtensionField, ReferenceField):
    """Extended Reference Field
    """


class ExtDateTimeField(ExtensionField, DateTimeField):
    """Extended DateTime Field
    """


class ExtComputedField(ExtensionField, ComputedField):
    """Extended Computed Field
    """


@implementer(IPlateUIDReferenceField)
class AnalysisUIDReferenceField(UIDReferenceField):
    """
    """
