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
('wash the dishes', 'test_user', 1, NULL,'2023-04-21', TRUE, ':red_circle:'),
('do the laundry', 'test_user', 1, NULL,'2023-04-19', TRUE, ':green_circle:'),
('mow the lawn', 'test_user', 1, 'cut all the grass in the front yard with my lawn mower', '2023-04-20', TRUE, ':green_circle:'),
('Buy groceries', 'test_user', 1, 'Milk, eggs, bread, and cheese', '2023-04-05', 0, ':red_circle:'),
('Pay rent', 'test_user',  1, 'Monthly rent payment for apartment', '2023-04-10', 0, ':red_circle:'),
('Finish report', 'test_user', 1, 'Complete project report and submit to supervisor', '2023-04-15', 0, ':yellow_circle:'),
('Attend meeting with team', 'test_user', 2, 'Discuss progress and goals for current project', '2023-04-18', 0, ':red_circle:'),
('Complete project deliverables', 'test_user', 2, 'Finish coding and testing for project', '2023-04-25', 0, ':red_circle:'),
('Schedule doctor appointment', 'test_user', 3, 'Annual check-up with family doctor', '2023-05-15', 0, ':yellow_circle:'),
('Buy birthday gift for friend', 'test_user', 3, 'Find and purchase gift for upcoming birthday', '2023-04-30', 0, ':green_circle:'),
('Research new hobby', 'test_user', 3, 'Explore options and interests for a new hobby', '2023-04-22', 0, ':yellow_circle:'),
('Fix leaky faucet', 'test_user', 3, 'Repair leaky faucet in bathroom sink', '2023-04-19', 0, ':red_circle:');
