# -*- coding: utf-8 -*-

# from bika.lims import api

from senaite.app.plating import api
from senaite.app.plating import logger


def worksheet_created_event(worksheet, event):
    """"""
    # plate_folder = api.get_portal().get("plates")
    # plate = api.create(
    #     plate_folder,
    #     "Plate",
    # )
    # logger.info("Created plate {} for worksheet {}".format(plate, worksheet))
    # worksheet.plate_id = api.get_id(plate)
    # worksheet.reindexObject(idxs=["plate_searchable_id"])
    plate = api.create_plate(worksheet)
    logger.info("Created plate {} for worksheet {}".format(plate, worksheet))
    logger.info("LAYOUT: {}".format(plate.getLayout()))
    return

