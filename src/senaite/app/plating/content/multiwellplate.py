# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.APP.PLATING.
#
# see: https://en.wikipedia.org/wiki/Microplate#cite_note-1

from AccessControl import ClassSecurityInfo

from zope import schema
from zope.interface import implementer

from plone.autoform import directives
from plone.supermodel import model
from plone.dexterity.content import Container
from plone.dexterity.content import Item

from Products.CMFCore import permissions
from Products.CMFPlone.utils import safe_unicode

from bika.lims import api

from senaite.core.schema.fields import DataGridField
from senaite.core.schema.fields import DataGridRow
from senaite.core.z3cform.widgets.datagrid import DataGridWidgetFactory

from senaite.app.plating import messageFactory as _
from senaite.app.plating.catalog.plate_catalog import CATALOG_ID
from senaite.app.plating.interfaces import IPlate
from senaite.app.plating.content.schema import IWellSchema
from senaite.app.plating import logger

from senaite.core.catalog import WORKSHEET_CATALOG

from senaite.core.schema import UIDReferenceField
from senaite.core.catalog import ANALYSIS_CATALOG
from senaite.core.z3cform.widgets.uidreference import UIDReferenceWidgetFactory


class IMultiwellPlateSchema(model.Schema):
    """Plate content-type schema
    """
    directives.omitted("title")
    title = schema.TextLine(
        title=u"Title",
        required=False
    )

    directives.omitted("description")
    description = schema.Text(
        title=u"Description",
        required=False
    )

    directives.widget(
        "layout",
        DataGridWidgetFactory,
        allow_reorder=True,
        allow_insert=False,
        allow_delete=False,
        auto_append=False,
    )
    layout = DataGridField(
        title=_("Layout"),
        value_type=DataGridRow(schema=IWellSchema),
        required=False,
        missing_value=[],
        default=[],
    )


@implementer(IPlate, IMultiwellPlateSchema)
class MultiwellPlate(Item):
    """
    """

    _catalogs = [CATALOG_ID]

    security = ClassSecurityInfo()

    def Title(self):
        return safe_unicode(self.getId()).encode('utf-8')

    @security.private
    def accessor(self, fieldname, raw=False):
        """Return the field accessor for the fieldname
        """
        schema = api.get_schema(self)
        if fieldname not in schema:
            return None
        field = schema[fieldname]
        if raw:
            if hasattr(field, "get_raw"):
                return field.get_raw
            return field.getRaw
        return field.get

    @security.private
    def mutator(self, fieldname):
        """Return the field mutator for the fieldname
        """
        schema = api.get_schema(self)
        if fieldname not in schema:
            return None
        return schema[fieldname].set

    @security.private
    def get_available_analyses_query(self):
        query = {
            "portal_type": "Worksheet",
            "plate_id": api.get_id(self),
        }
        brains = api.search(query, WORKSHEET_CATALOG)
        worksheets = map(api.get_object, brains)
        uids = []
        if len(worksheets) > 0:
            uids = map(api.get_uid, worksheets[0].getAnalyses())

        return {
            "portal_type": "Analysis",
            "UID": uids,
            "is_active": True,
            "isSampleReceived": True,
            "review_state": "assigned",
            "sort_on": "getPrioritySortkey",
            "sort_order": "ascending",
        }

    def get_labels(self):
        pass

    def get_rows_labels(self):
        pass

    def get_cols_labels(self):
        pass

    def get_well(self, row=None, col=None):
        pass

    def get_row(self, row=None):
        pass

    def get_col(self, col=None):
        pass

#assign/unassign
    def assign_analysis(self, row=None, col=None):
        pass

    def assign_analyses(self):
        pass

    def unassign_analysis(self):
        pass

    def unassign_analyses(self):
        pass

    @security.protected(permissions.View)
    def getLayout(self):
        accessor = self.accessor("layout", raw=False)
        return accessor(self)

    @security.protected(permissions.ModifyPortalContent)
    def setLayout(self, value):
        mutator = self.mutator("layout")
        mutator(self, value)
