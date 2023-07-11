PRAGMA foreign_keys = ON;

INSERT INTO users(username, fullname, email, password)
VALUES ('dokastho', 'Thomas Dokas', 'dokastho@umich.edu', 'password');

INSERT INTO topics(name, owner, styles, icon)
VALUES ('Bio', 'dokastho', '{"primary": "white", "alt": "#1f4954", "trim": "black", "text": "white", "alt-text": "#1f4954"}', 'Bio.svg');
INSERT INTO topics(name, owner, styles, icon)
VALUES ('Education', 'dokastho', '{"primary": "#ffcb0b", "alt": "#00326a", "trim": "white", "text": "#ffcb0b", "alt-text": "#00326a"}', 'Education.svg');
INSERT INTO topics(name, owner, styles, icon)
VALUES ('Projects', 'dokastho', '{"primary": "#ffcb0b", "alt": "#CF2F44", "trim": "white", "text": "powderblue", "alt-text": "#CF2F44"}', 'Projects.svg');
INSERT INTO topics(name, owner, styles, icon)
VALUES ('Experience', 'dokastho', '{"primary": "white", "alt": "#99EDC3", "trim": "gray", "text": "black", "alt-text": "black"}', 'Experience.svg');

INSERT INTO groups(owner, name, topicId, groupOrder)
VALUES ('dokastho', 'Hey There', 1, 1);
INSERT INTO stories(text, owner, topicId, groupId, storyOrder)
VALUES ('I love everything about networking, distributed systems and operating systems!', 'dokastho', 1, 1, 1);

INSERT INTO groups(owner, name, topicId, groupOrder)
VALUES ('dokastho', 'Under(graduate)', 2, 1);
INSERT INTO media(uuid, owner, topicId, groupId, storyOrder)
VALUES ('example.jpg', 'dokastho', 2, 2, 2);
INSERT INTO stories(text, owner, topicId, groupId, storyOrder)
VALUES ('foo bar baz', 'dokastho', 2, 2, 1);

INSERT INTO groups(owner, name, topicId, groupOrder)
VALUES ('dokastho', 'Placeholder Education', 2, 2);
INSERT INTO stories(text, owner, topicId, groupId, storyOrder)
VALUES ('first topic, second story, second group', 'dokastho', 2, 3, 1);

INSERT INTO groups(owner, name, topicId, groupOrder)
VALUES ('dokastho', 'Meet My Stack', 3, 1);
INSERT INTO stories(text, owner, topicId, groupId, storyOrder)
VALUES ('project 1', 'dokastho', 3, 4, 1);

INSERT INTO groups(owner, name, topicId, groupOrder)
VALUES ('dokastho', 'dRPC', 3, 2);
INSERT INTO stories(text, owner, topicId, groupId, storyOrder)
VALUES ('prokect 2', 'dokastho', 3, 5, 1);

INSERT INTO groups(owner, name, topicId, groupOrder)
VALUES ('dokastho', 'CPPaxos', 3, 3);
INSERT INTO stories(text, owner, topicId, groupId, storyOrder)
VALUES ('project 3', 'dokastho', 3, 6, 1);

INSERT INTO groups(owner, name, topicId, groupOrder)
VALUES ('dokastho', 'Placeholder Ford', 4, 1);
INSERT INTO stories(text, owner, topicId, groupId, storyOrder)
VALUES ('a story for the second topic.', 'dokastho', 4, 7, 1);
