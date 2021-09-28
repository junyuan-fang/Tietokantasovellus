CREATE TABLE forums (
    forum_id SERIAL PRIMARY KEY,
    theme TEXT NOT NULL,
    visibility BOOLEAN NOT NULL
);

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    forum_id INTEGER REFERENCES forums NOT NULL,
    account VARCHAR(30) UNIQUE,
    password VARCHAR(30)
);

CREATE TABLE user_forum (
    forum_id INTEGER REFERENCES forums NOT NULL,
    user_id INTEGER REFERENCES users NOT NULL,
    isOwner INTEGER NOT NULL
);

CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,
    topic_id INTEGER REFERENCES topic NOT NULL,
    user_id INTEGER REFERENCES users NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP,
    visibility BOOLEAN NOT NULL

);

CREATE TABLE topic (
    topic_id SERIAL PRIMARY KEY,
    forum_id INTEGER REFERENCES forums NOT NULL,
    user_id INTEGER REFERENCES users NOT NULL,
    title TEXT NOT NULL,
    visibility BOOLEAN NOT NULL
);

CREATE TABLE request (
    request_id SERIAL PRIMARY KEY,
    user_id_asking INTEGER REFERENCES users NOT NULL,
    forum_id_to INTEGER REFERENCES forums NOT NULL,
    user_id_admin INTEGER REFERENCES users NOT NULL,
    confirmValue BOOLEAN NOT NULL
);