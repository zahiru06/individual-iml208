import tkinter as tk
from tkinter import messagebox

def create_booking(bookings, name, telephone, manga_title, borrowed_days):
    if not name or not telephone or not manga_title or not borrowed_days:
        messagebox.showerror("Error", "All fields are required!")
        return
    bookings.append({"name": name, "telephone": telephone, "manga_title": manga_title, "borrowed_days": borrowed_days})
    messagebox.showinfo("Success", "Booking created successfully!")

def view_bookings(bookings, listbox):
    listbox.delete(0, tk.END)
    if not bookings:
        listbox.insert(tk.END, "No bookings available.")
    else:
        for booking in bookings:
            listbox.insert(tk.END, f"Name: {booking['name']}, Telephone: {booking['telephone']}, Manga: {booking['manga_title']}, Borrowed Days: {booking['borrowed_days']}")

def update_booking(bookings, name, telephone, manga_title, borrowed_days):
    for booking in bookings:
        if booking['name'] == name and booking['telephone'] == telephone:
            booking['manga_title'] = manga_title
            booking['borrowed_days'] = borrowed_days
            messagebox.showinfo("Success", "Booking updated successfully!")
            return
    messagebox.showerror("Error", "No booking found for the given customer.")

def delete_booking(bookings, name, telephone):
    for booking in bookings:
        if booking['name'] == name and booking['telephone'] == telephone:
            bookings.remove(booking)
            messagebox.showinfo("Success", "Order cancelled successfully!")
            return
    messagebox.showerror("Error", "No booking found for the given customer.")

def main():
    bookings = []

    def handle_create():
        create_booking(bookings, name_entry.get(), telephone_entry.get(), manga_entry.get(), days_entry.get())
        name_entry.delete(0, tk.END)
        telephone_entry.delete(0, tk.END)
        manga_entry.delete(0, tk.END)
        days_entry.delete(0, tk.END)

    def handle_view():
        view_bookings(bookings, listbox)

    def handle_update():
        update_booking(bookings, name_entry.get(), telephone_entry.get(), manga_entry.get(), days_entry.get())
        name_entry.delete(0, tk.END)
        telephone_entry.delete(0, tk.END)
        manga_entry.delete(0, tk.END)
        days_entry.delete(0, tk.END)

    def handle_delete():
        delete_booking(bookings, name_entry.get(), telephone_entry.get())
        name_entry.delete(0, tk.END)
        telephone_entry.delete(0, tk.END)

    root = tk.Tk()
    root.title("Manga Booking System")

    tk.Label(root, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1)

    tk.Label(root, text="Telephone:").grid(row=1, column=0)
    telephone_entry = tk.Entry(root)
    telephone_entry.grid(row=1, column=1)

    tk.Label(root, text="Manga Title:").grid(row=2, column=0)
    manga_entry = tk.Entry(root)
    manga_entry.grid(row=2, column=1)

    tk.Label(root, text="Borrowed Days:").grid(row=3, column=0)
    days_entry = tk.Entry(root)
    days_entry.grid(row=3, column=1)

    tk.Button(root, text="Create Booking", command=handle_create).grid(row=4, column=0, columnspan=2)
    tk.Button(root, text="View Bookings", command=handle_view).grid(row=5, column=0, columnspan=2)
    tk.Button(root, text="Update Booking", command=handle_update).grid(row=6, column=0, columnspan=2)
    tk.Button(root, text="Cancel Booking", command=handle_delete).grid(row=7, column=0, columnspan=2)

    listbox = tk.Listbox(root, width=50)
    listbox.grid(row=8, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
