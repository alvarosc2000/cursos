-- Pregunta 1
-- ¿Quien es el actor o actriz que ha participado en la mayor cantidad de series?
SELECT actor_id, COUNT(DISTINCT serie_id) AS numero
FROM actuaciones
GROUP BY actor_id
ORDER BY numero DESC


-- Pregunta 2
-- ¿Cual es la serie con mejor rating promedio segun imdb?
SELECT serie_id, AVG(rating_imdb) AS media
FROM episodios
GROUP BY serie_id
ORDER BY media DESC
LIMIT 1;


-- Pregunta 3
-- ¿Cual es el episodio con la duración más larga?
select titulo, duracion as duracion 
from episodios
order by duracion DESC
limit 1


-- Pregunta 4
-- Todos los años de lanzamiento y los ordene
select distinct año_lanzamiento 
from series
order by año_lanzamiento desc

-- Pregunta 5
-- Selecciona los nombres de los 5 primeros actores
select nombre from actores
limit 5


-- Pregunta 6
-- Todos los registros de la tabla series cuyo genero sea igual a comedia
select * from series
where genero = 'Comedia'


-- Pregunta 7
-- Selecciona titulo, año lanzamiento de las series cuyo año de lanzamiento sea mayor que 2020
select titulo, año_lanzamiento 
from series
where año_lanzamiento > '2020'

-- Pregunta 8
-- Seleccione todas las columnas de 
-- todas las series en la tabla Series, donde el género sea 'Drama' o 'Ciencia ficción'
select * from series
where genero = 'Drama' or genero = 'Ciencia ficción'

-- Pregunta 9
-- Seleccione el año de lanzamiento de las series en la tabla Series , 
-- y cuenta el número de series lanzadas en cada año
select año_lanzamiento, count(serie_id) as cantidad_de_series
from series
group by año_lanzamiento


-- Pregunta 10
-- Seleccione solo la columna titulo de la tabla Series
-- y solo las series que posean la palabra 'The' en su titulo.
select titulo from series
where titulo like '%The%'


-- Pregunta 11
-- Duracion total de todos los episodios de la tabla Episodios
select sum(duracion) from episodios

-- Pregunta 12
-- Sumar duracion de la serie 2 y la suma > 400
select temporada, sum(duracion) as duracion_total
from episodios
where serie_id = '2'
group by temporada
having sum(duracion) > 400


-- Pregunta 13
-- Seleccione todos los campos de las tablas series y episodios
-- donde coincida el serie_id
select * from series join episodios
on series.serie_id = episodios.serie_id

-- Pregunta 14
-- Obtener el titulo de la serie, titulo de cada episodio y su duracion de la serie
-- Stranger Things
select series.titulo as titulo_serie, 
episodios.titulo as titulo_episodio,
duracion
from series
join episodios
on series.serie_id = episodios.serie_id
where series.titulo = 'Stranger Things'


-- Pregunta 15
-- Para cada serie, su titulo, titulo de episodio y ratings de imdb
select series.titulo as Título_de_la_Serie, 
episodios.titulo as Título_del_Episodio, 
episodios.rating_imdb as Rating_IMDB
from series
left join episodios
on series.serie_id = episodios.serie_id
order by series.titulo asc

-- Pregunta 16
-- Para cada serie, su titulo, titulo de episodio y ratings de imdb
-- de la serie de Stranger Things
select series.titulo as titulo_serie,
episodios.titulo as titulo_episodio,
episodios.rating_imdb as rating
from series
right join episodios
on series.serie_id = episodios.serie_id
where series.titulo = 'Stranger Things'
order by episodios.rating_imdb desc

-- Pregunta 17
-- Genere una lista de titulo de cada serie, junto con el titulo y duracion de sus episodios
-- duracion > 30, ordenados alfabeticamente
select series.titulo as titulo_serie,
episodios.titulo as titulo_episodio,
episodios.duracion as duracion_episodio
from episodios
right join series
on series.serie_id = episodios.serie_id
where episodios.duracion > 30
order by series.titulo asc


-- Pregunta 18
-- Todas las filas y columnas de la tabla Series que pertenezcan a
-- los géneros 'Ciencia ficción' y 'Drama'

SELECT * FROM Series
WHERE genero = 'Ciencia ficción'
 
UNION ALL
 
SELECT * FROM Series
WHERE genero = 'Drama'


-- Pregunta 19
-- Distintos generos y la cantidad de series de cada uno
select genero, count(*) as cantidad_series
from series
group by genero
order by cantidad_series desc


-- Pregunta 20
-- 3 series con mayor rating imbd y cuantos episodios
-- joun para unir info de series y episodios

select series.titulo, count(episodios.episodio_id)
as numero_de_episodio,
avg(episodios.rating_imdb) as promedio_imdb
from series
inner join episodios
on series.serie_id = episodios.serie_id
group by series.serie_id
order by promedio_imdb desc
limit 3


-- Pregunta 21
-- Duracion total de los episodios de la serie Stranger Things
select series.titulo as titulo_serie,
count(episodios.serie_id) as episodios_serie
from series
inner join episodios
on series.serie_id = episodios.serie_id
where series.titulo = 'Stranger Things'
group by series.titulo


-- Pregunta 22
-- Todos los episodios de The Office
select * from episodios
where serie_id = (
	select serie_id from series
	where titulo = 'The Office'
)

-- Pregunta 23
-- Lista de titulo de series cuyos episodios en
-- promedio tienen un rating de IMDb mayor a 8.
select titulo from series
where serie_id in (
	select serie_id from episodios
	where rating_imdb > 8
)

-- Pregunta 24
-- Seleccione el titulo de todas las series de la tabla 
-- Series junto con una nueva columna denominada 'Antigüedad'.
-- Esta columna debe mostrar 'Antigua' para las series lanzadas
-- antes del año 2010 y 'Reciente' para las series 
-- lanzadas en 2010 o después, puedes utilizar el campo 
-- año_lanzamiento para realizar dicha clasificació
select titulo,
case
    when año_lanzamiento < 2010 then 'Antigua'
    else 'Reciente'
END AS "Antigüedad"
from series




-- Pregunta 25
-- Escribe una consulta SQL que seleccione el titulo de todas
-- las series y una nueva columna llamada 'Categoría de Género'
-- Esta columna debe reflejar si el género de la serie es 'Drama'
-- o 'Comedia', clasificándolas como 'Dramático' o 'Divertido', 
-- respectivamente.
-- Para cualquier otro género, la clasificación debe 
-- ser 'Otro'.
select titulo,
case
	when genero = 'Drama' then 'Dramático'
	when genero = 'Comedia' then 'Divertido'
	else 'Otro'
end as "Categoría de Género"
from series

-- Pregunta 26
-- Seleccionar el titulo de la serie y año de lanzamiento
SELECT TITULO, CAST(año_lanzamiento AS TEXT) as "Año de Lanzamiento"
FROM SERIES


-- Pregunta 27
-- Titulo en mayuscula
select upper(titulo) as titulo_mayusculas
from series

-- Pregunta 28
-- Los 5 primeros caracteres de una cadena
select substr(titulo, 1, 5) as primeros_cinco_caracteres
from episodios


--  Pregunta 29
SELECT 
    Series.titulo AS 'Título de la Serie', 
    Series.año_lanzamiento AS 'Año de Lanzamiento', 
    Series.genero AS 'Género', 
    AVG(Episodios.rating_imdb) AS 'Rating Promedio IMDb'
FROM 
    Series
JOIN 
    Episodios ON Series.serie_id = Episodios.serie_id
WHERE 
    Series.genero IN (SELECT genero FROM (
					  SELECT genero, COUNT(*) AS cantidad_de_series
					  FROM Series 
					  GROUP BY genero 
                      ORDER BY cantidad_de_series DESC
                      LIMIT 3) AS top3)
GROUP BY 
    Series.serie_id
ORDER BY 
    `Rating Promedio IMDb` DESC;