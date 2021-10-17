drop table if exists forums,users,user_forum,topic,messages,request
CREATE TABLE forums (
    forum_id SERIAL PRIMARY KEY,
    theme TEXT NOT NULL,
    public BOOLEAN NOT NULL,
    visibility BOOLEAN NOT NULL
);

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    account TEXT UNIQUE,
    password TEXT
);

CREATE TABLE user_forum (
    forum_id INTEGER REFERENCES forums ON DELETE CASCADE,
    user_id INTEGER REFERENCES users ON DELETE SET NULL,
    isOwner BOOLEAN NOT NULL
);

CREATE TABLE topic (
    topic_id SERIAL PRIMARY KEY,
    forum_id INTEGER REFERENCES forums ON DELETE CASCADE,
    user_id INTEGER REFERENCES users ON DELETE SET NULL,
    title TEXT NOT NULL,
    visibility BOOLEAN NOT NULL
);

CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,
    topic_id INTEGER REFERENCES topic ON DELETE CASCADE,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    content TEXT NOT NULL,
    created_at TIMESTAMP,
    visibility BOOLEAN NOT NULL

);



CREATE TABLE request (
    request_id SERIAL PRIMARY KEY,
    user_id1 INTEGER REFERENCES users ON DELETE NO ACTION,
    user_id2 INTEGER REFERENCES users ON DELETE CASCADE,
    forum_id INTEGER REFERENCES forums ON DELETE CASCADE,
    owner_id INTEGER REFERENCES users ON DELETE CASCADE,
    visibility BOOLEAN NOT NULL
);