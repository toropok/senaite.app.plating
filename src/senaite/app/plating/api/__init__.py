# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.APP.PLATING.
#

from zope.component import getUtility
from zope.component.interfaces import IFactory

from Products.CMFPlone.utils import safe_unicode

from bika.lims import api
from bika.lims.utils import tmpID

from zope.event import notify
from zope.lifecycleevent import ObjectCreatedEvent


def create_plate(worksheet, *args, **kwargs):
    """Creates Plate object

    This code uses most of the parts from the TypesTool
    see: `bika.lims.api.create`

    :param worksheet: The created Worksheet
    :type worksheet: object
    :returns: The new created object
    """

    container = api.get_portal().get("plates")
    portal_type = "Plate"
    id = kwargs.pop("id", tmpID())
    title = kwargs.pop("title", "New {}".format(portal_type))

    # get the fti
    types_tool = api.get_tool("portal_types")
    fti = types_tool.getTypeInfo(portal_type)

    # newstyle factory
    factory = getUtility(IFactory, fti.factory)
    obj = factory(id, *args, **kwargs)
    if hasattr(obj, '_setPortalTypeName'):
        obj._setPortalTypeName(fti.getId())
    # set the title
    obj.title = safe_unicode(title)
    obj.layout = [dict(analyses=[], substances=[])] * 96
    # notify that the object was created
    notify(ObjectCreatedEvent(obj))
    # notifies ObjectWillBeAddedEvent, ObjectAddedEvent and
    # ContainerModifiedEvent
    container._setObject(id, obj)
    # we get the object here with the current object id, as it might be
    # renamed already by an event handler
    obj = container._getOb(obj.getId())

    worksheet.plate_id = api.get_id(obj)
    worksheet.reindexObject(idxs=["plate_searchable_id"])

    return obj
