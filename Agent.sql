CREATE TABLE agent (
    PRIMARY KEY (agent_id),
    FOREIGN KEY (person_id) REFERENCES person(person_id),
    agent_id       INT NOT NULL,
    person_id      INT NOT NULL,
    customer_count INT NOT NULL DEFAULT 0
);
