select name from movies as a
join stars as b on a.id = b.movie_id
join people as c on c.id = b.person_id where a.title = 'Toy Story'