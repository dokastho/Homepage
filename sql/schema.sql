PRAGMA foreign_keys = ON;

CREATE TABLE users(
  username VARCHAR(20) NOT NULL,
  fullname VARCHAR(40) NOT NULL,
  email VARCHAR(40) NOT NULL,
  filename VARCHAR(64) NOT NULL,
  password VARCHAR(256) NOT NULL,
  created DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(username)
);

CREATE TABLE pages(
  title TINYTEXT NOT NULL,
  description TINYTEXT,
  body MEDIUMTEXT,
  route TINYTEXT,
  owner VARCHAR(20) NOT NULL,
  page_id INTEGER PRIMARY KEY AUTOINCREMENT,
  FOREIGN KEY(owner) REFERENCES users(username)
);
