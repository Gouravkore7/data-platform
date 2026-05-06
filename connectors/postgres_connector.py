from sqlalchemy import create_engine
import pandas as pd

class PostgresConnector:

    def __init__(self, connection_string):

        self.engine = create_engine(connection_string)

    def write(self, df, table_name):

        df.to_sql(
            table_name,
            self.engine,
            if_exists="append",
            index=False
        )

    def read(self, query):

        return pd.read_sql(query, self.engine)