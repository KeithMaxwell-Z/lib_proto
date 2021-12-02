DROP TABLE IF EXISTS temp_books_info;

CREATE TEMPORARY TABLE temp_books_info (LIKE books_information);

COPY temp_books_info (isbn, title, author_first_name, author_last_name, publish_date, current_status)
    FROM 'D:\Programming\Python\INST123\book_info.csv'
    WITH (FORMAT CSV, HEADER);

SELECT * FROM temp_books_info;

INSERT INTO books_information
  SELECT isbn, title, author_first_name, author_last_name, publish_date, current_status, false
    FROM temp_books_info;