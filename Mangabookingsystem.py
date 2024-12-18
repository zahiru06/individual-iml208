def show_menu():
    print("\nManga Booking System")
    print("1. Create Manga Booking")
    print("2. View All Bookings")
    print("3. Update Booking")
    print("4. Cancel Booking")
    print("5. Exit")

def create_booking(bookings):
    name = input("Enter your name: ")
    telephone = input("Enter your telephone number: ")
    manga_title = input("Enter the manga title: ")
    borrowed_days = input("Enter the number of borrowed days: ")
    bookings.append({"name": name, "telephone": telephone, "manga_title": manga_title, "borrowed_days": borrowed_days})
    print("Booking created successfully!")

def view_bookings(bookings):
    if not bookings:
        print("No bookings available.")
    else:
        print("\nCurrent Bookings:")
        for i, booking in enumerate(bookings, start=1):
            print(f"{i}. Name: {booking['name']}, Telephone: {booking['telephone']}, Manga: {booking['manga_title']}, Borrowed Days: {booking['borrowed_days']}")

def update_booking(bookings):
    name = input("Enter the name of the customer to update: ")
    telephone = input("Enter the telephone number of the customer to update: ")
    found = False
    for booking in bookings:
        if booking['name'] == name and booking['telephone'] == telephone:
            print(f"Current Order: Manga - {booking['manga_title']}, Borrowed Days - {booking['borrowed_days']}")
            booking["manga_title"] = input("Enter new manga title: ")
            booking["borrowed_days"] = input("Enter new number of borrowed days: ")
            print("Booking updated successfully!")
            found = True
            break
    if not found:
        print("No booking found for the given customer.")

def delete_booking(bookings):
    name = input("Enter the name of the customer to cancel the order: ")
    telephone = input("Enter the telephone number of the customer to cancel the order: ")
    found = False
    for booking in bookings:
        if booking['name'] == name and booking['telephone'] == telephone:
            bookings.remove(booking)
            print("Order cancelled successfully!")
            found = True
            break
    if not found:
        print("No booking found for the given customer.")

def main():
    bookings = []
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            create_booking(bookings)
        elif choice == "2":
            view_bookings(bookings)
        elif choice == "3":
            update_booking(bookings)
        elif choice == "4":
            delete_booking(bookings)
        elif choice == "5":
            print("Exiting Manga Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
