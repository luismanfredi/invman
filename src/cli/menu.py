from src.utils.formatting import separator
from src.services.product_service import  register_product, show_products


still_working = [...]

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
		"1. Register Product\n"
		"2. Register Purchase\n" 
		"3. Register Sale\n"
		"4. Show Inventory\n"
		"5. Report\n"
		"6. Config")
		separator()
		users_choice = input("Enter your choice: ").strip().lower()
		separator()

		while users_choice in still_working:
			print("working on this... you can add a product only rn...")
			separator()
			break
		while users_choice == "1":
			register_product()
			separator()
			break
		while users_choice == "4":
			print("This is your inventory!")
			separator()
			show_products()
			separator()
			break
		if users_choice == "q" or users_choice == "quit":
			break
		
		continue