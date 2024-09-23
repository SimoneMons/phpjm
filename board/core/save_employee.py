import pandas as pd
import io, time

from sqlalchemy import text
from connections.db_connection import DbConnection

table_name_employee = 'SEITT_employee1'

class save_employee:

    def __init__(self, first_name, last_name):

        self._first_name = first_name
        self._last_name = last_name
        print('Inside init save employee class')


    def save_employee(self):
        # Database connection
        _conn = DbConnection()
        _engine = _conn.conn()


        # dictionary of lists
        dict = {'first_name': self._first_name, 'last_name': self._last_name}

        df = pd.DataFrame(dict, index=[0])

        print(df)

        # Insert into last loaded date table
        df.to_sql(table_name_employee, con=_engine.connect(), if_exists='append', index=False)

