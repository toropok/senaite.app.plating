# -*- coding: utf-8 -*-

from senaite.core.interfaces import ISenaiteCatalogObject
from senaite.lims.interfaces import ISenaiteLIMS
from senaite.core.schema.interfaces import IUIDReferenceField
from zope.interface import interface


class ISenaitePlatingLayer(ISenaiteLIMS):
    """Senaite Plating Browser Layer Interface
    """


class IPlateCatalog(ISenaiteCatalogObject):
    """Marker interface for Plate Catalog
    """


class IPlated(interface.Interface):
    """Marker interface for Analysis being plated to the particular plate
    """


class IPlate(interface.Interface):
    """Marker interface for Plates
    """


class IPlateType(interface.Interface):
    """Marker interface for Plate types
    """


class IPlateUIDReferenceField(IUIDReferenceField):
    """
    """