select distinct name from stars as a
join people as b on a.person_id = b.id
where movie_id in (select movie_id from stars where person_id = (select id from people where name = 'Kevin Bacon' and birth = 1958))
and person_id not in (select id from people where name = 'Kevin Bacon' and birth = 1958)

