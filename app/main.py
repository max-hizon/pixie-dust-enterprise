import tkinter as tk
import psycopg2
from App import App

HOSTNAME = ''
DATABASE = ''
USERNAME = ''
PASSWORD = ''

def main():
	conn = psycopg2.connect(host=HOSTNAME, dbname=DATABASE, user=USERNAME, password=PASSWORD)
	conn.autocommit = True
	cursor = conn.cursor()

	root = tk.Tk()
	root.geometry("800x600")
	root.resizable(0, 0)
	root.title('PIXIE DUST ENTERPRISES')
	App(root, cursor).pack()
	root.mainloop()

	cursor.close()
	conn.close()

if __name__ == '__main__':
	main()
