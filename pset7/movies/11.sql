select title from people as a
join stars as b on a.id = b.person_id
join ratings as c on c.movie_id = b.movie_id
join movies as d on d.id = c.movie_id
where name = 'Chadwick Boseman' order by rating desc limit 5