-- 1. View all songs in the table
SELECT * FROM spotify_songs;


-- 2. Sort songs by popularity in descending order (highest first)
SELECT track_name, artist_name, popularity
FROM spotify_songs
ORDER BY popularity DESC;


-- 3. Sort songs by popularity in ascending order (lowest first)
SELECT track_name, artist_name, popularity
FROM spotify_songs
ORDER BY popularity ASC;


-- 4. Top 10 most popular songs
SELECT track_name, artist_name, popularity
FROM spotify_songs
ORDER BY popularity DESC
LIMIT 10;


-- 5. Most frequent artists (who has the most songs)
SELECT artist_name, COUNT(*) AS song_count
FROM spotify_songs
GROUP BY artist_name
ORDER BY song_count DESC;


-- 6. Average popularity score of all songs
SELECT AVG(popularity) AS average_popularity
FROM spotify_songs;


-- 7. Top 10 songs with highest energy
SELECT track_name, artist_name, energy
FROM spotify_songs
ORDER BY energy DESC
LIMIT 10;


-- 8. Top 10 songs with lowest energy
SELECT track_name, artist_name, energy
FROM spotify_songs
ORDER BY energy ASC
LIMIT 10;


-- 9. Count number of songs per artist
SELECT artist_name, COUNT(*) AS total_songs
FROM spotify_songs
GROUP BY artist_name
ORDER BY total_songs DESC;


-- 10. Sort all songs alphabetically by track name
SELECT track_name, artist_name
FROM spotify_songs
ORDER BY track_name ASC;


-- 11. Songs with popularity greater than 80
SELECT track_name, artist_name, popularity
FROM spotify_songs
WHERE popularity > 80;


-- 12. Songs with popularity less than 50
SELECT track_name, artist_name, popularity
FROM spotify_songs
WHERE popularity < 50;


-- 13. Find the maximum popularity score in the table
SELECT MAX(popularity) AS highest_popularity
FROM spotify_songs;


-- 14. Find the minimum popularity score in the table
SELECT MIN(popularity) AS lowest_popularity
FROM spotify_songs;


-- 15. Count total number of songs in the table
SELECT COUNT(*) AS total_songs
FROM spotify_songs;


-- 16. Songs with high danceability (greater than 0.8)
SELECT track_name, artist_name, danceability
FROM spotify_songs
WHERE danceability > 0.8
ORDER BY danceability DESC;


-- 17. Average energy and average danceability of all songs
SELECT 
    ROUND(AVG(energy), 2) AS avg_energy,
    ROUND(AVG(danceability), 2) AS avg_danceability
FROM spotify_songs;


-- 18. Top artists based on number of songs (top 5 only)
SELECT artist_name, COUNT(*) AS song_count
FROM spotify_songs
GROUP BY artist_name
ORDER BY song_count DESC
LIMIT 5;


-- 19. Songs with both high popularity and high energy
SELECT track_name, artist_name, popularity, energy
FROM spotify_songs
WHERE popularity > 80 AND energy > 0.7
ORDER BY popularity DESC;


-- 20. Average popularity grouped by artist
SELECT artist_name,
       ROUND(AVG(popularity), 2) AS avg_popularity,
       COUNT(*) AS total_songs
FROM spotify_songs
GROUP BY artist_name
ORDER BY avg_popularity DESC;