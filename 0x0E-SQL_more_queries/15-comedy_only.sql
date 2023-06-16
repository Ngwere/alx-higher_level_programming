-- Import the database dump from hbtn_0d_tvshows to your MySQL serve
   -- lists all Comedy shows in the database hbtn_0d_tvshows.
   -- Display number of shows linked to each
      -- Record
      -- tv_shows.title
   -- Result sorted in ascending order by show title
   -- The database name will be passed as an argument of the mysql command

SELECT title FROM tv_shows
JOIN tv_show_genres ON id=tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;
