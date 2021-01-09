select title from stars as a
join movies as b on a.movie_id = b.id
where person_id in (select id from people where name in ('Johnny Depp','Helena Bonham Carter'))
group by title having count(title) = 2 order by title