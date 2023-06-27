PRAGMA foreign_keys = ON;

INSERT INTO users(username, fullname, email, password)
VALUES ('dokastho', 'Thomas Dokas', 'dokastho@umich.edu', 'password');

INSERT INTO topics(name, owner, styles)
VALUES ('About Me', 'dokastho', '{"primary": "white", "alt": "#1f4954", "trim": "black", "text": "white"}');
INSERT INTO topics(name, owner, styles)
VALUES ('Education', 'dokastho', '{"primary": "#00326a", "alt": "#ffcb0b", "trim": "white", "text": "black"}');
INSERT INTO topics(name, owner, styles)
VALUES ('Experience', 'dokastho', '{"primary": "#00095b", "alt": "white", "trim": "gray", "text": "black"}');

INSERT INTO groups(owner, topicId, groupOrder)
VALUES ('dokastho', 1, 1);
INSERT INTO stories(text, owner, topicId, groupId, topicOrder)
VALUES ('I love everything about networking, distributed systems and operating systems!', 'dokastho', 1, 1, 1);

INSERT INTO groups(owner, topicId, groupOrder)
VALUES ('dokastho', 2, 1);
INSERT INTO media(uuid, owner, topicId, groupId, topicOrder)
VALUES ('example.jpg', 'dokastho', 2, 2, 1);
INSERT INTO stories(text, owner, topicId, groupId, topicOrder)
VALUES ('foo bar baz', 'dokastho', 2, 2, 2);

INSERT INTO groups(owner, topicId, groupOrder)
VALUES ('dokastho', 2, 2);
INSERT INTO stories(text, owner, topicId, groupId, topicOrder)
VALUES ('first topic, second story, second group', 'dokastho', 2, 3, 1);

INSERT INTO groups(owner, topicId, groupOrder)
VALUES ('dokastho', 3, 1);
INSERT INTO stories(text, owner, topicId, groupId, topicOrder)
VALUES ('a story for the second topic.', 'dokastho', 3, 4, 1);
