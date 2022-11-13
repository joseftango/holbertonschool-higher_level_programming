-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT name FROM tv_genres
INNER JOIN tv_shows ON tv_shows.id = 
