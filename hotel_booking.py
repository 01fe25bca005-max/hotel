name = input("Enter guest name: ")
phone = input("Enter phone number: ")
booking_id = input("Enter booking ID: ")
check_in = input("Enter check-in date: ")
nights = int(input("Enter number of nights: "))
room_type = input("Enter room type (Single/Double/Deluxe): ")
price = float(input("Enter price per night: "))
total = nights * price
print("\\n--- Hotel Booking Details ---")
print("Guest Name:", name)
print("Phone Number:", phone)
print("Booking ID:", booking_id)
print("Check-in Date:", check_in)
print("Number of Nights:", nights)
print("Room Type:", room_type)
print("Price per Night:", price)
print("Total Amount:", total)
with open("hotel_bookings.txt", "a") as f:
    f.write(
        f"{name}, {phone}, {booking_id}, {check_in}, "
        f"{nights}, {room_type}, {price}, {total}\\n"
    )
print("Booking details saved successfully!")

