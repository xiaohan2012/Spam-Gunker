import pymongo
def get_db(db_name = "spambayes"):
    conn = pymongo.Connection()
    return conn[db_name]
