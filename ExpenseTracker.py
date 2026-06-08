def add_expense():
    print("Example - DD/MM/YY")
    date = input("Enter date: ")
    amount = input("Enter amount: ")
    print("Options - Food/Transport/Entertainment/Others")
    category = input("Enter category: ")
    choice_for_note = input("Would you like to write a Note? (y/n): ")
    if choice_for_note.lower() == "y":
        note = input("Enter note: ")
    else:
        note = "N/A"

    with open("data.txt", "a") as file:
        file.write(f"{date},{category},{amount},{note}\n")
    
def view_All_expenses():
    total = 0

    print(f"{'Date':<12}{'Category':<13}{'Amount':<10}{'Note'}")
    print("-" * 50)

    with open("data.txt", "r") as file:
        for line in file:
            date, category, amount, note = line.strip().split(",")

            print(f"{date:<12}{category:<13}{amount:<10}{note}")

            total += float(amount)

    print("-" * 50)
    print("Total =", total)

def filter_by_category():
    search = input("Enter category: ")
    subtotal = 0

    print(f"{'Date':<12}{'Category':<13}{'Amount':<10}{'Note'}")
    print("-" * 50)

    with open("data.txt" , "r") as file:
        for line in file:
            date, category, amount, note = line.strip().split(",")

            if category.lower() == search.lower():
                print(f"{date:<12}{category:<13}{amount:<10}{note}")
                subtotal += float(amount)

    print("-" * 50)
    print("Subtotal =", subtotal)

while True:
    print("\n1. Add an Expense")
    print("2. View All Expenses")
    print("3. Filter by Category")
    print("4. Exit")

    User_Input = input("input: ")

    if User_Input == "1":
        add_expense()
    elif User_Input == "2":
        view_All_expenses()
    elif User_Input == "3":
        filter_by_category()
    elif User_Input == "4":
        print("Thanks For Visiting!")
        break
    else : print("Invalid Option")
    
