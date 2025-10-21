import configparser
import psycopg2

config = configparser.ConfigParser()
config.read('dwh.cfg')

conn = psycopg2.connect(
    "host={} dbname={} user={} password={} port={}".format(
        *config['CLUSTER'].values()
    )
)
cur = conn.cursor()

# Count records in each table
tables = ['staging_events', 'staging_songs', 'songplays', 'users', 'songs', 'artists', 'time']

for table in tables:
    cur.execute(f"SELECT COUNT(*) FROM {table}")
    count = cur.fetchone()[0]
    print(f"{table}: {count} rows")

conn.close()