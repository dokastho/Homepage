PRAGMA foreign_keys = ON;

INSERT INTO users(username, fullname, email, password)
VALUES ('dokastho', 'Thomas Dokas', 'dokastho@umich.edu', 'password');

INSERT INTO pages(title, description, body, route, owner, card_size)
VALUES ('Hello!', 'I''m in the process of rewriting the code for my website''s homepage. Please check back after the holiday break', 'body', 'route', 'dokastho', '1');
INSERT INTO pages(title, description, body, route, owner, card_size)
VALUES ('In the meantime', 'if you would like to see some of my personal projects, check out my github: https://github.com/dokastho', 'body', 'route', 'dokastho', '1');
