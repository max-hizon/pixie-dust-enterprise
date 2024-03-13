import tkinter as tk

class RegisterProduct(tk.Frame):
    def __init__(self, master, cursor):
        super().__init__(master)
        self.cursor = cursor

        self.contents = tk.Frame(self)

        self.nameLabel = tk.Label(self.contents, text="name")
        self.nameEntry = tk.Entry(self.contents)
        self.nameLabel.grid(row=0, column=0)
        self.nameEntry.grid(row=0, column=1)

        self.addFeatureButton = tk.Button(self.contents, text="add feature", command=self.addFeature)
        self.featureEntryFrame = tk.Frame(self.contents)
        
        self.addFeatureButton.grid(row=1, columnspan=2)
        self.featureEntryFrame.grid(row=2, columnspan=2)
        self.addFeature()

        self.categoryLabel = tk.Label(self.contents, text="category")
        self.categoryLabel2 = tk.Label(self.contents, text="pen organizers")
        self.categoryLabel.grid(row=3, column=0)
        self.categoryLabel2.grid(row=3, column=1)

        self.slotsLabel = tk.Label(self.contents, text="slots")
        self.slotsEntry = tk.Entry(self.contents)
        self.slotsLabel.grid(row=4, column=0)
        self.slotsEntry.grid(row=4, column=1)

        self.limitLabel = tk.Label(self.contents, text="Personalization Limit")
        self.limitEntry = tk.Entry(self.contents)
        self.limitLabel.grid(row=5, column=0)
        self.limitEntry.grid(row=5, column=1)

        self.priceLabel = tk.Label(self.contents, text="Price")
        self.priceEntry = tk.Entry(self.contents)
        self.priceLabel.grid(row=6, column=0)
        self.priceEntry.grid(row=6, column=1)

        self.submitButton = tk.Button(self.contents, text="submit", command=self.submit)
        self.submitButton.grid(row=7, columnspan=2)

    def addFeature(self):
        tk.Entry(self.featureEntryFrame).pack()

    def submit(self):
        if self.validateEntries():
            self.insertQuery()
            self.clearEntries()

    def insertQuery(self):
        product_id = self.getNextProductID()
        category = 'pen organizers'
        name = self.nameEntry.get()
        personalizationLimit = self.limitEntry.get()
        price = self.priceEntry.get()
        slots = self.slotsEntry.get()

        self.cursor.execute(f'''
            INSERT INTO product (product_id, category, name, personalization_limit, price)
            VALUES ({product_id}, \'{category}\', \'{name}\', {personalizationLimit}, {price});
        ''')

        self.cursor.execute(f'''
            INSERT INTO product_pen_organizers (product_id, slots)
            VALUES ({product_id}, {slots});
        ''')

        for feature in self.getFeatures():
            self.cursor.execute(f'''
                INSERT INTO product_features (product_id, feature)
                VALUES ({product_id}, \'{feature}\');
            ''')

    def clearEntries(self):
        self.nameEntry.delete(0,'end')
        for entry in [self.slotsEntry, self.limitEntry, self.priceEntry]:
            entry.delete(0, 'end')
        for entry in self.featureEntryFrame.winfo_children():
            entry.destroy()
        self.addFeature()

    def getNextProductID(self):
        self.cursor.execute('SELECT MAX(product_id) FROM product;')
        return int(self.cursor.fetchall()[0][0])+1

    def getFeatures(self):
        return [entry.get() for entry in self.featureEntryFrame.winfo_children()]

    def validateEntries(self):
        for entry in [self.nameEntry, *self.featureEntryFrame.winfo_children()]:
            if len(entry.get()) == 0:
                return False
        for entry in [self.slotsEntry, self.limitEntry, self.priceEntry]:
            try:
                float(entry.get())
            except:
                return False
        return True

    def pack(self):
        super().pack()
        self.contents.pack()

    def forget(self):
        super().forget()
        self.contents.forget()
