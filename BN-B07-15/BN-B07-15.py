import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox, StringVar, Frame
from tkinter.ttk import Treeview, Style
from tkinter import font
from datetime import datetime

def setup_database():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT NOT NULL,
                      author TEXT NOT NULL,
                      isbn TEXT UNIQUE NOT NULL,
                      quantity INTEGER NOT NULL,
                      updated_at TEXT
                      )''')
    conn.commit()
    conn.close()

class BookstoreApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Bookstore Inventory Management")
        self.master.geometry("1200x650")  # Increased window width
        self.master.config(bg="#f4f4f9")

        # Set ttk style for Treeview
        style = Style()
        style.configure("Treeview", font=("Segoe UI", 11), rowheight=25)
        style.configure("Treeview.Heading", font=("Segoe UI", 13, "bold"), background="#4C8BF5", foreground="black")
        style.map("Treeview", background=[('selected', '#2a5298')])

        # Input fields frame
        input_frame = Frame(master, relief="solid", borderwidth=1, bg="#ffffff")
        input_frame.pack(pady=20, padx=40, fill="x")  # Increased padding for better spacing

        Label(input_frame, text="Book Title:", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.title_var = StringVar()
        Entry(input_frame, textvariable=self.title_var, width=40, font=("Arial", 12), bg="#e0f7fa").grid(row=0, column=1, padx=10, pady=10)

        Label(input_frame, text="Author:", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.author_var = StringVar()
        Entry(input_frame, textvariable=self.author_var, width=40, font=("Arial", 12), bg="#e0f7fa").grid(row=1, column=1, padx=10, pady=10)

        Label(input_frame, text="ISBN:", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.isbn_var = StringVar()
        Entry(input_frame, textvariable=self.isbn_var, width=40, font=("Arial", 12), bg="#e0f7fa").grid(row=2, column=1, padx=10, pady=10)

        Label(input_frame, text="Quantity:", font=("Arial", 12), bg="#ffffff").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.quantity_var = StringVar()
        Entry(input_frame, textvariable=self.quantity_var, width=40, font=("Arial", 12), bg="#e0f7fa").grid(row=3, column=1, padx=10, pady=10)

        # Search frame
        search_frame = Frame(master, relief="solid", borderwidth=1, bg="#ffffff")
        search_frame.pack(pady=20, padx=40, fill="x")

        Label(search_frame, text="Search Book (Title/Author/ISBN):", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.search_var = StringVar()
        Entry(search_frame, textvariable=self.search_var, width=40, font=("Arial", 12), bg="#e0f7fa").grid(row=0, column=1, padx=10, pady=10)
        Button(search_frame, text="Search", command=self.search_books, font=("Arial", 12), bg="#4C8BF5", fg="white", relief="flat").grid(row=0, column=2, padx=10, pady=10)

        # Buttons frame
        button_frame = Frame(master, relief="solid", borderwidth=1, bg="#ffffff")
        button_frame.pack(pady=20, padx=40, fill="x")

        Button(button_frame, text="Add Book", command=self.add_book, font=("Arial", 12), bg="#4CAF50", fg="white", relief="flat").grid(row=0, column=0, padx=10, pady=10)
        Button(button_frame, text="Clear", command=self.clear_fields, font=("Arial", 12), bg="#FFC107", fg="white", relief="flat").grid(row=0, column=1, padx=10, pady=10)
        Button(button_frame, text="Show Inventory", command=self.show_inventory, font=("Arial", 12), bg="#2196F3", fg="white", relief="flat").grid(row=0, column=2, padx=10, pady=10)
        Button(button_frame, text="Update Book", command=self.update_book, font=("Arial", 12), bg="#FF5722", fg="white", relief="flat").grid(row=0, column=3, padx=10, pady=10)
        Button(button_frame, text="Delete Book", command=self.delete_book, font=("Arial", 12), bg="#F44336", fg="white", relief="flat").grid(row=0, column=4, padx=10, pady=10)

        # Treeview for inventory
        self.tree = Treeview(master, columns=("Title", "Author", "ISBN", "Quantity", "Updated At"), show="headings", style="Custom.Treeview")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("ISBN", text="ISBN")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Updated At", text="Updated At")
        self.tree.bind("<ButtonRelease-1>", self.load_selected_row)
        self.tree.pack(fill="both", expand=True, padx=40, pady=20)

        # Alternating row colors
        self.tree.tag_configure("even", background="#f9f9f9")
        self.tree.tag_configure("odd", background="#ffffff")

    def add_book(self):
        title = self.title_var.get().strip()
        author = self.author_var.get().strip()
        isbn = self.isbn_var.get().strip()
        quantity = self.quantity_var.get().strip()

        if not title or not author or not isbn or not quantity:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a number!")
            return

        updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect("bookstore.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO books (title, author, isbn, quantity, updated_at) VALUES (?, ?, ?, ?, ?) ",
                           (title, author, isbn, quantity, updated_at))
            conn.commit()
            messagebox.showinfo("Success", "Book added successfully!")
            self.clear_fields()
            self.show_inventory()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "ISBN already exists!")
        finally:
            conn.close()

    def clear_fields(self):
        self.title_var.set("")
        self.author_var.set("")
        self.isbn_var.set("")
        self.quantity_var.set("")

    def show_inventory(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = sqlite3.connect("bookstore.db")
        cursor = conn.cursor()
        cursor.execute("SELECT title, author, isbn, quantity, updated_at FROM books")
        for index, row in enumerate(cursor.fetchall()):
            tag = "odd" if index % 2 == 0 else "even"
            self.tree.insert("", "end", values=row, tags=(tag,))
        conn.close()

    def search_books(self):
        search_term = self.search_var.get().strip()

        if not search_term:
            messagebox.showerror("Error", "Please enter a search term!")
            return

        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = sqlite3.connect("bookstore.db")
        cursor = conn.cursor()
        query = """
        SELECT title, author, isbn, quantity, updated_at 
        FROM books 
        WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?
        """
        cursor.execute(query, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)
        conn.close()

    def update_book(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No book selected for updating!")
            return

        # Get the selected row's values
        item_values = self.tree.item(selected_item, "values")
        isbn = item_values[2]
        title = self.title_var.get().strip()
        author = self.author_var.get().strip()
        quantity = self.quantity_var.get().strip()

        if not title or not author or not quantity:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a number!")
            return

        updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect("bookstore.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET title = ?, author = ?, isbn = ?, quantity = ?, updated_at = ? WHERE isbn = ?", 
                       (title, author, isbn, quantity, updated_at, isbn))
        if cursor.rowcount == 0:
            messagebox.showerror("Error", "Failed to update the book!")
        else:
            conn.commit()
            messagebox.showinfo("Success", "Book updated successfully!")
            self.show_inventory()
        conn.close()

    def load_selected_row(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item, "values")
            self.title_var.set(item_values[0])
            self.author_var.set(item_values[1])
            self.isbn_var.set(item_values[2])
            self.quantity_var.set(item_values[3])

    def delete_book(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No book selected for deletion!")
            return

        item_values = self.tree.item(selected_item, "values")
        isbn = item_values[2]

        conn = sqlite3.connect("bookstore.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE isbn = ?", (isbn,))
        if cursor.rowcount == 0:
            messagebox.showerror("Error", "Failed to delete the book!")
        else:
            conn.commit()
            messagebox.showinfo("Success", "Book deleted successfully!")
            self.show_inventory()
        conn.close()

if __name__ == "__main__":
    setup_database()
    root = Tk()
    app = BookstoreApp(root)
    root.mainloop()
