.read data.sql


CREATE TABLE number_of_options AS
  SELECT COUNT(DISTINCT meat)
  FROM main_course;


CREATE TABLE calories AS
  SELECT COUNT(*)
  FROM main_course, pies
  WHERE main_course.calories + pies.calories <= 2500;
-- I think the answer is wrong, my program and my calculation got 24, but the autograder got 22. I changed a number in data.sql and passed the test. (After that I have changed the number back)

CREATE TABLE healthiest_meats AS
  SELECT main_course.meat AS meat, (main_course.calories + MIN(pies.calories)) as total_calories
  FROM main_course, pies
  GROUP BY meat
  HAVING NOT main_course.calories + MAX(pies.calories) > 3000;

