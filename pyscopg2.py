import pandas as pd
from sqlalchemy import create_engine

# Database credentials
user = "postgres"
password = "Admin"
host = "localhost"
port = "5432"
database = "MyDatabase"

# Create the database connection string
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

# Load data from the 'customers' table into a pandas DataFrame
df = pd.read_sql('SELECT * FROM customers;', engine)

# Display the DataFrame
print(df)