import csv #this is for the csv file jaha i am storing the data

from datetime import datetime #this is for the date and time

def show_menu():
    print("\n===Personal Expense Tracker===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Show Summary")
    print("5. Exit")
    print("=============================")
# this part shows the menu of the expenses tracker

def add_expense():
    amount = input("Enter the amount:  ")
    category = input("Enter the category (food, travel, entertainment, etc):  ")
    description = input("Enter a description:  ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
        print("Expense added successfully!")
# this above part of code is for the adding of the expenses
def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            print("\nDate     | Amount  |  Category  |  Description")
            print("------------------------------------------------")
            for row in reader:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
                
    except FileNotFoundError:
        print("No expenses found.")
        # this above part of code is for the viewing of the expenses
        
def delete_expenses():
    try:
        with open("expenses.csv","r") as file:
            expenses = list(csv.reader(file))

        for index, row in enumerate(expenses):
            print(f"{index+1}. {row}")

        index = int(input("Enter the number to delete: "))-1
        if index < len(expenses):
            delete = expenses.pop(index)
            with open ("expenses.csv","w",newline="") as file:
                writer = csv.writer(file)
                writer.writerows(expenses)
                print(f"Expense '{delete}' deleted successfully!")
        else:
            print("Invalid number.")
    except:
        print("No expenses found.")
        # this above part of code is for the deleting of the expenses
            

def summary():
    summ ={}
    try:
        with open ("expenses.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[2]
                amount = float(row[1])
                summ[category]= summ.get(category,0) + amount
                # this above part of code is for the summary of the expenses
        print("\n______Expense Summary______")
        for category, amount in summ.items():
            print(f"{category} : {amount}")
    except:
        print("No expenses found.")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expenses()
    elif choice == "4":
        summary()             # this above part of code is for the menu of the expenses tracker
    elif choice == "5":
        print("Exiting the program...")
        break    
    else:
        print("Invalid choice. Please try again.")
        
