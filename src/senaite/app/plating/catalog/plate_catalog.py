# -*- coding: utf-8 -*-

from App.class_init import InitializeClass
from zope.interface import implementer
from senaite.core.catalog.base_catalog import COLUMNS as BASE_COLUMNS
from senaite.core.catalog.base_catalog import INDEXES as BASE_INDEXES
from senaite.core.catalog.base_catalog import BaseCatalog
from senaite.app.plating.interfaces import IPlateCatalog


CATALOG_ID = "senaite_catalog_plate"
CATALOG_TITLE = "Senaite Plate Catalog"


INDEXES = BASE_INDEXES + [
    # id, indexed attribute, type
    ("plate_id", "", "FieldIndex"),
]

COLUMNS = BASE_COLUMNS + [
    # attribute name
    "plate_id",
]

TYPES = [
    # portal_type name
    "Plate"
]


@implementer(IPlateCatalog)
class PlateCatalog(BaseCatalog):
    """Catalog for Plates
    """
    def __init__(self):
        BaseCatalog.__init__(self, CATALOG_ID, title=CATALOG_TITLE)

    @property
    def mapped_catalog_types(self):
        return TYPES


InitializeClass(PlateCatalog)
