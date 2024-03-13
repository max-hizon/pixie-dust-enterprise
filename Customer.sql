CREATE TABLE customer (
    PRIMARY KEY (customer_id),
    FOREIGN KEY (agent_id)  REFERENCES agent(agent_id),
    FOREIGN KEY (person_id) REFERENCES person(person_id),
    customer_id INT NOT NULL,
    agent_id    INT NOT NULL,
    person_id   INT NOT NULL
);
