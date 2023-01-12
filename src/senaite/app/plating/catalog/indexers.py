# -*- coding: utf-8 -*-

from plone.indexer import indexer
from senaite.app.plating.interfaces import IPlate


@indexer(IPlate)
def plate_searchable_id(instance):
    """Index for searchable Plate ID queries
    """
    searchable_text_tokens = [
        instance.getPlateID(),
    ]
    searchable_text_tokens = filter(None, searchable_text_tokens)
    return " ".join(searchable_text_tokens)
