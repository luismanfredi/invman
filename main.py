from src.cli.menu import menu
from src.database.connection import initialize_database

def main():
    initialize_database()
    menu()

if __name__ == "__main__":
    main()