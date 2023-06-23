PRAGMA foreign_keys = ON;

INSERT INTO users(username, fullname, email, password)
VALUES ('dokastho', 'Thomas Dokas', 'dokastho@umich.edu', 'password');

INSERT INTO topics(name, owner)
VALUES ('Education', 'dokastho');
INSERT INTO topics(name, owner)
VALUES ('Experience', 'dokastho');

INSERT INTO media(uuid, owner, topicId)
VALUES ('example.jpg', 'dokastho', 1);

INSERT INTO stories(text, owner, topicId)
VALUES ('foo bar baz', 'dokastho', 1);
INSERT INTO stories(text, owner, topicId)
VALUES ('SEOND STORY', 'dokastho', 1);

INSERT INTO stories(text, owner, topicId)
VALUES ('a story for the second topic.', 'dokastho', 2);
