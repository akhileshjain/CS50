select distinct name from movies as a
join ratings as b on a.id = b.movie_id
join directors as c on c.movie_id = a.id
join people as d on d.id = c.person_id
where rating >= 9.0
