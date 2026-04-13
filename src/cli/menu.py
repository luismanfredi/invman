from src.utils.formatting import separator
from src.services.sale_service import make_sale, show_sales
from src.services.purchase_service import make_purchase, show_purchases
from src.services.product_service import register_product, show_products

still_working = ["5", "6"]


def menu():
    separator()
    print("Welcome to the InvMan 👓!")
    separator()
    print("The Inventory Manager Software that\n" "will help you manage your items!\n")
    while True:
        print("What option would you like to use?")
        separator()
        print(
            "1. Products\n"
            "2. Purchases\n"
            "3. Sales\n"
            "4. Inventory\n"
            "5. 🚧 Report\n"
            "6. 🚧 Config\n"
            "7. Exit"
        )

        separator()
        menu_option = input("Enter your choice: ").strip()
        separator()

        if menu_option in still_working:
            print("🚧 Still Working!! 🚧")
            separator()
            continue
        elif menu_option == "1":
            product_menu()
            continue
        elif menu_option == "2":
            purchase_menu()
            continue
        elif menu_option == "3":
            sale_menu()
            continue
        elif menu_option == "4":
            print("This is your inventory!")
            separator()
            show_products()
            separator()
            continue
        elif menu_option == "7":
            break
        else:
            print(f"{menu_option} is not a valid option. Try again!")
            continue


def product_menu():
    print("Product options:\n" "1. Register Product\n" "2. Exit")
    separator()
    product_option = input("Enter your choice: ").strip()
    if product_option == "1":
        register_product()
    elif product_option == "2":
        pass
    else:
        print(f"{product_option} is not a valid option. Try again!")

    separator()


def purchase_menu():
    print(
        "Purchase options:\n" "1. Register Purchase\n" "2. Show Purchases\n" "3. Exit"
    )
    separator()
    purchase_option = input("Enter your choice: ").strip()
    if purchase_option == "1":
        make_purchase()
    elif purchase_option == "2":
        show_purchases()
    elif purchase_option == "3":
        pass
    else:
        print(f"{purchase_option} is not a valid option. Try again!")

    separator()


def sale_menu():
    print("Sale options:\n" "1. Register Sale\n" "2. Show Sales\n" "3. Exit")
    separator()
    sale_option = input("Enter your choice: ").strip()
    if sale_option == "1":
        make_sale()
    elif sale_option == "2":
        show_sales()
    elif sale_option == "3":
        pass
    else:
        print(f"{sale_option} is not a valid option. Try again!")

    separator()
