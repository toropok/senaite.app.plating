# -*- coding: utf-8 -*-

from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier

from Products.Archetypes.public import ReferenceWidget

from zope.interface import implements
from zope.component import adapts

from bika.lims.interfaces import IWorksheetTemplate

from senaite.app.plating import messageFactory as _
from senaite.app.plating.fields import ExtReferenceField


class PlateTypeSchemaExtender(object):
    adapts(IWorksheetTemplate)
    implements(IOrderableSchemaExtender)

    def __init__(self, context):
        self.context = context
        self.fields = [
            ExtReferenceField(
                'plate_type',
                schemata='Plating',
                required=False,
                multi_valued=False,
                allowed_types=('PlateType',),
                relationship='WorksheetPlateType',
                widget=ReferenceWidget(
                    checkbox_bound=0,
                    label=_('Plate type'),
                    description=_('Select the preferred plate type'),
                ),
            )
        ]

    def getOrder(self, schematas):
        return schematas

    def getFields(self):
        return self.fields


class PlateTypeSchemaModifier(object):
    adapts(IWorksheetTemplate)
    implements(ISchemaModifier)

    def __init__(self, context):
        self.context = context

    def fiddle(self, schema):
        return schema
