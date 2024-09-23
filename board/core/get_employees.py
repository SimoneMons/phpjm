import pandas as pd
import io, time

from sqlalchemy import text
from connections.db_connection import DbConnection

table_name_employee = 'SEITT_employee1'

class get_employees:

    def __init__(self, first_name):

        self._first_name = first_name
        print('Inside init get employee class')


    def get_employees(self):
        # Database connection
        _conn = DbConnection()
        _engine = _conn.conn()

        query_employees = "select * FROM " + table_name_employee  # '2023-04-01'"

        df_employees = pd.DataFrame(_engine.connect().execute(text(query_employees)))

        return  df_employees

    def get_employees_by_name(self):
        # Database connection
        _conn = DbConnection()
        _engine = _conn.conn()

        query_employees_name = "select * FROM " + table_name_employee  + " where first_name like " + " '%" + self._first_name + "%'"

        print(query_employees_name)

        df_employees = pd.DataFrame(_engine.connect().execute(text(query_employees_name)))

        return  df_employees