DROP TABLE Users;

CREATE TABLE Users (
    username    TEXT PRIMARY KEY,
    password    TEXT,               -- hashed using sha512 (64 bytes)
    email       TEXT
);

