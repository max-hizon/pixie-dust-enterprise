DROP DATABASE pixiedustmain;
CREATE DATABASE pixiedustmain;
DROP TABLE agent CASCADE;
DROP TABLE customer CASCADE;
DROP TABLE order_recipient CASCADE;
DROP TABLE ordered_product CASCADE;
DROP TABLE orders CASCADE;
DROP TABLE person CASCADE;
DROP TABLE product CASCADE;
DROP TABLE product_color_stock CASCADE;
DROP TABLE product_features CASCADE;
DROP TABLE product_folders CASCADE;
DROP TABLE product_pen_organizers CASCADE;
DROP TABLE product_planners CASCADE;

CREATE TABLE person (
    PRIMARY KEY (person_id),
    person_id INT          NOT NULL,
    name      VARCHAR(127) NOT NULL
);

CREATE TABLE agent (
    PRIMARY KEY (agent_id),
    FOREIGN KEY (person_id) REFERENCES person(person_id),
    agent_id       INT NOT NULL,
    person_id      INT NOT NULL,
    customer_count INT NOT NULL DEFAULT 0
);

CREATE TABLE customer (
    PRIMARY KEY (customer_id),
    FOREIGN KEY (agent_id)  REFERENCES agent(agent_id),
    FOREIGN KEY (person_id) REFERENCES person(person_id),
    customer_id INT NOT NULL,
    agent_id    INT NOT NULL,
    person_id   INT NOT NULL
);

CREATE TABLE product (
    PRIMARY KEY (product_id),
    product_id            INT            NOT NULL,
    category              VARCHAR(31)    NOT NULL,
    name                  VARCHAR(127)   NOT NULL,
    personalization_limit INT            NOT NULL,
    price                 NUMERIC(16, 2) NOT NULL,
    CHECK (category IN ('folders', 'pen organizers', 'planners'))
);

CREATE TABLE product_features (
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    product_id INT          NOT NULL,
    feature    VARCHAR(127) NOT NULL DEFAULT ''
);

CREATE TABLE product_pen_organizers (
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    product_id INT NOT NULL,
    slots      INT NOT NULL
);

CREATE TABLE product_folders (
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    product_id INT           NOT NULL,
    height     NUMERIC(6, 2) NOT NULL,
    length     NUMERIC(6, 2) NOT NULL,
    width      NUMERIC(6, 2) NOT NULL
);

CREATE TABLE product_planners (
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    product_id INT           NOT NULL,
    height     NUMERIC(6, 2) NOT NULL,
    length     NUMERIC(6, 2) NOT NULL,
    width      NUMERIC(6, 2) NOT NULL
);

CREATE TABLE product_color_stock (
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    product_id INT          NOT NULL,
    color      VARCHAR(7)   NOT NULL,
    stock      INT          NOT NULL,
    CHECK (color IN ('red', 'orange', 'yellow', 'green',
                     'blue', 'purple', 'pink', 'black'))
);

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

