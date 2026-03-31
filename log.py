import datetime

'''
Create a file for a basic log that saves the date/time and log to a txt file
'''
def show_menu():
    choice = int(input("\nWhat would you like to do?\n1: Review log.\n2: Submit an entry.\n3: Clear log.\n4: Exit program.\nEnter choice here: "))
    return choice

# Choice #1
def view_log():
    with open('log.txt', 'r') as file:
        for line in file:
            print(line.strip())
    log_options()

# Choice #2
def make_entry():
    with open('log.txt', 'a') as file:
        entry = input("Enter log here: ")
        timestamp = datetime.datetime.now().replace(microsecond=0)
        file.write(f'[{timestamp}] {entry}\n')
    print("Entry logged.")
    log_options()

# Choice #3
def clear_log():
    open('log.txt', 'w').close()
    log_options()

def log_options ():
    choice = show_menu()
    if choice == 1:
        view_log()
    elif choice == 2:
        make_entry()
    elif choice == 3:
        clear_log()
    elif choice == 4:
        print("\nYou have exited the program.")
        return

print("Welcome to your log!")
log_options()