create database countries;
create table users(
id int NOT NULL,
name varchar(255),
country_id int,
state_id int,
city_id int
);
ALTER TABLE USERS ADD PRIMARY KEY(ID);

select * from users;
insert into users values(1,'Laksha',1,11,21);
insert into users values(2,'garvit',1,11,21);
insert into users values(3,'usha',1,12,23);
insert into users values(4,'edress',2,21,35);

CREATE TABLE COUNTRIES(
ID int primary key,
C_ID int not null,
NAME VARCHAR(255),
foreign key(C_ID) REFERENCES users(country_id)
);