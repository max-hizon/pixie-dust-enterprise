import tkinter as tk
from datetime import datetime, timedelta


class AgentTransactions(tk.Frame):
    def __init__(self, master, cursor):
        super().__init__(master)
        self.cursor = cursor

        self.datetime = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        self.header_contents = tk.StringVar()
        self.header_contents.set(f'AGENT TRANSACTIONS {self.datetime.year} {self.datetime.month}')
        self.header = tk.Label(self, textvariable=self.header_contents)

        self.buttons = tk.Frame(self)
        tk.Button(self.buttons, text='Prev month', command=self.prev_month).grid(row=0, column=0)
        tk.Button(self.buttons, text='Next month', command=self.next_month).grid(row=0, column=1)

        self.contents = tk.Frame(self)

    def next_month(self):
        self.datetime = (self.datetime + timedelta(days=32)).replace(day=1)
        self.header_contents.set(f'AGENT TRANSACTIONS {self.datetime.year} {self.datetime.month}')
        self.populate()

    def prev_month(self):
        self.datetime = (self.datetime - timedelta(days=1)).replace(day=1)
        self.header_contents.set(f'AGENT TRANSACTIONS {self.datetime.year} {self.datetime.month}')
        self.populate()

    def populate(self):
        for widget in self.contents.winfo_children():
            widget.destroy()

        for idx, column in enumerate(['order_date', 'agent', 'customer', 'order_id', 'amount_due']):
            tk.Label(self.contents, text=f'{column}').grid(row=0, column=idx)
            
        for row, row_contents in enumerate(self.query()):
            for col, col_contents in enumerate(row_contents[1:]):
                tk.Label(self.contents, text=f'{col_contents}').grid(row=row+1, column=col)
            amount_due = self.query_due(row_contents[0])
            tk.Label(self.contents, text=f'{amount_due:.2f}').grid(row=row+1, column=len(row_contents)-1)
                
    def query(self):
        self.cursor.execute(f'''
            SELECT order_id, order_date, agent_info.name, customer_info.name, order_id
              FROM orders
                   JOIN customer ON customer.customer_id = orders.customer_id
                   JOIN agent ON agent.agent_id = orders.agent_id
                   JOIN person AS customer_info
                     ON customer_info.person_id = customer.person_id
                   JOIN person AS agent_info
                     ON agent_info.person_id = agent.person_id
             WHERE DATE '{self.datetime.year}-{self.datetime.month}-1' < order_date
               AND order_date < DATE '{self.datetime.year}-{self.datetime.month}-1' + INTERVAL '1 month';
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
        self.buttons.pack()
        self.header.pack()
        self.contents.pack()
        self.populate()

    def forget(self):
        super().forget()
        self.header.forget()
        self.buttons.forget()
        self.contents.forget()
