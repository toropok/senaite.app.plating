# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.APP.PLATING.
#

import collections

from bika.lims.catalog import SETUP_CATALOG
from bika.lims.utils import get_link_for
from senaite.app.listing import ListingView
from senaite.app.plating import messageFactory as _


class PlateTypesView(ListingView):
    """"""

    def __init__(self, context, request):
        super(PlateTypesView, self).__init__(context, request)

        # self.catalog = SETUP_CATALOG

        self.contentFilter = {
            "portal_type": "PlateType",
            "sort_on": "created",
        }

        self.context_actions = {
            _("Add"): {
                "url": "++add++PlateType",
                "icon": "add.png"}
        }
        self.title = _("Plate types")
        self.description = _("")
        self.show_select_column = True
        self.pagesize = 25
        self.icon = "{}/{}".format(self.portal_url, "senaite_theme/icon/platetype")

        self.columns = collections.OrderedDict((
            ("Title", {
                "title": _("Title"),
                "index": "sortable_title"}),
            ("Description", {
                "title": _("Description"),
                "index": "Description"}),
        ))

        self.review_states = [
            {
                "id": "default",
                "title": _("Active"),
                "contentFilter": {"is_active": True},
                "transitions": [],
                "columns": self.columns.keys(),
            }, {
                "id": "inactive",
                "title": _("Inactive"),
                "contentFilter": {'is_active': False},
                "transitions": [],
                "columns": self.columns.keys(),
            }, {
                "id": "all",
                "title": _("All"),
                "contentFilter": {},
                "columns": self.columns.keys(),
            },
        ]

    def update(self):
        """Update hook
        """
        super(PlateTypesView, self).update()

    def before_render(self):
        """Before template render hook
        """
        super(PlateTypesView, self).before_render()

    def folderitem(self, obj, item, index):
        """Service triggered each time an item is iterated in folderitems.
        The use of this service prevents the extra-loops in child objects.
        :obj: the instance of the class to be foldered
        :item: dict containing the properties of the object to be used by
            the template
        :index: current index of the item
        """
        item["replace"]["Title"] = get_link_for(obj)
        return item
