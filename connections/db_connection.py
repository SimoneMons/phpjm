from sqlalchemy import create_engine


class DbConnection:
    # server_name = '192.168.64.46'
    server_name = 'S2K22BI01\SEITT_DB'
    db_name = 'seitt_ctr_bi'
    user = '$2b$12$ZQ.jRE/S0QkvobjgEnXnm.yE7PELxMBa/R8CD3xFtW0GPX6BsdFAi'
    password = '$2b$12$NzcKX3fkmUxAdSuhZ0tmjuUte1hPIXKaiojoPM8fRRBzwjBGDC5Xe'

    def __init__(self):
        print('Inside init connection')

    def conn(self):
        '''
        engine = create_engine(
            "mssql+pyodbc://" + self.user + ":" + self.password + "@" + self.server_name + "/" + self.db_name + \
            "?driver=SQL+Server")
        '''

        # engine = create_engine('mssql://*S2K22BI01\SEITT_DB*/*seitt_ctr_bi*?trusted_connection=yes')

        # engine = create_engine('mssql://*S2K22BI01\SEITT_DB*\\SQLEXPRESS/*seitt_ctr_bi*?trusted_connection=yes')

        engine = create_engine(
            'mssql+pyodbc://' + self.server_name + '/' + self.db_name + '?trusted_connection=yes&driver=ODBC Driver '
                                                                        '17 for SQL Server')

        print('Conectado a la base de datos')

        return engine

# connect = DbConnection()

# connect.conn()
