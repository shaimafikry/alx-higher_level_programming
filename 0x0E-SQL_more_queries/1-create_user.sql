-- script that creates the MySQL server user user_0d_1.

CREATE USER IF NOT EXISTS "user_0d_1" IDENTIFIED BY "user_0d_1_pwd";
GRANT ALL PRIVILAGES
ON *.*
TO user_0d_1;
