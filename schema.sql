CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,
    topic_id INTEGER REFERENCES topic NOT NULL,
    user_id INTEGER REFERENCES user NOT NULL,
    content TEXT NOT NULL,
    visibility BOOLEAN NOT NULL

);

CREATE TABLE topic (
    topic_id SERIAL PRIMARY KEY,
    forum_id INTEGER REFERENCES topic NOT NULL,
    user_id INTEGER REFERENCES user NOT NULL,
    title TEXT NOT NULL,
    visibility BOOLEAN NOT NULL
);

CREATE TABLE forum (
    forum_id SERIAL PRIMARY KEY,
    theme TEXT NOT NULL,
    visibility BOOLEAN NOT NULL
    
);

CREATE TABLE user_forum (
    forum_id INTEGER REFERENCES user NOT NULL,
    user_id INTEGER REFERENCES user NOT NULL,
    isOwner INTEGER NOT NULL
);

CREATE TABLE user (
    user_id SERIAL PRIMARY KEY,
    forum_id INTEGER REFERENCES user NOT NULL,
    account VARCHAR(30) UNIQUE,
    password VARCHAR(30),
);

CREATE TABLE request (
    request_id SERIAL PRIMARY KEY,
    user_id_asking INTEGER REFERENCES user NOT NULL,
    forum_id_to INTEGER REFERENCES forum NOT NULL,
    user_id_admin INTEGER REFERENCES user NOT NULL,
    confirmValue BOOLEAN NOT NULL
);