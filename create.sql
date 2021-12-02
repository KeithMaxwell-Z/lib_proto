CREATE TABLE books_information(
	isbn bigint,
	title varchar(255),
	author_first_name varchar(255),
	author_last_name varchar(255),
	publish_date varchar(12),
	current_status varchar(255) DEFAULT 'Good',
	borrowed bool DEFAULT NULL,
	CONSTRAINT bookpk PRIMARY KEY (isbn)
);

CREATE TABLE members_information(
    member_id serial,
	member_first_name varchar(30),
	member_last_name varchar(30),
	dob date,
	address varchar(255),
	rank int,
    CONSTRAINT memberpk PRIMARY KEY (member_id)
);

-- Removed the borrower's name columns
-- Changed some name of columns
CREATE TABLE log(
    log_id bigserial,
	book_id bigint,
	member_id int,
	operation_time date,
	keep_time varchar(30),
	CONSTRAINT logpk PRIMARY KEY (log_id),
	CONSTRAINT logbid FOREIGN KEY (book_id) REFERENCES books_information(isbn),
	CONSTRAINT logmid FOREIGN KEY (member_id) REFERENCES members_information(member_id)
);