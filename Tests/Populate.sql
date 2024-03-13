INSERT INTO person (person_id, name)
VALUES (1001, 'Diluc Ragnvindr'),
       (1002, 'Venti'),
       (1003, 'Victor Magtanggol'),
       (1004, 'Maria Ressa'),
       (1005, 'Osana Azuma'),
       (1006, 'Hoh Lee'),
       (1007, 'Yoshi P.'),
       (1008, 'Axis Snowdrop'),
       (1009, 'Ashley Pinefall'),
       (1010, 'Nelly Khitsu'),
       (1011, 'Carrie Itson'),
       (1012, 'Elliot Rainydew'),
       (1013, 'Badger Ramoh');

INSERT INTO agent (agent_id, person_id, customer_count)
VALUES (2001, 1001, 0),
       (2010, 1002, 0),
       (2002, 1003, 20),
       (2020, 1004, 10),
       (2003, 1005, 0),
       (2030, 1006, 0),
       (2004, 1007, 15),
       (2005, 1008, 2),
       (2006, 1010, 2);

INSERT INTO customer (customer_id, agent_id, person_id)
VALUES (3002, 2001, 1002),
       (3004, 2010, 1004),
       (3006, 2002, 1006),
       (3008, 2004, 1007),
       (3010, 2004, 1001),
       (3012, 2005, 1009),
       (3014, 2005, 1012),
       (3015, 2006, 1011),
       (3016, 2006, 1013);

INSERT INTO product (product_id, category, name, personalization_limit, price)
VALUES (4001, 'planners', 'yung ninakaw na notebook ni albedo', 30, 12345),
       (4002, 'folders', 'mga harana ni venti', 32, 31415),
       (4003, 'pen organizers', 'pencil case ni xinqiu', 32, 12345),
       (4004, 'folders', 'flipper', 8, 745),
       (4005, 'folders', 'filer', 8, 995),
       (4006, 'folders', 'keeper', 8, 895),
       (4007, 'pen organizers', 'slinger', 5, 95),
       (4008, 'pen organizers', 'shifter', 8, 295),
       (4009, 'pen organizers', 'wrapper', 6, 345),
       (4010, 'planners', 'doodler', 8, 595),
       (4011, 'planners', 'scribbler', 8, 595);


INSERT INTO product_features (product_id, feature)
VALUES (4001, 'mjolnir'),
       (4002, 'venti sadboi vibes'),
       (4002, 'may kasamang paboritong kanta ni barbara'),
       (4002, 'pampatulog ni xiao'),
       (4003, 'may kasamang pencil sharpener'),
       (4004, 'reversible'),
       (4004, 'slim and compact'),
       (4004, 'leatherette material'),
       (4004, 'magnetic corners'),
       (4004, 'magnetic clipboard'),
       (4004, 'envelope pocket'),
       (4004, 'pen loop (2)'),
       (4005, 'multi-function portfolio organizer'),
       (4005, 'leather exterior'),
       (4005, 'magnetic flap'),
       (4005, '3-ring binder'),
       (4005, 'sleeves for papers'),
       (4005, 'pen loop'),
       (4005, 'concealable handles'),
       (4006, 'accordion-style with label slots'),
       (4006, 'leather exterior'),
       (4006, 'waterproof interior'),
       (4006, 'magnetic lock'),
       (4006, 'pen loop (2)'),
       (4006, 'detachable shoulder strap'),
       (4007, 'magnetic lock'),
       (4007, 'dual ribbon straps with velcro'),
       (4007, 'water repellant'),
       (4007, 'no tear interior lining'),
       (4008, 'triple zipper'),
       (4008, 'expandable bin'),
       (4008, 'velcro-locked pockets'),
       (4008, 'water repellant'),
       (4009, 'water resistant'),
       (4009, 'leather exterior'),
       (4009, '4-way compartment'),
       (4009, 'flexible format'),
       (4009, 'magnetic buttons'),
       (4010, 'smyth sewn hardbound'),
       (4010, 'premium 120 gsm paper'),
       (4010, 'monthly spread'),
       (4010, 'weekly, daily views'),
       (4010, 'non-lined, colorable pages'),
       (4010, 'leisure list'),
       (4010, 'money tracker'),
       (4010, 'back pocket'),
       (4011, 'smyth sewn hardbound'),
       (4011, 'premium 100 gsm paper'),
       (4011, 'weekly spread'),
       (4011, 'monthly spread'),
       (4011, 'limited notes pages'),
       (4011, 'monthly watercolor artwork'),
       (4011, 'optional sleeve (+185)');

INSERT INTO product_pen_organizers (product_id, slots)
VALUES (4003, 5),
       (4007, 6),
       (4008, 15),
       (4009, 4);

INSERT INTO product_folders (product_id, height, length, width)
VALUES (4002, 10, 4, 20),
       (4004, 13.5, 10.25, 0.75),
       (4005, 14, 11, 1.5),
       (4006, 14, 11.5, 1);

INSERT INTO product_planners (product_id, height, length, width)
VALUES (4001, 9, 8, 7),
       (4010, 8, 6, 0.75),
       (4011, 8.5, 6, 0.75);

INSERT INTO product_color_stock (product_id, color, stock)
VALUES (4001, 'red', 3),
       (4001, 'orange', 1),
       (4001, 'yellow', 4),
       (4002, 'green', 1),
       (4002, 'blue', 5),
       (4002, 'purple', 9),
       (4003, 'pink', 2),
       (4003, 'black', 6),
       (4003, 'red', 8),
       (4007, 'red', 60),
       (4007, 'orange', 43),
       (4007, 'yellow', 94),
       (4007, 'green', 98),
       (4007, 'blue', 30),
       (4007, 'purple', 30),
       (4007, 'pink', 85),
       (4007, 'black', 88),
       (4008, 'red', 93),
       (4008, 'orange', 18),
       (4008, 'yellow', 84),
       (4008, 'green', 71),
       (4008, 'blue', 75),
       (4008, 'purple', 48),
       (4008, 'pink', 45),
       (4008, 'black', 3),
       (4009, 'red', 50),
       (4009, 'orange', 11),
       (4009, 'yellow', 66),
       (4009, 'green', 25),
       (4009, 'blue', 21),
       (4009, 'purple', 79),
       (4009, 'pink', 54),
       (4009, 'black', 93);

INSERT INTO orders (order_id, agent_id, customer_id, order_date, schedule, delivery_address, gift)
VALUES (5001, 2001, 3002, '2021-12-12', '2022-1-4', 'Windrise Tree', false),
       (5002, 2004, 3008, '2021-12-12', '2022-1-10', 'Loyola Heights', false),
       (5003, 2004, 3010, '2021-12-13', '2022-1-11', 'Summoners Rift', true),
       (5004, 2005, 3012, '2025-2-1', '2025-2-10', 'North Point, Dewpeak', false),
       (5005, 2006, 3016, '2021-12-14', '2022-1-25', 'Quezon City', true);

INSERT INTO ordered_product (order_id, product_id, discount, personalization, color, quantity)
VALUES (5001, 4002, 0, 'XxBarbatosxX', 'blue', 1),
       (5002, 4003, 0, 'Cloud_Strife', 'red', 1),
       (5003, 4001, 0, 'Vi', 'pink', 3),
       (5004, 4006, 0, '(none)', 'blue', 1),
       (5004, 4007, 0.10, 'Tasi', 'orange', 1),
       (5005, 4008, 0, 'Victhory', 'blue', 1);

INSERT INTO order_recipient (order_id, person_id)
VALUES (5001, 1002),
       (5002, 1007),
       (5003, 1003),
       (5004, 1009),
       (5005, 1013);
