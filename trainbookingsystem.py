from random import randint, choice

class Train:
    def __init__(self, trainNo, seats=5):
        self.trainNo = trainNo
        self.seats = seats
        self.booked_tickets = []

    def book(self, passenger, fro, to):
        if self.seats > 0:
            ticket_id = randint(1000, 9999)
            self.booked_tickets.append({
                "ticket_id": ticket_id,
                "passenger": passenger,
                "from": fro,
                "to": to
            })
            self.seats -= 1
            print(f"\n✅ Ticket booked: ID {ticket_id}, Train {self.trainNo}, {passenger} from {fro} to {to}")
        else:
            print("\n❌ No seats available!")

    def cancel(self, ticket_id):
        for ticket in self.booked_tickets:
            if ticket["ticket_id"] == ticket_id:
                self.booked_tickets.remove(ticket)
                self.seats += 1
                print(f"\n🛑 Ticket {ticket_id} cancelled successfully.")
                return
        print("\n❌ Ticket not found!")

    def getStatus(self):
        status = choice(["On Time", "Delayed", "Cancelled"])
        print(f"\n🚂 Train {self.trainNo} is {status}")

    def getFare(self, fro, to):
        distance = randint(50, 500)  # km
        fare = distance * 5  # ₹5 per km
        print(f"\n💰 Fare from {fro} to {to} in Train {self.trainNo}: ₹{fare}")

    def showBookings(self):
        if not self.booked_tickets:
            print("\n📭 No tickets booked yet.")
        else:
            print("\n📃 Booked Tickets:")
            for ticket in self.booked_tickets:
                print(ticket)


# -------- Menu Driven Program --------
def main():
    t = Train(12345, seats=5)

    while True:
        print("\n--- Train Booking System ---")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Check Train Status")
        print("4. Check Fare")
        print("5. Show All Bookings")
        print("6. Exit")

        choice_input = input("Enter your choice: ")

        if choice_input == "1":
            passenger = input("Enter passenger name: ")
            fro = input("From: ")
            to = input("To: ")
            t.book(passenger, fro, to)

        elif choice_input == "2":
            try:
                ticket_id = int(input("Enter ticket ID to cancel: "))
                t.cancel(ticket_id)
            except ValueError:
                print("❌ Invalid ticket ID!")

        elif choice_input == "3":
            t.getStatus()

        elif choice_input == "4":
            fro = input("From: ")
            to = input("To: ")
            t.getFare(fro, to)

        elif choice_input == "5":
            t.showBookings()

        elif choice_input == "6":
            print("👋 Exiting Train Booking System. Thank you!")
            break

        else:
            print("❌ Invalid choice, try again.")


# Run the program
if __name__ == "__main__":
    main()
