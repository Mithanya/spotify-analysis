import mysql.connector
import csv
import os

CSV_FILE = "spotify_data.csv"

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="spotify_db"
)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS spotify_songs (
        song_id       INT PRIMARY KEY,
        track_name    VARCHAR(200) NOT NULL,
        artist_name   VARCHAR(200) NOT NULL,
        album_name    VARCHAR(200),
        release_year  INT,
        popularity    INT,
        energy        FLOAT,
        danceability  FLOAT,
        duration_ms   INT,
        genre         VARCHAR(100)
    )
""")
connection.commit()

cursor.execute("SELECT COUNT(*) FROM spotify_songs")
if cursor.fetchone()[0] == 0:
    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT INTO spotify_songs
                    (song_id, track_name, artist_name, album_name,
                     release_year, popularity, energy, danceability,
                     duration_ms, genre)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                int(row["song_id"]), row["song_name"], row["artist_name"],
                row["album_name"], int(row["release_year"]), int(row["popularity"]),
                float(row["energy"]), float(row["danceability"]),
                int(row["duration_ms"]), row["genre"]
            ))
    connection.commit()


def print_table(headers, rows):
    if not rows:
        print("  No records found.\n")
        return

    col_widths = [len(str(h)) for h in headers]

    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    separator = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

    print(separator)
    print("|" + "|".join(f" {str(h).ljust(col_widths[i])} " for i, h in enumerate(headers)) + "|")
    print(separator)

    for row in rows:
        print("|" + "|".join(f" {str(c).ljust(col_widths[i])} " for i, c in enumerate(row)) + "|")

    print(separator)


def view_all_songs():
    print("\nALL SONGS IN DATABASE")

    cursor.execute("""
        SELECT song_id, track_name, artist_name, popularity, genre
        FROM spotify_songs
        ORDER BY song_id
    """)

    print_table(
        ["ID", "Track Name", "Artist", "Popularity", "Genre"],
        cursor.fetchall()
    )


def add_song():
    print("\nADD A NEW SONG")

    try:
        song_id = int(input("   Enter Song ID            : "))
        track_name = input("   Enter Track Name         : ")
        artist_name = input("   Enter Artist Name        : ")
        album_name = input("   Enter Album Name         : ")
        release_year = int(input("   Enter Release Year       : "))
        popularity = int(input("   Enter Popularity (0-100) : "))
        energy = float(input("   Enter Energy (0.0-1.0)   : "))
        danceability = float(input("   Enter Danceability (0.0-1.0): "))
        duration_ms = int(input("   Enter Duration (ms)      : "))
        genre = input("   Enter Genre              : ")

        cursor.execute("""
            INSERT INTO spotify_songs
                (song_id, track_name, artist_name, album_name,
                 release_year, popularity, energy, danceability,
                 duration_ms, genre)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            song_id, track_name, artist_name, album_name,
            release_year, popularity, energy,
            danceability, duration_ms, genre
        ))

        connection.commit()

        print(f"\nSong '{track_name}' added successfully!")

    except Exception as e:
        print(f"\nError: {e}")


def update_song():
    print("\nUPDATE A SONG")

    view_all_songs()

    try:
        song_id = int(input("\n   Enter Song ID to update: "))

        print("   What do you want to update?")
        print("   1. Track Name")
        print("   2. Artist Name")
        print("   3. Popularity")
        print("   4. Genre")
        print("   5. Energy")

        choice = input("   Enter choice (1-5): ")

        fields = {
            "1": ("track_name", "New Track Name   : ", str),
            "2": ("artist_name", "New Artist Name  : ", str),
            "3": ("popularity", "New Popularity   : ", int),
            "4": ("genre", "New Genre        : ", str),
            "5": ("energy", "New Energy       : ", float),
        }

        if choice in fields:
            col, prompt, cast = fields[choice]

            new_value = cast(input(f"   Enter {prompt}"))

            cursor.execute(
                f"UPDATE spotify_songs SET {col} = %s WHERE song_id = %s",
                (new_value, song_id)
            )

            connection.commit()

            if cursor.rowcount > 0:
                print(f"\nSong ID {song_id} updated successfully!")
            else:
                print(f"\nNo song found with ID {song_id}.")

        else:
            print("Invalid choice.")

    except Exception as e:
        print(f"\nError: {e}")


def delete_song():
    print("\nDELETE A SONG")

    view_all_songs()

    try:
        song_id = int(input("\n   Enter Song ID to delete: "))

        cursor.execute(
            "SELECT track_name FROM spotify_songs WHERE song_id = %s",
            (song_id,)
        )

        result = cursor.fetchone()

        if result:
            confirm = input(
                f"   Are you sure you want to delete '{result[0]}'? (yes/no): "
            )

            if confirm.lower() == "yes":
                cursor.execute(
                    "DELETE FROM spotify_songs WHERE song_id = %s",
                    (song_id,)
                )

                connection.commit()

                print(f"\nSong '{result[0]}' deleted successfully!")

            else:
                print("Delete cancelled.")

        else:
            print(f"No song found with ID {song_id}.")

    except Exception as e:
        print(f"\nError: {e}")


def search_song():
    print("\nSEARCH SONGS")

    print("   1. Search by Track Name")
    print("   2. Search by Artist Name")
    print("   3. Search by Genre")

    choice = input("   Enter choice (1-3): ")

    try:
        if choice == "1":
            keyword = input("   Enter track name to search: ")

            cursor.execute("""
                SELECT song_id, track_name, artist_name, popularity, genre
                FROM spotify_songs
                WHERE track_name LIKE %s
            """, (f"%{keyword}%",))

        elif choice == "2":
            keyword = input("   Enter artist name to search: ")

            cursor.execute("""
                SELECT song_id, track_name, artist_name, popularity, genre
                FROM spotify_songs
                WHERE artist_name LIKE %s
            """, (f"%{keyword}%",))

        elif choice == "3":
            keyword = input("   Enter genre to search: ")

            cursor.execute("""
                SELECT song_id, track_name, artist_name, popularity, genre
                FROM spotify_songs
                WHERE genre LIKE %s
            """, (f"%{keyword}%",))

        else:
            print("Invalid choice.")
            return

        print_table(
            ["ID", "Track Name", "Artist", "Popularity", "Genre"],
            cursor.fetchall()
        )

    except Exception as e:
        print(f"\nError: {e}")


def run_analysis():
    print("\nQUERY 1: Top 10 Most Popular Songs")

    cursor.execute("""
        SELECT track_name, artist_name, popularity
        FROM spotify_songs
        ORDER BY popularity DESC
        LIMIT 10
    """)

    print_table(
        ["Track Name", "Artist", "Popularity"],
        cursor.fetchall()
    )

    print("\nQUERY 2: Most Frequent Artists")

    cursor.execute("""
        SELECT artist_name, COUNT(*) AS song_count
        FROM spotify_songs
        GROUP BY artist_name
        ORDER BY song_count DESC
        LIMIT 10
    """)

    print_table(
        ["Artist Name", "Song Count"],
        cursor.fetchall()
    )

    print("\nQUERY 3: Average Popularity Score")

    cursor.execute("SELECT ROUND(AVG(popularity), 2) FROM spotify_songs")

    print(f"\nAverage popularity score: {cursor.fetchone()[0]}\n")

    print("QUERY 4: Top 10 Songs with Highest Energy")

    cursor.execute("""
        SELECT track_name, artist_name, energy
        FROM spotify_songs
        ORDER BY energy DESC
        LIMIT 10
    """)

    print_table(
        ["Track Name", "Artist", "Energy"],
        cursor.fetchall()
    )

    print("\nQUERY 5: Count of Songs per Artist")

    cursor.execute("""
        SELECT artist_name, COUNT(*) AS total_songs
        FROM spotify_songs
        GROUP BY artist_name
        ORDER BY total_songs DESC
    """)

    print_table(
        ["Artist Name", "Total Songs"],
        cursor.fetchall()
    )

    print("\nBONUS: Average Popularity per Artist")

    cursor.execute("""
        SELECT artist_name,
               ROUND(AVG(popularity), 2),
               COUNT(*)
        FROM spotify_songs
        GROUP BY artist_name
        ORDER BY AVG(popularity) DESC
    """)

    print_table(
        ["Artist Name", "Avg Popularity", "Songs"],
        cursor.fetchall()
    )


while True:
    print("\nSPOTIFY SONGS MANAGEMENT SYSTEM")
    print("  1. View All Songs")
    print("  2. Add New Song")
    print("  3. Update Song")
    print("  4. Delete Song")
    print("  5. Search Song")
    print("  6. Run Full Analysis")
    print("  7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        view_all_songs()

    elif choice == "2":
        add_song()

    elif choice == "3":
        update_song()

    elif choice == "4":
        delete_song()

    elif choice == "5":
        search_song()

    elif choice == "6":
        run_analysis()

    elif choice == "7":
        print("\nGoodbye! Database connection closed.\n")
        break

    else:
        print("\nInvalid choice. Please enter 1 to 7.")

cursor.close()
connection.close()