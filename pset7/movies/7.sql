select title, rating from ratings as a
join movies as b
on a.movie_id = b.id where b.year = 2010
order by rating desc, title asc