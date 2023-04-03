PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Tasks;

CREATE TABLE Tasks (
    taskID      INTEGER PRIMARY KEY AUTOINCREMENT,
    listID      INTEGER, 
    username    TEXT,      
    taskName    TEXT NOT NULL,
    description TEXT,
    dueDate     TEXT NOT NULL,     -- YYYY-MM-DD
    isCompleted INTEGER NOT NULL,
    priority    TEXT,

    FOREIGN KEY(listID) REFERENCES TaskLists(listID)
    FOREIGN KEY(username) REFERENCES Users(username)
);

INSERT INTO Tasks (taskName, username, listID, description, dueDate, isCompleted, priority) VALUES
('wash the dishes', 'test_user', 1, NULL,'2023-04-21', TRUE, 'high'),
('do the laundry', 'test_user', 1, NULL,'2023-04-19', TRUE, NULL),
('mow the lawn', 'test_user', 1, 'cut all the grass in the front yard with my lawn mower', '2023-04-20', TRUE, NULL),
('Buy groceries', 'test_user', 1, 'Milk, eggs, bread, and cheese', '2023-04-05', 0, 'high'),
('Pay rent', 'test_user',  1, 'Monthly rent payment for apartment', '2023-04-10', 0, 'high'),
('Finish report', 'test_user', 1, 'Complete project report and submit to supervisor', '2023-04-15', 0, 'medium'),
('Plan vacation', 'test_user', 2, 'Research and book flights, accommodations, and activities for upcoming vacation', '2023-05-01', 0, 'low'),
('Call mom', 'test_user', 2, 'Check in and catch up with mom', '2023-04-07', 0, 'medium');
