import tkinter as tk
from ProductCatalog import ProductCatalog
from OrdersDeliveries import OrdersDeliveries
from AgentTransactions import AgentTransactions
from Inventory import Inventory
from RegisterProduct import RegisterProduct


class App(tk.Frame):
	def __init__(self, master, cursor):
		super().__init__(master)

		self.buttons = tk.Frame(self)
		tk.Button(self.buttons, text='catalog', command=self.view_catalog).grid(row=0, column=0)
		tk.Button(self.buttons, text='orders', command=self.view_orders).grid(row=0, column=1)
		tk.Button(self.buttons, text='transactions', command=self.view_transactions).grid(row=0, column=2)
		tk.Button(self.buttons, text='inventory', command=self.view_inventory).grid(row=0, column=3)
		tk.Button(self.buttons, text='register product', command=self.view_register_product).grid(row=0, column=4)

		self.product_catalog = ProductCatalog(self, cursor)
		self.orders_deliveries = OrdersDeliveries(self, cursor)
		self.agent_transactions = AgentTransactions(self, cursor)
		self.inventory = Inventory(self, cursor)
		self.register = RegisterProduct(self, cursor)

	def view_register_product(self):
		self.hide_views()
		self.register.pack()

	def view_catalog(self):
		self.hide_views()
		self.product_catalog.pack()

	def view_orders(self):
		self.hide_views()
		self.orders_deliveries.pack()

	def view_transactions(self):
		self.hide_views()
		self.agent_transactions.pack()

	def view_inventory(self):
		self.hide_views()
		self.inventory.pack()

	def hide_views(self):
		self.product_catalog.forget()
		self.orders_deliveries.forget()
		self.agent_transactions.forget()
		self.inventory.forget()
		self.register.forget()

	def pack(self):
		super().pack()
		self.hide_views()
		self.buttons.pack()
		self.product_catalog.pack()

	def forget(self):
		super().forget()
		self.product_catalog.forget()
		self.orders_deliveries.forget()
		self.agent_transactions.forget()
		self.inventory.forget()
		self.buttons.forget()
		self.register.forget()