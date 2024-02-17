CREATE DATABASE atme;

\c atme;

CREATE TABLE user_table (
    localID TEXT, --user id
    Email TEXT,
    DisplayName TEXT,
    photoUrl TEXT,
    refleshToken TEXT
);

CREATE TABLE tasks (
    kind TEXT,
    localID TEXT, --user id
    id TEXT, -- TASK ID
    title TEXT,
    selfLink TEXT,
    due TIMESTAMP,
    note TEXT


);



CREATE TABLE worktimeWeek (
    worktimeStart TIME[7], -- Index 0 = Sunday, Index 7 = Saturday
    worktimeEnd TIME[7],
    localID TEXT -- user id

);

CREATE TABLE worktimeDate (
    targetDate DATE,
    worktimeStart TIME,
    worktimeEnd TIME,
    localID TEXT -- user id
);

CREATE TABLE calendar (
    starttime: TIMESTAMP,
    endtime: TIMESTAMP,
    title: TEXT,
    note: TEXT,
    localID TEXT -- user id,
    calID TEXT
);

