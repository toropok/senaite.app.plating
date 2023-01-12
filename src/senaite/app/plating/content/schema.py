# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.APP.PLATING.
#
# see: https://en.wikipedia.org/wiki/Microplate

from zope import schema
from zope.interface import Interface

from plone.autoform import directives

from senaite.core.schema import UIDReferenceField
from senaite.core.catalog import ANALYSIS_CATALOG
from senaite.core.z3cform.widgets.uidreference import UIDReferenceWidgetFactory

from senaite.app.plating import messageFactory as _
from senaite.app.plating.fields import AnalysisUIDReferenceField


class IWellSchema(Interface):
    """Well info sub-schema
    """
    directives.widget(
        "analyses",
        UIDReferenceWidgetFactory,
        catalog=ANALYSIS_CATALOG,
        query="get_available_analyses_query",
        columns=[
            {
                "name": "getRequestID",
                "width": "20",
                "align": "left",
                "label": _(u"Sample"),
            },
            {
                "name": "title",
                "width": "100",
                "align": "left",
                "label": _(u"Title"),
            },
        ],
        limit=15,
    )
    analyses = AnalysisUIDReferenceField(
        title=_(u"Analyses"),
        multi_valued=True,
        allowed_types=("Analysis",),
        required=False,
    )

    directives.widget(
        "substances",
        UIDReferenceWidgetFactory,
        catalog=ANALYSIS_CATALOG,
        query="get_available_analyses_query",
        columns=[
            {
                "name": "getRequestID",
                "width": "20",
                "align": "left",
                "label": _(u"Sample"),
            },
            {
                "name": "title",
                "width": "100",
                "align": "left",
                "label": _(u"Title"),
            },
        ],
        limit=15,
    )
    substances = AnalysisUIDReferenceField(
        title=_(u"Substances"),
        multi_valued=True,
        allowed_types=("Analysis",),
        required=False,
    )
