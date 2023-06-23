PRAGMA foreign_keys = ON;

INSERT INTO users(username, fullname, email, password)
VALUES ('dokastho', 'Thomas Dokas', 'dokastho@umich.edu', 'password');

INSERT INTO topics(name, owner)
VALUES ('Education', 'dokastho');
INSERT INTO topics(name, owner)
VALUES ('Experience', 'dokastho');

INSERT INTO groups(owner, topicId, groupOrder)
VALUES ('dokastho', 1, 1);
INSERT INTO media(uuid, owner, topicId, groupId, topicOrder)
VALUES ('example.jpg', 'dokastho', 1, 1, 1);
INSERT INTO stories(text, owner, topicId, groupId, topicOrder)
VALUES ('foo bar baz', 'dokastho', 1, 1, 2);

INSERT INTO groups(owner, topicId, groupOrder)
VALUES ('dokastho', 1, 2);
INSERT INTO stories(text, owner, topicId, groupId, topicOrder)
VALUES ('first topic, second story, second group', 'dokastho', 1, 2, 1);

INSERT INTO groups(owner, topicId, groupOrder)
VALUES ('dokastho', 2, 1);
INSERT INTO stories(text, owner, topicId, groupId, topicOrder)
VALUES ('a story for the second topic.', 'dokastho', 2, 3, 1);
