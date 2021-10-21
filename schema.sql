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
    isOwner BOOLEAN NOT NULL,
    PRIMARY KEY (forum_id,user_id)
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



-- CREATE TABLE request (
--     request_id SERIAL PRIMARY KEY,
--     user_id1 INTEGER REFERENCES users ON DELETE NO ACTION,
--     user_id2 INTEGER REFERENCES users ON DELETE CASCADE,
--     forum_id INTEGER REFERENCES forums ON DELETE CASCADE,
--     owner_id INTEGER REFERENCES users ON DELETE CASCADE,
--     visibility BOOLEAN NOT NULL
-- );

CREATE TABLE request (
    request_id SERIAL,
    user_id1 INTEGER ,
    user_id2 INTEGER ,
    forum_id INTEGER ,
    owner_id INTEGER ,
    visibility BOOLEAN NOT NULL,
    PRIMARY KEY( user_id1, user_id2, forum_id, owner_id),
    FOREIGN KEY (user_id1) REFERENCES users ON DELETE NO ACTION,
    FOREIGN KEY (user_id2) REFERENCES users ON DELETE CASCADE,
    FOREIGN KEY (forum_id) REFERENCES forums ON DELETE CASCADE,
    FOREIGN KEY (owner_id) REFERENCES users ON DELETE CASCADE 
);