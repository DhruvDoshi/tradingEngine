from modules.session import Session

def print_menu():
    print("\n" + "="*30)
    print("Main Menu:")
    print("1. Test Function")
    print("14. Logout")
    print("="*30)

def main():
    session = Session()
    if session.login():
        while True:
            print_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                print("\nSelected profile 1...")
            elif choice == '14':
                if session.logout():
                    break
            else:
                print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()

