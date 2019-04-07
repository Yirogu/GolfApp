from sqlalchemy import create_engine
import sqlalchemy
from .Config import Config

class Database :

    def readAll():

        engine = create_engine(Config.getDatabase())
        with engine.connect() as con:

            data = engine.execute("SELECT * FROM Users")
            text = ""
            for row in data:
                text =text + str(row)
        return text
