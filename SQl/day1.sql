SELECT * FROM indian_food;
SELECT name from indian_food;

## changing name of flavor_profile to flavour
ALTER TABLE indian_food RENAME COLUMN flavor_profile TO flavor;
SELECT * FROM INDIAN_FOOD;

#food where cooking time is greater than 40
SELECT * FROM indian_food where cook_time >40;

#foods where cooking time is in between 10 and 40
SELECT * FROM indian_food WHERE cook_time BETWEEN 10 and 40;

#Foods where the name starts with 'Ba'
SELECT * FROM indian_food where name like 'Ba%';

#foods where name ended with 'i'
SELECT * FROM indian_food where name like '%i';

#food with prep_time of 10 , 20 and 30
SELECT * FROM indian_food WHERE prep_time in (10,20,30);

#  Unique state names in the table
SELECT DISTINCT(state) from indian_food;

#Aggregation
#Finding average cook_time
SELECT avg(cook_time) FROM indian_food;

#counting total states with repetition in indian_food
SELECT COUNT(STATE) FROM indian_food;

#counting unique states in indian_food
SELECT COUNT(DISTINCT(state)) FROM indian_food;

#minimum preparation time of the food in indian_food
SELECT MIN(prep_time) from indian_food;

#maximum preparation_time of the food in indian_food
SELECT MAX(prep_time) from indian_food;

#SELECT * FROM indian_food WHERE prep_time = MAX(prep_time); --- Not working
SELECT * FROM indian_food WHERE prep_time = 500;

#Grouping by department id
SELECT max(cook_time),region FROM indian_food GROUP BY region;
SELECT min(cook_time),region FROM indian_food GROUP BY region;
SELECT avg(cook_time),region FROM indian_food GROUP BY region;
SELECT sum(cook_time),region FROM indian_food GROUP BY region;

#having
SELECT * FROM indian_food GROUP BY course HAVING prep_time between 10 and 50;
SELECT avg(cook_time),region,course FROM indian_food GROUP BY course;

# ORDER BY
SELECT * FROM indian_food ORDER BY cook_time;

#Union
SELECT * FROM indian_food WHERE region='East' UNION SELECT*FROM indian_food where region='West';

