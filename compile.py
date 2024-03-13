files = [
	'Initialize.sql',
	'Person.sql',
	'Agent.sql',
	'Customer.sql',
	'Product.sql',
	'Order.sql',
]

with open('PixieDust.sql', mode='w', encoding='utf-8') as output:
	for i in files:
		with open(i, mode='r', encoding='utf-8') as sqlfile:
			print(*sqlfile, file=output, sep='')
