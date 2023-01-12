# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.APP.PLATING.
#

from plone.dexterity.content import Container
from plone.supermodel import model
from senaite.app.plating.interfaces import IPlateTypes
from senaite.core.interfaces import IHideActionsMenu
from zope.interface import implementer


class IPlateTypesSchema(model.Schema):
    """
    """
    pass


@implementer(IPlateTypes, IPlateTypesSchema, IHideActionsMenu)
class PlateTypes(Container):
    """
    """
    pass
