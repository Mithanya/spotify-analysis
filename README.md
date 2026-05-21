# 🎵 Spotify Songs Data Analysis using Python and SQL

A beginner-friendly data analysis project that uses **Python** and **SQLite** to explore a Spotify songs dataset. This project demonstrates how to connect Python to a SQL database, load data from a CSV file, and run meaningful analytical queries.

---

## 📁 Project Structure

```
spotify-analysis/
│
├── spotify_data.csv   → Sample Spotify dataset (30 songs)
├── analysis.py        → Main Python script (runs all queries)
├── queries.sql        → All SQL queries (for reference)
└── README.md          → Project documentation (this file)
```

> **Note:** After running `analysis.py`, a `spotify.db` file will be auto-created in the same folder. This is the SQLite database file.

---

## 🛠️ Technologies Used

| Tool       | Purpose                              |
|------------|--------------------------------------|
| Python 3   | Main programming language            |
| SQLite3    | Lightweight SQL database (built-in)  |
| CSV module | Reading the dataset file             |
| SQL        | Querying and analyzing the data      |

> No external libraries needed — everything used is built into Python!

---

## 📊 Dataset Format (`spotify_data.csv`)

| Column         | Type    | Description                        |
|----------------|---------|------------------------------------|
| `song_id`      | Integer | Unique ID for each song            |
| `song_name`    | Text    | Title of the song                  |
| `artist_name`  | Text    | Name of the artist                 |
| `album_name`   | Text    | Album the song belongs to          |
| `release_year` | Integer | Year the song was released         |
| `popularity`   | Integer | Popularity score (0–100)           |
| `energy`       | Float   | Energy level of the song (0.0–1.0) |
| `danceability` | Float   | How danceable the song is (0.0–1.0)|
| `duration_ms`  | Integer | Song duration in milliseconds      |
| `genre`        | Text    | Music genre                        |

---

## 🔍 Analyses Performed

| # | Query                          | Description                                  |
|---|--------------------------------|----------------------------------------------|
| 1 | Top 10 Most Popular Songs      | Songs ranked by popularity score (desc)      |
| 2 | Most Frequent Artists          | Artists with the most songs in the dataset   |
| 3 | Average Popularity Score       | Overall average popularity across all songs  |
| 4 | Songs with Highest Energy      | Top 10 songs ranked by energy level          |
| 5 | Count of Songs per Artist      | How many songs each artist has               |
| B | Avg Popularity per Artist      | Bonus: Average popularity grouped by artist  |

---

## ▶️ How to Run

### Prerequisites
- Python 3 must be installed. Check by running:
  ```bash
  python --version
  ```

### Steps

1. **Download or clone** all project files into one folder.

2. **Open VS Code**, then open the project folder.

3. **Open the terminal** in VS Code (`Ctrl + `` ` ``).

4. **Run the script:**
   ```bash
   python analysis.py
   ```

5. **View results** — all query results will be printed to the terminal in a formatted table.

### Expected Output (example)
```
============================================================
   Spotify Songs Data Analysis
============================================================

✅ Connected to database: spotify.db
✅ Table 'spotify_songs' is ready.
✅ Loaded 30 songs into the database.

============================================================
  QUERY 1: Top 10 Most Popular Songs
============================================================
+------------------------+---------------+------------+
| Song Name              | Artist        | Popularity |
+------------------------+---------------+------------+
| Blinding Lights        | The Weeknd    | 97         |
| Shape of You           | Ed Sheeran    | 95         |
...
```

---

## 💡 How It Works (Step by Step)

1. **Connect to SQLite** — Python's built-in `sqlite3` module creates a local `.db` file.
2. **Create Table** — A `spotify_songs` table is created if it doesn't already exist.
3. **Load CSV Data** — The `csv` module reads `spotify_data.csv` and inserts each row into the database.
4. **Run Queries** — SQL `SELECT` queries are executed using the cursor object.
5. **Display Results** — A custom `print_table()` function formats and prints results.
6. **Close Connection** — The database connection is closed cleanly at the end.

---

## 📚 Key Python Concepts Used

- `sqlite3.connect()` — opens or creates a database
- `cursor.execute()` — runs a SQL command
- `cursor.fetchall()` — retrieves all rows from a query result
- `csv.DictReader()` — reads CSV rows as dictionaries
- `f-strings` — for clean string formatting

---

## 🧑‍💻 Author

**Student Project** — Created as a college assignment to demonstrate Python + SQL integration for data analysis.

---

## 📝 License

This project is for educational purposes only.
