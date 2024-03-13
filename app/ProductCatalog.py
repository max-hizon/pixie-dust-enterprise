import tkinter as tk


class ProductCatalog(tk.Frame):
    def __init__(self, master, cursor):
        super().__init__(master)
        self.cursor = cursor

        self.cursor.execute('SELECT DISTINCT category FROM product;')
        self.categories = [i[0] for i in self.cursor.fetchall()]
        self.current_categ = 0

        self.header = tk.Label(self, text='PRODUCT CATALOG')

        self.buttons = tk.Frame(self)
        tk.Button(self.buttons, text='Prev category', command=self.prev_categ).grid(row=0, column=0)
        tk.Button(self.buttons, text='Next category', command=self.next_categ).grid(row=0, column=1)

        self.contents = tk.Frame(self)

    def next_categ(self):
        self.current_categ = (self.current_categ+1) % len(self.categories)
        self.populate()

    def prev_categ(self):
        self.current_categ = (self.current_categ-1) % len(self.categories)
        self.populate()

    def populate(self):
        for widget in self.contents.winfo_children():
            widget.destroy()

        category = self.categories[self.current_categ]
        section_header = tk.Label(self.contents, text=category).pack()
        
        extra_col = {
            'folders': 'Dimensions',
            'planners': 'Dimensions',
            'pen organizers': 'Slots',
        }
        extra_query = {
            'folders': self.query_folders,
            'planners': self.query_planners,
            'pen organizers': self.query_pen_organizers,
        }

        products_info = tk.Frame(self.contents)
        products = self.query_products(category)
        columns = ['Item', 'Features', extra_col[category], 'Personalization', 'Price']
        for idx, column in enumerate(columns):
            tk.Label(products_info, text=column).grid(row=0, column=idx)

        for row, row_contents in enumerate(self.query_products(category)):
            product_id, item, personalization, price = row_contents
            features = '\n'.join(self.query_features(product_id))
            extra = extra_query[category](product_id)

            columns = [item, features, extra, personalization, price]
            for col, col_contents in enumerate(columns):
                tk.Label(products_info, text=f'{col_contents}').grid(row=row+1, column=col)
        products_info.pack()
    
    def query_products(self, category):
        self.cursor.execute(f'''
            SELECT product_id, name, personalization_limit, price
              FROM product
             WHERE category = '{category}';
        ''')
        return self.cursor.fetchall()

    def query_features(self, product_id):
        self.cursor.execute(f'''
            SELECT product_features.feature
              FROM product_features
             WHERE product_id = {product_id};
        ''')
        return [i[0] for i in self.cursor.fetchall()]

    def query_folders(self, product_id):
        self.cursor.execute(f'''
            SELECT height, length, width
            FROM product_folders
            WHERE product_id = {product_id};
        ''')
        return '\n'.join([f'{i} inches' for i in self.cursor.fetchall()[0]])

    def query_pen_organizers(self, product_id):
        self.cursor.execute(f'''
            SELECT slots
            FROM product_pen_organizers
            WHERE product_id = {product_id};
        ''')
        return f'{self.cursor.fetchall()[0][0]}'

    def query_planners(self, product_id):
        self.cursor.execute(f'''
            SELECT height, length, width
            FROM product_planners
            WHERE product_id = {product_id};
        ''')
        return '\n'.join([f'{i} inches' for i in self.cursor.fetchall()[0]])

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
