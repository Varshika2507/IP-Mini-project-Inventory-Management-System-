# INVENTORY MANAGEMENT SYSTEM

# Lists to store product details
ids = []
names = []
prices = []
quantities = []

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Sell Product")
    print("6. Delete Product")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add product
    if choice == "1":
        pid = input("Enter product ID: ")

        if pid in ids:
            print("Product ID already exists!")
        else:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            qty = int(input("Enter product quantity: "))

            ids.append(pid)
            names.append(name)
            prices.append(price)
            quantities.append(qty)

            print("Product added successfully!")

    # View products
    elif choice == "2":
        if len(ids) == 0:
            print("Inventory is empty.")
        else:
            print("\nID\tName\tPrice\tQuantity")

            for i in range(len(ids)):
                print(ids[i], "\t", names[i], "\t",
                      prices[i], "\t", quantities[i])

    # Search product
    elif choice == "3":
        pid = input("Enter product ID: ")

        if pid in ids:
            i = ids.index(pid)

            print("Product Name:", names[i])
            print("Price:", prices[i])
            print("Quantity:", quantities[i])
        else:
            print("Product not found!")

    # Update quantity
    elif choice == "4":
        pid = input("Enter product ID: ")

        if pid in ids:
            i = ids.index(pid)
            qty = int(input("Enter new quantity: "))

            if qty >= 0:
                quantities[i] = qty
                print("Quantity updated successfully!")
            else:
                print("Quantity cannot be negative.")
        else:
            print("Product not found!")

    # Sell product
    elif choice == "5":
        pid = input("Enter product ID: ")

        if pid in ids:
            i = ids.index(pid)
            qty = int(input("Enter quantity to sell: "))

            if qty > 0 and qty <= quantities[i]:
                quantities[i] = quantities[i] - qty
                bill = prices[i] * qty

                print("Sale successful!")
                print("Total bill: Rs.", bill)
                print("Remaining quantity:", quantities[i])
            else:
                print("Invalid quantity or insufficient stock!")
        else:
            print("Product not found!")

    # Delete product
    elif choice == "6":
        pid = input("Enter product ID: ")

        if pid in ids:
            i = ids.index(pid)

            ids.pop(i)
            names.pop(i)
            prices.pop(i)
            quantities.pop(i)

            print("Product deleted successfully!")
        else:
            print("Product not found!")

    # Exit
    elif choice == "7":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please try again.")
