import tkinter as tk


class OrdersDeliveries(tk.Frame):
    def __init__(self, master, cursor):
        super().__init__(master)
        self.cursor = cursor

        self.cursor.execute('SELECT order_id FROM orders;')
        self.orders = [i[0] for i in self.cursor.fetchall()]
        self.current_order = 0

        self.header = tk.Label(self, text='ORDER FORM')

        self.buttons = tk.Frame(self)
        tk.Button(self.buttons, text='Prev order', command=self.prev_order).grid(row=0, column=0)
        tk.Button(self.buttons, text='Next order', command=self.next_order).grid(row=0, column=1)

        self.contents = tk.Frame(self)

    def next_order(self):
        self.current_order = (self.current_order+1) % len(self.orders)
        self.populate()

    def prev_order(self):
        self.current_order = (self.current_order-1) % len(self.orders)
        self.populate()

    def populate(self):
        for widget in self.contents.winfo_children():
            widget.destroy()
        
        order_id = self.orders[self.current_order]
        order_info = tk.Frame(self.contents)

        recipients = '/'.join(self.query_recipients(order_id))
        customer, address, schedule, gift, date, agent = self.query_order(order_id)
        tk.Label(order_info, text=f'Customer: {customer}').grid(row=0, column=0)
        tk.Label(order_info, text=f'Delivery Address: {address}').grid(row=1, column=0)
        tk.Label(order_info, text=f'Schedule: {schedule}').grid(row=2, column=0)
        tk.Label(order_info, text=f'Recipient: {recipients}').grid(row=3, column=0)
        tk.Label(order_info, text=f'Gift: {gift}').grid(row=4, column=0)
        tk.Label(order_info, text=f'Order No.: {order_id}').grid(row=0, column=1)
        tk.Label(order_info, text=f'Date: {date}').grid(row=1, column=1)
        tk.Label(order_info, text=f'Agent: {agent}').grid(row=2, column=1)
        tk.Label(order_info, text=f'Amount Due: {self.query_due(order_id):.2f}').grid(row=3, column=1)

        order_info.pack()

        products_info = tk.Frame(self.contents)
        for idx, column in enumerate(['Item', 'Description', 'Qty', 'SRP', 'Discount', 'Total']):
            tk.Label(products_info, text=column).grid(row=0, column=idx)

        for row, row_contents in enumerate(self.query_products(order_id)):
            product, color, personalization, qty, srp, discount, total = row_contents
            description = f'Color: {color}\nPersonalization: {personalization}'
            for col, col_contents in enumerate([product, description, qty, srp, discount, f'{float(total):.2f}']):
                tk.Label(products_info, text=f'{col_contents}').grid(row=row+1, column=col)

        products_info.pack()

    def query_order(self, order_id):
        self.cursor.execute(f'''
            SELECT customer_info.name, delivery_address, schedule, gift, order_date, agent_info.name
              FROM orders
                   JOIN customer ON customer.customer_id = orders.customer_id
                   JOIN agent ON agent.agent_id = orders.agent_id
                   JOIN person AS customer_info
                     ON customer_info.person_id = customer.person_id
                   JOIN person AS agent_info
                     ON agent_info.person_id = agent.person_id
             WHERE order_id = {order_id};
        ''')
        return self.cursor.fetchall()[0]

    def query_recipients(self, order_id):
        self.cursor.execute(f'''
            SELECT recipient.name
              FROM order_recipient
                   JOIN person as recipient ON recipient.person_id = order_recipient.person_id
             WHERE order_id = {order_id};
        ''')
        return [i[0] for i in self.cursor.fetchall()]

    def query_products(self, order_id):
        self.cursor.execute(f'''
            SELECT product.name, color, personalization, quantity, product.price, discount,
                   quantity*(product.price-product.price*discount*0.01)
              FROM ordered_product
                   JOIN product ON product.product_id = ordered_product.product_id
             WHERE order_id = {order_id};
        ''')
        return self.cursor.fetchall()

    def query_due(self, order_id):
        self.cursor.execute(f'''
            SELECT SUM(quantity*(product.price-product.price*discount*0.01))
              FROM ordered_product
                   JOIN product ON product.product_id = ordered_product.product_id
             WHERE order_id = {order_id};
        ''')
        return float(self.cursor.fetchall()[0][0])

    def pack(self):
        super().pack()
        self.header.pack()
        self.buttons.pack()
        self.contents.pack()
        self.populate()

    def forget(self):
        super().forget()
        self.header.forget()
        self.buttons.forget()
        self.contents.forget()
