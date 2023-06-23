PRAGMA foreign_keys = ON;

INSERT INTO users(username, fullname, email, password)
VALUES ('dokastho', 'Thomas Dokas', 'dokastho@umich.edu', 'password');

INSERT INTO topics(name, owner)
VALUES ('Education', 'dokastho');
INSERT INTO topics(name, owner)
VALUES ('Experience', 'dokastho');

INSERT INTO media(uuid, owner, topicId, topicOrder)
VALUES ('example.jpg', 'dokastho', 1, 1);

INSERT INTO stories(text, owner, topicId, topicOrder)
VALUES ('foo bar baz', 'dokastho', 1, 2);
INSERT INTO stories(text, owner, topicId, topicOrder)
VALUES ('first topic, second story', 'dokastho', 1, 3);

INSERT INTO stories(text, owner, topicId, topicOrder)
VALUES ('a story for the second topic.', 'dokastho', 2, 1);
