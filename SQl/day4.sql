select * from indian_food;

-- Ingredients with longest and shortest names
(
select name,length(name) from indian_food order by length(name) asc limit 1
)
union(
select name,length(name) from indian_food order by length(name) desc limit 1
);
 	

SELECT Surname
   FROM Contacts
   WHERE Surname LIKE 'Mc%';

/*
Match expression 	Description 																					Returns
'Mc%' 				Search for every name that begins with the letters Mc 											McEvoy
'%er' 				Search for every name that ends with er 														Brier, Miller, Weaver, Rayner
'%en%' 				Search for every name containing the letters en. 												Pettengill, Lencki, Cohen
'_ish' 				Search for every four-letter name ending in ish. 												Fish
'Br[iy][ae]r' 		Search for Brier, Bryer, Briar, or Bryar. 														Brier
'[M-Z]owell' 		Search for all names ending with owell that begin with a single letter in the range M to Z. 	Powell
'M[^c]%' 			Search for all names beginning with M that do not have c as the second letter 					Moore, Mulley, Miller, Masalsky

*/
-- query the list of city names  staring with vowels (a,e,i,o,u)

SELECT * FROM indian_food where left(name,1) in ('a','e','i','o','u','A','E','I','O','U');
SELECT * FROM  indian_food;
SELECT * FROM indian_food where right(state,1) in ('n');
select * from indian_food where state like 'Ut%';
select * from indian_food where state like '%hand';
SELECT * FROM indian_food where ingredients like '%Maida%';

-- what are last 5 words in ingredients
SELECT right(ingredients,5) FROM indian_food;

-- rows where the last word in ingredients is sugar
SELECT * FROM indian_food where right(ingredients,5) = 'sugar';

-- SAME THING with regex

SELECT * FROM indian_food where ingredients REGEXP '^(Maida).+(sugar)$';

select * from indian_food;

-- find ingredients where the ingredient column value starts with a vowel and ends with a vowel

SELECT * FROM indian_food where ingredients regexp '^[aeiou].+[aeious]$';

-- select names where the name doesnt start with a vowel
SELECT NAME FROM indian_food where NAME REGEXP '^[^aeiou]';

-- name doesnt end with a vowel
SELECT NAME FROM indian_food where NAME REGEXP '[^aeiou]$';

select * from indian_food;
select * from indian_food order by right(name,1) desc,prep_time limit 10;

SELECT * FROM indian_food;


(SELECT NAME,LENGTH(NAME) FROM INDIAN_FOOD ORDER BY LENGTH(NAME),PREP_TIME LIMIT 1)
UNION(
SELECT NAME,LENGTH(NAME) FROM INDIAN_FOOD ORDER BY LENGTH(NAME) DESC,PREP_TIME LIMIT 1
);

-- ROUNDING UP VALUES TO 3 DECIMAL POINTS
SELECT * FROM WHREPORT;
SELECT TRUNCATE(SUM(SCORE),3) FROM WHREPORT;

SELECT * FROM indian_food;

SELECT 
CASE
WHEN prep_time < cook_time then 'Good time'
WHEN prep_time = cook_time then 'Average time'
when prep_time > cook_time then 'bad time'
end
from indian_food;

SELECT * FROM INDIAN_FOOD;



