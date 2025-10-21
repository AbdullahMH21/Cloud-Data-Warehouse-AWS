# README

## Project Overview
This project implements an ETL (Extract, Transform, Load) pipeline for Amazon Redshift. The goal is to move raw data stored in Amazon S3 into Redshift tables for data analysis and reporting.

The ETL process is automated through a Python script (`etl.py`) that connects to Redshift, loads data from S3, transforms it as needed, and inserts it into the appropriate tables.

---

## ETL Workflow

### 1. Extract
Data is read from Amazon S3 where raw log and song data are stored. The data is typically in JSON or CSV format.

### 2. Transform
The data is processed in Python to ensure consistency and correctness before loading into Redshift. Transformations include cleaning, filtering, and mapping columns to match the schema.

### 3. Load
The processed data is loaded into Redshift tables using the `COPY` command for bulk loading and `INSERT` statements for staging or analytics tables.

Each table has its own `COPY` command. A single command can load multiple files stored in the same S3 directory.

---

## Configuration (dwh.cfg)

The ETL script uses a configuration file named `dwh.cfg` to store connection information and S3 paths. 
This file **must not be uploaded to GitHub**, as it contains sensitive credentials.

Below is the example structure of the file:

```ini
[CLUSTER]
HOST=your-redshift-cluster.us-west-2.redshift.amazonaws.com
DB_NAME=dev
DB_USER=awsuser
DB_PASSWORD=YOUR_PASSWORD_HERE
DB_PORT=5439

[IAM_ROLE]
ARN=arn:aws:iam::123456789012:role/MyRedshiftRole

[S3]
LOG_DATA=s3://your-bucket/log_data
LOG_JSONPATH=s3://your-bucket/log_json_path.json
SONG_DATA=s3://your-bucket/song_data
```

Notes:
- Replace `YOUR_PASSWORD_HERE` with your actual Redshift password (keep it local).
- The `ARN` should match your IAM role with S3 read permissions.
- Ensure that the S3 bucket paths are correct and accessible by Redshift.

---

## Project Structure
```
├── create_tables.py     # Creates all necessary tables in Redshift
├── etl.py               # Main ETL script that runs the data pipeline
├── sql_queries.py       # Contains all SQL statements used in the ETL process
├── dwh.cfg              # Configuration file (contains Redshift and S3 credentials)
└── README.txt           # Project documentation
```

---

## Running the Project

### Prerequisites
- Python 3.x installed
- Access to an Amazon Redshift cluster
- IAM Role with S3 read permissions
- Required Python packages: psycopg2, configparser

### Steps
1. Update your `dwh.cfg` file with the correct Redshift cluster, database, user, password, and S3 paths.
2. Run `create_tables.py` to create all tables in Redshift:
   ```bash
   python create_tables.py
   ```
3. Run `etl.py` to start the ETL process:
   ```bash
   python etl.py
   ```

---

## Example Redshift Table
```sql
CREATE TABLE staging_events (
    event_id      INT IDENTITY(0,1),
    artist        VARCHAR,
    auth          VARCHAR,
    firstName     VARCHAR,
    gender        VARCHAR,
    itemInSession INT,
    lastName      VARCHAR,
    length        FLOAT,
    level         VARCHAR,
    location      VARCHAR,
    method        VARCHAR,
    page          VARCHAR,
    registration  FLOAT,
    sessionId     INT,
    song          VARCHAR,
    status        INT,
    ts            BIGINT,
    userAgent     VARCHAR,
    userId        INT
);
```

---

## Notes
- Each `COPY` command loads data for one table.
- You can include multiple files in the same `COPY` load path.
- Make sure your Redshift cluster is running and accessible before executing the script.
- Data types in Redshift tables must match the input data formats to avoid type mismatches.

---

## Conclusion
This ETL project provides a reliable and scalable way to transfer and organize data from S3 into Redshift. Once loaded, the data can be used for analytical queries, dashboards, and reporting.# Cloud-Data-Warehouse-AWS
