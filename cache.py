from typing import Any
import pickle


def storeData(filepath: str, obj: Any):

    # Its important to use binary mode
    dbfile = open(filepath, 'ab')

    # source, destination
    pickle.dump(obj, dbfile)
    dbfile.close()


def loadData(filepath: str) -> Any:
    # for reading also binary mode is important
    try:
        dbfile = open(filepath, 'rb')
        return pickle.load(dbfile)
    finally:
        dbfile.close()
