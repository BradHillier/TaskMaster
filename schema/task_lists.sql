DROP TABLE IF EXISTS TaskLists;

CREATE TABLE TaskLists (
    listID      INTEGER PRIMARY KEY AUTOINCREMENT,
    listName    TEXT NOT NULL,
    username    TEXT NOT NULL,
    FOREIGN KEY(username) REFERENCES Users(username)
);

INSERT INTO TaskLists (listName, username) VALUES
('Chores', 'test_user'),
('Work', 'test_user'),
('Personal', 'test_user');
