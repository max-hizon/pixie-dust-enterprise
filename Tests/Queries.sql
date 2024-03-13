SELECT *
FROM person;

SELECT p.name, a.customer_count
FROM person p, agent a
WHERE a.person_id = p.person_id;

SELECT c.customer_id, a.agent_id, o.order_id
FROM customer c, agent a, orders o
WHERE c.customer_id = o.customer_id
AND a.agent_id = o.agent_id;

SELECT *
FROM product_pen_organizers;

SELECT c.customer_id, p.name
FROM customer c, person p
WHERE c.person_id = p.person_id;

SELECT *
FROM product
WHERE price < 30000;

SELECT p.name, pf.feature
FROM product p, product_features pf
WHERE pf.product_id = p.product_id;
