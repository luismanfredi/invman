from src.utils.formatting import separator
from src.database.connection import show_products
from src.services.inventory_service import create_product

still_working = ["2", "3", "4", "5"]

def menu():
	separator()
	print(
	"Welcome to the InvMan 👓!")
	separator()
	print(
	"The  Inventory Manager Software that\n"
	"will help you manage your items!\n"
	"(Use 'Q'; 'q' or 'quit' to quit)\n")
	while True:
		print("What option would you like to use?")
		separator()
		print(
		"1. Add product\n"
		"(Options below are not ready to use)\n"
		"2. Register sale\n" 
		"3. Remove item\n"
		"4. Report\n"
		"5. Config")
		separator()
		users_choice = input("Enter your choice: ").strip().lower()
		separator()

		while users_choice in still_working:
			print("working on this... you can add a product only rn...")
			separator()
			users_choice = input("Enter your choice: ")
		while users_choice == "1":
			create_product()
			separator()
			show_products()
			separator()
			break
		if users_choice == "q" or users_choice == "quit":
			break
		
		continue