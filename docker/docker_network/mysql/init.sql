use demodb;

CREATE TABLE user(
    user_id int serial PRIMARY KEY,
    name varchar(50) not null
);