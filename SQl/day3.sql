select * from whreport;
-- Changing names of columns to ease out
ALTER TABLE whreport RENAME COLUMN `Overall rank` TO `rank`;
ALTER TABLE whreport RENAME COLUMN `Country or region` TO `country`;
ALTER TABLE whreport RENAME COLUMN `Score` TO `score`;
ALTER TABLE whreport RENAME COLUMN `GDP per capita` TO `GDP`;
ALTER TABLE whreport RENAME COLUMN `Social support` TO `socialsupport`;
ALTER TABLE whreport RENAME COLUMN `Healthy life expectancy` TO `healthlife`;
ALTER TABLE whreport RENAME COLUMN `Freedom to make life choices` TO `freedom`;
ALTER TABLE whreport RENAME COLUMN `Generosity` TO `generosity`;
ALTER TABLE whreport RENAME COLUMN `Perceptions of corruption` TO `corruption`;


select avg(score) from whreport;
select sum(score) from whreport;
select * from whreport;
select * from whreport  order by GDP;

-- Ordering the table wrt to names
select * from whreport order by `country`;

-- find countries with gdp less than 2 and countries whose health life is greater than 1
select * from whreport where `GDP` < 1 and `healthlife` <1;

-- find the difference between total number of countries and total unique cities in the table

select count(country) - count(distinct country) from whreport;
-- 0

select count(country) from whreport;
-- 156

select count(distinct(country)) from whreport;
-- 156

-- ordering by score in ascending order and then by country in descending order
select * from whreport order by score asc, country desc;

-- find country with the largest and smallest name and show the country and the length
(
select country,GDP,length(country) from whreport order by(length(country)) asc,country limit 1
) union(
select country,GDP,length(country) from whreport order by(length(country)) desc,country limit 1
) 



