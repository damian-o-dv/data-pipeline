# CSV to SQL ETL Pipeline

## Description
Simple ETL pipeline that loads raw CSV data,
cleans and transforms it using Pandas,
and loads the final dataset into SQL Server.

## Technologies

- Python
- Pandas
- SQL Server
- SQLAlchemy

## Pipeline
CSV → Pandas → Cleaning → Transformation → SQL Server

## Assumptions
- Missing quantity values were treated as 0.
- Invalid price values were converted to NaN.
- Missing city values were replaced with "N/A".
- Duplicate rows were removed.
- Revenue was calculated as Quantity × Price