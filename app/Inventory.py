import tkinter as tk
from datetime import datetime, timedelta


class Inventory(tk.Frame):
    def __init__(self, master, cursor):
        super().__init__(master)
        self.cursor = cursor
        self.datetime = datetime.now()
        self.header_contents = tk.StringVar()
        self.header_contents.set(f'INVENTORY as of {self.datetime.year}, {self.datetime.month}')
        self.header = tk.Label(self, textvariable=self.header_contents)
        self.contents = tk.Frame(self)

    def populate(self):
        for widget in self.contents.winfo_children():
            widget.destroy()
        
        cols = ['item', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'black']
        for idx, column in enumerate(cols):
            tk.Label(self.contents, text=f'{column}').grid(row=0, column=idx)

        for row, row_contents in enumerate(self.query()):
            for col, col_contents in enumerate(row_contents):
                tk.Label(self.contents, text=f'{col_contents}').grid(row=row+1, column=col)

    def query(self):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'black']
        query = []
        query.append('SELECT product.name,')
        for color in colors:
            query.append(f'coalesce({color}_stock.stock, 0) as "{color}"' \
                            + ('' if color == colors[-1] else ','))
        query.append('FROM product')
        for color in colors:
            query.append(f'LEFT OUTER JOIN product_color_stock AS {color}_stock')
            query.append(f'ON {color}_stock.product_id = product.product_id')
            query.append(f'AND {color}_stock.color = \'{color}\''\
                               + (';' if color == colors[-1] else ''))
        self.cursor.execute('\n'.join(query))
        return self.cursor.fetchall()

    def pack(self):
        super().pack()
        self.header.pack()
        self.contents.pack()
        self.populate()

    def forget(self):
        super().forget()
        self.header.forget()
        self.contents.forget()
