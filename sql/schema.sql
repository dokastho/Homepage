PRAGMA foreign_keys = ON;

CREATE TABLE users(
  username VARCHAR(20) NOT NULL,
  fullname VARCHAR(40) NOT NULL,
  email VARCHAR(40) NOT NULL,
  -- filename VARCHAR(64) NOT NULL,
  password VARCHAR(256) NOT NULL,
  created DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(username)
);

CREATE TABLE topics(
  topicId INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(64) NOT NULL,
  owner VARCHAR(20) NOT NULL,
  styles VARCHAR(256) NOT NULL,
  icon VARCHAR(64) NOT NULL,
  FOREIGN KEY(owner) REFERENCES users(username) ON DELETE CASCADE
);

CREATE TABLE groups(
  groupId INTEGER PRIMARY KEY AUTOINCREMENT,
  owner VARCHAR(20) NOT NULL,
  name VARCHAR(64) NOT NULL,
  topicId INTEGER NOT NULL,
  groupOrder INTEGER NOT NULL,
  FOREIGN KEY(topicId) REFERENCES topics(topicId) ON DELETE CASCADE,
  FOREIGN KEY(owner) REFERENCES users(username) ON DELETE CASCADE
);

CREATE TABLE media(
  mediaId INTEGER PRIMARY KEY AUTOINCREMENT,
  uuid VARCHAR(64) NOT NULL,
  owner VARCHAR(20) NOT NULL,
  topicId INTEGER NOT NULL,
  groupId INTEGER NOT NULL,
  storyOrder INTEGER NOT NULL,
  FOREIGN KEY(topicId) REFERENCES topics(topicId) ON DELETE CASCADE,
  FOREIGN KEY(groupId) REFERENCES groups(groupId) ON DELETE CASCADE,
  FOREIGN KEY(owner) REFERENCES users(username) ON DELETE CASCADE
);

CREATE TABLE stories(
  storyId INTEGER PRIMARY KEY AUTOINCREMENT,
  text VARCHAR(400) NOT NULL,
  owner VARCHAR(20) NOT NULL,
  topicId INTEGER NOT NULL,
  groupId INTEGER NOT NULL,
  storyOrder INTEGER NOT NULL,
  FOREIGN KEY(topicId) REFERENCES topics(topicId) ON DELETE CASCADE,
  FOREIGN KEY(groupId) REFERENCES groups(groupId) ON DELETE CASCADE,
  FOREIGN KEY(owner) REFERENCES users(username) ON DELETE CASCADE
);
