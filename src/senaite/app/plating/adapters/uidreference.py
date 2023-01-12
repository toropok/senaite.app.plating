# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.APP.PLATING.
#

from zope.component import adapter

from z3c.form import interfaces

from senaite.app.plating.interfaces import IPlateUIDReferenceField

from senaite.core.z3cform.widgets.uidreference import UIDReferenceDataConverter


@adapter(IPlateUIDReferenceField, interfaces.IWidget)
class AnalysisUIDReferenceDataConverter(UIDReferenceDataConverter):
    """Converts the raw field data for widget/field usage
    """

    def toWidgetValue(self, value):
        return super(AnalysisUIDReferenceDataConverter, self).toWidgetValue(value)

    def toFieldValue(self, value):
        """Converts a unicode string to a list of UIDs
        """
        if not value:
            value = u""
        if isinstance(value, (list, tuple)):
            value = u"\n".join(value)

        # remove any blank lines at the end
        value = value.rstrip("\r\n")
        return super(AnalysisUIDReferenceDataConverter, self).toFieldValue(value)
