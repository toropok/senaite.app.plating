# -*- coding: utf-8 -*-

from AccessControl.SecurityInfo import ModuleSecurityInfo
from zope.i18nmessageid import MessageFactory

import logging

PRODUCT_NAME = "senaite.app.plating"

security = ModuleSecurityInfo("senaite.app.plating")

messageFactory = MessageFactory(PRODUCT_NAME)

logger = logging.getLogger(PRODUCT_NAME)


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    logger.info("*** Initializing SENAITE.APP.PLATING ***")
