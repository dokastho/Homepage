PRAGMA foreign_keys = ON;

INSERT INTO users(username, fullname, email, password)
VALUES ('dokastho', 'Thomas Dokas', 'dokastho@umich.edu', 'password');

INSERT INTO topics(name, owner)
VALUES ('Education', 'dokastho');
INSERT INTO topics(name, owner)
VALUES ('Experience', 'dokastho');
