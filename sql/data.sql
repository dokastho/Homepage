PRAGMA foreign_keys = ON;

INSERT INTO users(username, fullname, email, password)
VALUES ('dokastho', 'Thomas Dokas', 'dokastho@umich.edu', 'password');

INSERT INTO pages(title, description, body, route, owner, card_size)
VALUES ('Hello!', 'I&#39;m in the process of rewriting the code for my website&#39;s homepage. Please check back after the holiday break', 'body', 'route', 'dokastho', '1');
INSERT INTO pages(title, description, body, route, owner, card_size)
VALUES ('In the meantime', 'if you would like to see some of my personal projects, check out my <a href="https://github.com/dokastho">github', 'body', 'route', 'dokastho', '1');
