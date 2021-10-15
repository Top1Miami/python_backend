DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email text NOT NULL UNIQUE,
    is_demo INTEGER NOT NULL,
    launch_left INTEGER NOT NULL);

