# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.APP.PLATING.
#

from AccessControl import ClassSecurityInfo

from zope.interface import implementer

from plone.autoform import directives
from plone.supermodel import model
from plone.dexterity.content import Item

from Products.CMFCore import permissions

from bika.lims import api
from bika.lims.catalog import SETUP_CATALOG

from senaite.core.schema import IntField
from senaite.core.z3cform.widgets.number import IntFieldWidget

from senaite.app.plating import messageFactory as _
from senaite.app.plating.interfaces import IPlateType


class IPlateTypeSchema(model.Schema):
    """
    """
    directives.widget(
        "rows",
        IntFieldWidget,
    )
    rows = IntField(
        title=_(u"Row counts"),
        default=8,
        min=1,
        max=48,
    )

    directives.widget(
        "cols",
        IntFieldWidget,
    )
    cols = IntField(
        title=_(u"Column counts"),
        default=12,
        min=1,
        max=72,
    )


@implementer(IPlateType, IPlateTypeSchema)
class PlateType(Item):
    """
    """

    _catalogs = [SETUP_CATALOG]

    security = ClassSecurityInfo()
    exclude_from_nav = True

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

    @security.protected(permissions.ModifyPortalContent)
    def setRows(self, value):
        mutator = self.mutator("rows")
        mutator(self.context, value)

    @security.protected(permissions.View)
    def getRows(self):
        accessor = self.accessor("rows")
        return accessor(self)

    @security.protected(permissions.ModifyPortalContent)
    def setCols(self, value):
        mutator = self.mutator("cols")
        mutator(self.context, value)

    @security.protected(permissions.View)
    def getCols(self):
        accessor = self.accessor("cols")
        return accessor(self)
