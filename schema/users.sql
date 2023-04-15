DROP TABLE IF EXISTS Users;

CREATE TABLE Users (
    username    TEXT PRIMARY KEY,
    password    TEXT NOT NULL,               -- hashed using sha512 (64 bytes)
    email       TEXT NOT NULL
);

INSERT INTO Users VALUES ('test_user', '123', 'user@example.com');
INSERT INTO Users VALUES ('admin', 'password', 'admin@example.com');

