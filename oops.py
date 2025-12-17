# # 1.Create a Student class with name, roll, and marks; add method to compute average.

# def read_marks(subject_names):
#     marks = {}
#     for name in subject_names:
#         while True:
#             try:
#                 value = float(input(f"Enter marks for {name} (0-100): ").strip())
#                 if 0 <= value <= 100:
#                     marks[name] = value
#                     break
#                 print("Please enter a number between 0 and 100.")
#             except ValueError:
#                 print("Invalid number. Try again.")
#     return marks

# def compute_grade(average):
#     if average >= 90:
#         return "A"
#     elif average >= 80:
#         return "B"
#     elif average >= 70:
#         return "C"
#     elif average >= 60:
#         return "D"
#     else:
#         return "F"

# def main():
#     subject_names = ["Maths", "Science", "English", "History", "Computer"]
#     marks = read_marks(subject_names)

#     total = sum(marks.values())
#     average = total / len(marks)

#     grade = compute_grade(average)

#     all_pass = all(m >= 35 for m in marks.values())
#     distinction = average >= 75 and all(m >= 60 for m in marks.values())
#     needs_improvement = (not all_pass) or grade == "F"

#     if grade in ("A", "B"):
#         remark = "Excellent" if distinction else "Good"
#     elif grade in ("C", "D"):
#         remark = "Satisfactory" if all_pass else "Needs Improvement"
#     else:
#         remark = "Fail"

#     print("\n===== Result =====")
#     for name in subject_names:
#         print(f"{name}: {marks[name]:.2f}")
#     print(f"Total: {total:.2f}")
#     print(f"Average: {average:.2f}")
#     print(f"Grade: {grade}")
#     print("Status: At Risk" if needs_improvement else "Status: On Track")
#     print(f"Remark: {remark}")

# if __name__ == "__main__":

#     main()
#     print("Evaluation completed.")


# 2.Create a BankAccount class with deposit, withdraw, and balance check.

def main():
    bal = 0.0
    while True:
        try:
            ch = input("\n1) Deposit  2)  Check BalWithdraw  3)ance  4) Exit\nChoose: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye."); break

        if ch == "1":
            try:
                amt = float(input("Deposit amount: "))
            except ValueError:
                print("Invalid amount."); continue 
            if amt <= 100000:
                print("Enter a positive amount."); continue
            bal += amt; print(f"Deposited {amt:.2f}. Balance: {bal:.2f}")

        elif ch == "2":
            try:
                amt = float(input("Withdraw amount: "))
            except ValueError:
                print("Invalid amount."); continue
            if amt <= 0:
                print("Enter a positive amount."); continue
            if amt > bal:
                print("Insufficient funds. Skipping."); continue
            bal -= amt; print(f"Withdrew {amt:.2f}. Balance: {bal:.2f}")

        elif ch == "3":
            print(f"Balance: {bal:.2f}")

        elif ch == "4":
            print("Goodbye."); break


if __name__ == "__main__":
    main()
    print("ATM session ended.")



# # 3.Create a Car class with brand, model, and a drive() method.

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def drive(self):
#         print(f"The {self.brand} {self.model} is now driving!")

# car1 = Car("BMW", "X5")
# car1.drive()


# # 4.Create a Restaurant class that stores menu items in a dictionary and prints the bill.
# class Restaurant:
#     def __init__(self):
#         self.menu = {"Burger": 50, "Pizza": 100, "Pasta": 80, "Coffee": 30}
#         self.order = {}
    
#     def add_item(self, item, qty=1):
#         if item in self.menu:
#             self.order[item] = self.order.get(item, 0) + qty
    
#     def print_bill(self):
#         total = 0
#         print("\n----- Bill -----")
#         for item, qty in self.order.items():
#             cost = self.menu[item] * qty
#             print(f"{item} x{qty}: ₹{cost}")
#             total += cost
#         print(f"Total: ₹{total}")

# # Example
# r = Restaurant()
# r.add_item("Burger", 2)
# r.add_item("Pizza")
# r.print_bill()


# # 5.Create a User class with private password and a method to validate login.

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password  # private
    
#     def validate_login(self, password):
#         return self.__password == password

# Example
# user = User("ankit", "secret123")
# print(user.validate_login("secret123"))  # True
# print(user.validate_login("wrong"))      # False