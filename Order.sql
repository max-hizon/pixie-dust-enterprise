CREATE TABLE orders (
    PRIMARY KEY (order_id),
    FOREIGN KEY (agent_id)    REFERENCES agent(agent_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    order_id         INT            NOT NULL,
    agent_id         INT            NOT NULL,
    customer_id      INT            NOT NULL,
    delivery_address VARCHAR(127)   NOT NULL,
    gift             BOOLEAN        NOT NULL DEFAULT FALSE,
    order_date       DATE           NOT NULL,
    schedule         DATE           NOT NULL
);

CREATE TABLE ordered_product (
    FOREIGN KEY (order_id)   REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    order_id        INT          NOT NULL,
    product_id      INT          NOT NULL,
    color           VARCHAR(127) NOT NULL,
    discount        INT          NOT NULL DEFAULT 0,
    personalization VARCHAR(127) NOT NULL DEFAULT '',
    quantity        INT          NOT NULL DEFAULT 1,
    CHECK (color IN ('red', 'orange', 'yellow', 'green',
                     'blue', 'purple', 'pink', 'black'))
);

CREATE TABLE order_recipient (
    FOREIGN KEY (order_id)  REFERENCES orders(order_id),
    FOREIGN KEY (person_id) REFERENCES person(person_id),
    order_id  INT NOT NULL,
    person_id INT NOT NULL
);
