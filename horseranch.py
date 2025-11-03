import os
import datetime
from docx import Document

horses = []
boarders = []
barn = []

def users():
    print(".")

def clear_screen():
    """Clear the terminal screen (works on Windows, Linux, Mac)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def new_boarder():
    print("New boarder\n")
    print("Fill the following fields:")

    first_name = input("\nEnter your first name: ")[:10]
    last_name = input("\nEnter your last name: ")[:10]
    phone_number = input("\nEnter your phone number without spaces: ")[:10]
    address = input("\nEnter your full address: ")
    emergency_contact = input("\nEnter full name emergency contact: ")[:13]
    emergency_contact_phone_number = input("\nEnter phone number from emergency contact: ")[:10]

def new_horse():
    print("New horse is going to be added\n")
    while True:
        try:
            horse_name = input("Enter horse first name: ").strip()
            date = input("Enter horse birth date in YYYY-MM-DD format: ").strip()
            date_horse = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            breed = input("Enter horse breed: ").strip()
            breakfast = input("Enter horse breakfast hay: ").strip()
            lunch = input("Enter horse lunch hay: ").strip()
            dinner = input("Enter horse dinner hay: ").strip()
            allergies = [a.strip().lower() for a in input("Enter horse allergies separated by commas: ").split(",") if a.strip()]
            break  # only runs if no ValueError
        except ValueError:
            print("Invalid format. Please try again.\n")
    horse = {
        "name": horse_name,
        "birth_date": date_horse,
        "breed": breed,
        "breakfast_hay": breakfast,
        "lunch_hay": lunch,
        "dinner_hay": dinner,
        "allergies": allergies
    }
    horses.append(horse)
    print(f"\nHorse '{horse_name}' added successfully!")


def view_horse():
    print("\nView horse\n"
          "1. Print all horses\n"
          "2. Print a specific horse\n"
          "3. Go back to menu\n")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                if not horses:
                    print("\nNo horses registered yet.\n")
                else:
                    # Display horses on screen
                    for x in horses:
                        print(f"\nName: {x['name']}")
                        print(f"Breed: {x['breed']}")
                        print(f"Barn: {x['barn']}, Stall: {x['stall']}")
                        print(f"Birthdate: {x['birth_date']}")
                        print(f"Breakfast hay: {x['breakfast_hay']}")
                        print(f"Lunch: {x['lunch_hay']}")
                        print(f"Dinner: {x['dinner_hay']}")
                        print(f"Allergies: {', '.join(x['allergies']) if x['allergies'] else 'None'}")
                        print("-" * 40)

                    # Ask user if they want to export
                    export = input(
                        "\nWould you like to export the list of all horses to a .docx file? (y/n): ").strip().lower()
                    if export == 'y':
                        doc = Document()
                        today = datetime.date.today().strftime("%Y-%m-%d")
                        doc.add_heading(f"Horse List – Generated on {today}", level=1)
                        for x in horses:
                            doc.add_paragraph(f"Name: {x['name']}")
                            doc.add_paragraph(f"Breed: {x['breed']}")
                            doc.add_paragraph(f"Barn: {x['barn']}, Stall: {x['stall']}")
                            doc.add_paragraph(f"Birthdate: {x['birth_date']}")
                            doc.add_paragraph(f"Breakfast hay: {x['breakfast_hay']}")
                            doc.add_paragraph(f"Lunch: {x['lunch_hay']}")
                            doc.add_paragraph(f"Dinner: {x['dinner_hay']}")
                            doc.add_paragraph(f"Allergies: {', '.join(x['allergies']) if x['allergies'] else 'None'}")
                            doc.add_paragraph("-" * 40)
                        doc.save("horse_list.docx")
                        print("\nHorse list successfully exported to 'horse_list.docx'.")
                    else:
                        print("\nExport skipped.")
            elif choice == 2:
                name = input("Enter horse name: ").strip().lower()
                found = False
                for x in horses:
                    if name == x['name'].lower():
                        print(f"\nName: {x['name']}")
                        print(f"Birthdate: {x['birth_date']}")
                        print(f"Breed: {x['breed']}")
                        print(f"Barn: {x['barn']}, Stall: {x['stall']}")
                        print(f"Breakfast hay: {x['breakfast_hay']}")
                        print(f"Lunch: {x['lunch_hay']}")
                        print(f"Dinner: {x['dinner_hay']}")
                        print(f"Allergies: {', '.join(x['allergies']) if x['allergies'] else 'None'}")
                        print("-" * 40)
                        found = True
                        break
                if not found:
                    print("\nHorse hasn't been found.\n")
            elif choice == 3:
                return
            else:
                print("\nInvalid choice. Please select 1–3.\n")
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")

def barn_management():
    print("Barn management\n")
    print("1. Add a barn.")
    print("2. View a barn.")
    print("3. Search for empty stalls.")
    print("4. Remove a barn.")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_barn() # Add a barn.
            elif choice == 2:
                view_barn() # View horses inside a barn.
            elif choice == 3:
                search_empty_stalls() # Search for empty stalls.
            elif choice == 4:
                remove_barn() # Remove a specific barn.
                print("Remove a barn.")
            else:
                print("\nInvalid input. Please enter a number.\n")
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")

def add_barn():
    print("Add a barn.")

def view_barn():
    print("View a barn.")

def search_empty_stalls():
    print("Search for empty stalls.")

def remove_barn():
    print("Remove a barn.")

def search_horse():
    print("Search horse")

def view_current_stalls():
    print("Current stalls:")

def main():
    print("H")

if __name__ == "__main__":
    view_horse()
