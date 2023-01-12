# -*- coding: utf-8 -*-

from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier

from zope.interface import implements
from zope.component import adapts

from bika.lims.interfaces import IWorksheet

from senaite.app.plating.fields import ExtReferenceField
from senaite.app.plating.permissions import AddPlate


class PlateWorksheetSchemaExtender(object):
    adapts(IWorksheet)
    implements(IOrderableSchemaExtender)

    def __init__(self, context):
        self.context = context
        self.fields = [
            ExtReferenceField(
                'plate_id',
                required=False,
                multi_valued=False,
                read_permission=AddPlate,
                write_permission=AddPlate,
                allowed_types=('Plate',),
                relationship='WorksheetPlate',
            ),
        ]

    def getOrder(self, schematas):
        return schematas

    def getFields(self):
        return self.fields


class PlateWorksheetSchemaModifier(object):
    adapts(IWorksheet)
    implements(ISchemaModifier)

    def __init__(self, context):
        self.context = context

    def fiddle(self, schema):
        return schema
