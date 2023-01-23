-- Convert database, table and field to utf8
-- @charset: utf8mb4
-- @collate: utf8mb4_unicode_ci
ALTER TABLE hbtn_0c_0.first_table
         CONVERT TO CHARACTER SET utf8mb4
        COLLATE utf8mb4_unicode_ci;
