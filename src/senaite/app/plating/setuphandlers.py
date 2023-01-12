# -*- coding: utf-8 -*-

from bika.lims import api

from senaite.core.catalog import WORKSHEET_CATALOG
from senaite.core.setuphandlers import add_dexterity_items
from senaite.core.setuphandlers import setup_core_catalogs
from senaite.core.setuphandlers import setup_other_catalogs

from senaite.app.plating import messageFactory as _
from senaite.app.plating import logger
from senaite.app.plating import PRODUCT_NAME
from senaite.app.plating.catalog.plate_catalog import PlateCatalog


PROFILE_ID = "profile-{}:default".format(PRODUCT_NAME)

CATALOGS = (
    PlateCatalog,
)

OTHER_INDEXES = [
    (WORKSHEET_CATALOG, "plate_id", "", "FieldIndex"),
]

ID_FORMATTING = [
    {
        "portal_type": "Plate",
        "form": "PL{seq:06d}",
        "prefix": "plate",
        "sequence_type": "generated",
        "counter_type": "",
        "split_length": 1,
    },
]


def setup_handler(context):
    """Generic setup handler"""
    if context.readDataFile("{}.txt".format(PRODUCT_NAME)) is None:
        return

    logger.info("{} setup handler [BEGIN]".format(PRODUCT_NAME.upper()))
    portal = context.getSite()

    # Setup animal content type
    add_plate_folder(portal)

    # Setup catalogs
    setup_catalogs(portal)

    # Apply ID format to content types
    setup_id_formatting(portal)

    # Setup workflow (for field permissions mostly)
    # setup_workflow(portal)

    # Add PlateTypes to Setup
    add_dexterity_setup_items(portal)

    logger.info("{} setup handler [DONE]".format(PRODUCT_NAME.upper()))


def add_plate_folder(portal):
    """Adds the initial Plate folder"""
    if portal.get("plates") is None:
        logger.info("Adding Plate folder")
        portal.invokeFactory("PlateFolder", "plates", title=_("Plates"))


def setup_catalogs(portal):
    """Setup animal catalogs"""
    setup_core_catalogs(portal, catalog_classes=CATALOGS)
    setup_other_catalogs(portal, indexes=OTHER_INDEXES)


def setup_id_formatting(portal, format_definition=None):
    """Setup default ID formatting
    """
    if not format_definition:
        logger.info("Setting up ID formatting ...")
        for formatting in ID_FORMATTING:
            setup_id_formatting(portal, format_definition=formatting)
        logger.info("Setting up ID formatting [DONE]")
        return

    bs = portal.bika_setup
    p_type = format_definition.get("portal_type", None)
    if not p_type:
        return

    form = format_definition.get("form", "")
    if not form:
        logger.info("Param 'form' for portal type {} not set [SKIP")
        return

    logger.info("Applying format '{}' for {}".format(form, p_type))
    ids = list()
    for record in bs.getIDFormatting():
        if record.get('portal_type', '') == p_type:
            continue
        ids.append(record)
    ids.append(format_definition)
    bs.setIDFormatting(ids)


def add_dexterity_setup_items(portal):
    """Adds the Dexterity Container in the Setup Folder

    N.B.: We do this in code, because adding this as Generic Setup Profile in
          `profiles/default/structure` flushes the contents on every import.
    """
    # Tuples of ID, Title, FTI
    items = [
        ("plate_types",  # ID
         "Plate Types",  # Title
         "PlateTypes"),  # FTI
    ]
    setup = api.get_setup()
    logger.info("Add PlateTypes to Setup folder...")
    add_dexterity_items(setup, items)


def pre_install(portal_setup):
    """Runs before the first import step of the *default* profile
    This handler is registered as a *pre_handler* in the generic setup profile
    :param portal_setup: SetupTool
    """

    logger.info("{} pre-install handler [BEGIN]".format(PRODUCT_NAME.upper()))
    context = portal_setup._getImportContext(PROFILE_ID)  # noqa
    portal = context.getSite()  # noqa

    logger.info("{} pre-install handler [DONE]".format(PRODUCT_NAME.upper()))


def post_install(portal_setup):
    """Runs after the last import step of the *default* profile
    This handler is registered as a *post_handler* in the generic setup profile
    :param portal_setup: SetupTool
    """
    logger.info("{} install handler [BEGIN]".format(PRODUCT_NAME.upper()))
    # https://docs.plone.org/develop/addons/components/genericsetup.html#custom-installer-code-setuphandlers-py
    context = portal_setup._getImportContext(PROFILE_ID)
    portal = context.getSite()  # noqa

    logger.info("{} install handler [DONE]".format(PRODUCT_NAME.upper()))


def post_uninstall(portal_setup):
    """Runs after the last import step of the *uninstall* profile

    This handler is registered as a *post_handler* in the generic setup profile

    :param portal_setup: SetupTool
    """
    logger.info("{} uninstall handler [BEGIN]".format(PRODUCT_NAME.upper()))

    # https://docs.plone.org/develop/addons/components/genericsetup.html#custom-installer-code-setuphandlers-py
    profile_id = "profile-{}:uninstall".format(PRODUCT_NAME)
    context = portal_setup._getImportContext(profile_id)
    portal = context.getSite()  # noqa

    logger.info("{} uninstall handler [DONE]".format(PRODUCT_NAME.upper()))
