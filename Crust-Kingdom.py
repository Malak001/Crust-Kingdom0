import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class PizzaOrderingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('Pizza Ordering System')
        self.create_main_window()

    def create_main_window(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.img = ImageTk.PhotoImage(Image.open("Pizza-3007395.jpg"))
        self.label_img = tk.Label(self.main_frame, image=self.img)
        self.label_img.pack()

        tk.Label(self.main_frame, text="Welcome to Crust Kingdom").pack()

        tk.Button(self.main_frame, text='Login', command=self.login).pack()
        tk.Button(self.main_frame, text='Exit', command=self.root.destroy).pack()

    def login(self):
        self.main_frame.pack_forget()
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()

        tk.Label(self.login_frame, text="Username").pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()

        tk.Label(self.login_frame, text="Password").pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()

        tk.Button(self.login_frame, text='Submit', command=self.check_login).pack()
        tk.Button(self.login_frame, text='Back', command=self.go_back).pack()
        

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        #I have username and password saver as (admin , password) for now
        correct_username = "admin"
        correct_password = "password"

        if username == correct_username and password == correct_password:
            messagebox.showinfo("Success", "Logged in successfully!")
            self.login_frame.pack_forget()
            self.home_page()
        else:
            messagebox.showerror("Error", "Incorrect username or password.")

    def go_back(self):
        self.login_frame.pack_forget()
        self.create_main_window()

    def home_page(self):
        self.home_page_frame = tk.Frame(self.root)
        self.home_page_frame.pack()

        tk.Label(self.home_page_frame, text="Home Page").pack()

        self.menu_items = ["Pizza Margherita", "Pizza Pepperoni", "Pizza Hawaii"]
        self.cart = []

        for item in self.menu_items:
            button = tk.Button(self.home_page_frame, text=f"Add {item} to cart", 
                            command=lambda item=item: self.add_to_cart(item))
            button.pack()

        tk.Button(self.home_page_frame, text='View Cart', command=self.view_cart).pack()
        tk.Button(self.home_page_frame, text='Logout', command=self.logout).pack()

    def add_to_cart(self, item):
        self.cart.append(item)
        messagebox.showinfo("Success", f"{item} added to cart!")

    def view_cart(self):
        messagebox.showinfo("Cart", "\n".join(self.cart))

    def logout(self):
        self.home_page_frame.pack_forget()
        self.create_main_window()


if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaOrderingSystem(root)
    root.mainloop()
