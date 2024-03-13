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
