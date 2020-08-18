# import python library
import pandas as pd
import pyodbc
import sqlalchemy

# assign a variable that contains a string of your credentials
engine = sqlalchemy.create_engine("mssql+pyodbc://qcqauser:{password}@172.16.0.5/Nivano?driver=SQL Server".format(password = 'Q3Q@Us3r@1234'))

# read in your SQL query results using pandas
dataframe = pd.read_sql("""
            select count(0) from aaheader
            """, con = engine)
# return your first five rows
dataframe.head()

#firewall on the sql servcer must allow tcp connection from specific port for the engine approach to work.
