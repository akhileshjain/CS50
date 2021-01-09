select b.name from artists as a
join songs as b on a.id = b.artist_id
where a.name = 'Post Malone';