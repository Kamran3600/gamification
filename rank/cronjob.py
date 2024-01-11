import logging

from rank.views import process_and_update_mongo

logger = logging.getLogger(__name__)


def my_scheduled_job():
    process_and_update_mongo(None)
    logger.info("Cronjob ran successfully")
