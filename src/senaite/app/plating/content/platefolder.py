# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.APP.PLATING.
#

from zope.interface import implementer
from plone.dexterity.content import Container
from plone.supermodel import model
from senaite.core.interfaces import IHideActionsMenu


class IPlateFolder(model.Schema):
    """Plate Folder Interface
    """
    pass


@implementer(IPlateFolder, IHideActionsMenu)
class PlateFolder(Container):
    """Plate Folder
    """
    pass
