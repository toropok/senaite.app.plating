# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.APP.PLATING.
#

from zope.interface import implements

from bika.lims import api
from bika.lims.interfaces import IDuplicateAnalysis
from bika.lims.interfaces import IReferenceAnalysis
from bika.lims.interfaces import IRoutineAnalysis
from bika.lims.interfaces import IWorksheetLayouts
from bika.lims.browser.worksheet.views.analyses import AnalysesView

from senaite.app.plating import messageFactory as _


class PlatingLayouts(object):
    implements(IWorksheetLayouts)

    def getLayouts(self):
        return (
             ("plate_base_view", u"Plate base view"),
        )


class PlateBaseView(AnalysesView):
    """"""

    def __init__(self, context, request):
        super(PlateBaseView, self).__init__(context, request)

    def before_render(self):
        super(PlateBaseView, self).before_render()
        custom_transitions = [{
            "id": "add_multiwellplate",
            "title": _("Add Plate"),
            "url": "{}/workflow_action?action={}".format(
                api.get_url(self.context), "add_multiwellplate"),
        }]

        for review_state in self.review_states:
            review_state.setdefault("custom_transitions", []).extend(custom_transitions)

