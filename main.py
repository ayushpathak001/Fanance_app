class Finance :

    def __init__(self):
        self.balance = 0.0 
        self.income = 0.0
        self.expenses = 0.0

    def view_balance(self):
        print(f"current balance :${self.balance :.2f}")

    def add_income(self):
        amount = float(input("Enter income amount :$"))
        self.income += amount
        self.balance  += amount
        print(f"income of ${amount :.2f} added.")
    
    def add_expense(self):
        amount = float(input("Enter expense amount : $"))

        self.expenses += amount
        self.balance += amount
        
        print(f"Expense of ${amount :.2f} added .")

    def view_expenses(self):
        print(f"Tota; expenses :${self.expenses :.2f}")

    def menu (self):
        while True :
            print("\nFnance App menu :")

            print("\n1. View Balance")

            print("\n2. Add income")

            print("\n3. Add Expense")

            print("\n4. View Expenses")

            print("\n5. Exit")

            choice = input("Enter an option :")

            if choice == "1":
                self.view_balance()
            elif choice == "2":
                self.add_income()
            elif choice== "3":
                self.add_expense()
            elif choice == "4":
                self.view_expenses()
            elif choice == "5":
                print("Exiting the application.")
                break
            else :
                print("Invalid choice. Please try again !")
        
if __name__ == "__main__":
    app = Finance()
    app.menu()

    
