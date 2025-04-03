from time import time
import pandas as pd
from sqlalchemy import create_engine
import pyarrow.parquet as pq
import argparse
import os

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    parquet_file_name = "yellow_tripdata_2025-01.parquet"

    os.system(f"wget {url} -O {parquet_file_name}")
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    parquet_file = pq.ParquetFile(parquet_file_name)

    for i in range(parquet_file.num_row_groups):
        table = parquet_file.read_row_group(i)
        df_chunk = table.to_pandas()
        df_chunk.to_sql(name=table_name,con=engine, if_exists="append")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")

    parser.add_argument('user', help='user name for postgres')
    parser.add_argument('password', help='user password for postgres')
    parser.add_argument('host', help='host for postgres')
    parser.add_argument('port', help='port for postgres')
    parser.add_argument('db', help='database for postgres')
    parser.add_argument('table_name', help='table_name for postgres')
    parser.add_argument('url', help='url for csv file')

    args = parser.parse_args()
    # print(args.accumulate(args.integers))
    main(args)

