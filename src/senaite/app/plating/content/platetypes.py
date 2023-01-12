# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.APP.PLATING.
#

from zope.interface import implementer

from plone.supermodel import model
from plone.dexterity.content import Container

from senaite.core.interfaces import IHideActionsMenu


class IPlateTypes(model.Schema):
    """"""


@implementer(IPlateTypes, IHideActionsMenu)
class PlateTypes(Container):
    """"""
