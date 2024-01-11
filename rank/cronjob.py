from rank.views import process_and_update_mongo


def cronjob():
    process_and_update_mongo(None)
