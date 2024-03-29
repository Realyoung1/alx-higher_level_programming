-- listed all genre from hbtn_0d_tvshows and displays the 
-- numbers of shows linked to eachother







SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows FROM tv_show_genres INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id GROUP BY tv_genres.name ORDER BY COUNT(tv_show_genres.show_id) DESC;
