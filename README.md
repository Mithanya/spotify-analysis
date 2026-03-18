# Spotify Songs Data Analysis using Python and MySQL

A data analysis project demonstrating how Python and MySQL work together to manage and analyze structured data from a Spotify songs dataset.

## Overview
This project loads song data from a CSV file into a MySQL database and performs analysis using SQL queries. Python is used to execute queries and display results in a structured format.

## Project Structure
spotify-analysis/
- spotify_data.csv
- analysis.py
- queries.sql
- README.md

## Technologies Used
- Python 3.10: Core programming language  
- MySQL: Database for storing and querying data  
- MySQL Workbench: Database management tool  
- Visual Studio Code: Development environment  
- CSV: Source dataset  

## Features
- Load CSV data into MySQL database  
- Perform CRUD operations (Add, Update, Delete, View)  
- Search songs by name, artist, or genre  
- Execute analytical SQL queries  
- Display formatted output in terminal  

## Key Analysis
- Top 10 most popular songs  
- Most frequent artists  
- Average popularity score  
- Songs with highest energy  
- Grouping and aggregation by artist  

## How to Run
1. Create database in MySQL:
   CREATE DATABASE spotify_db;

2. Update MySQL credentials in analysis.py:
   host="localhost"
   user="root"
   password="your_password"

3. Run the script:
   python analysis.py

## Output
- Creates and manages a MySQL table  
- Loads dataset into database  
- Performs queries and analysis  
- Displays results in structured tables  

## Key Concepts
- SQL: SELECT, WHERE, ORDER BY, GROUP BY, COUNT, AVG  
- Python: mysql.connector, csv, database operations  

## Author
Mithanya Murugesan  
Aspiring Software Developer focused on Python and Full Stack Development
