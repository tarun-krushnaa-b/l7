seasonal_flavors = []
ingredient_stock = []
customer_feedback = []
def insert_flavor(flavor, season):
    seasonal_flavors.append({"flavor": flavor, "season": season})
    print(f"New seasonal flavor '{flavor}' added for the {season} season.")
def insert_ingredient(name, amount):
    ingredient_stock.append({"ingredient": name, "quantity": amount})
    print(f"Added {amount} units of {name} to the inventory.")
def insert_suggestion(customer_name, suggested_flavor, allergies):
    customer_feedback.append({"name": customer_name, "suggestion": suggested_flavor, "allergy": allergies})
    print(f"Customer suggestion recorded from {customer_name}: Flavor suggestion - {suggested_flavor}, Allergies - {allergies}")
def display_data(data_list, title):
    print(f"\n{title}:")
    if not data_list:
        print("No data available.")
    else:
        for entry in data_list:
            print(entry)
def main_menu():
    while True:
        print("\n1. Add a New Seasonal Flavor")
        print("2. Add a New Ingredient to Inventory")
        print("3. Submit a Customer Suggestion")
        print("4. View Seasonal Flavors")
        print("5. View Ingredient Inventory")
        print("6. View Customer Feedback")
        print("7. Exit")
        user_choice = input("Please choose an option: ")
        if user_choice == '1':
            flavor_name = input("Enter the flavor name: ")
            season_name = input("Enter the season: ")
            insert_flavor(flavor_name, season_name)
        elif user_choice == '2':
            ingredient_name = input("Enter the ingredient name: ")
            ingredient_amount = input("Enter the quantity: ")
            insert_ingredient(ingredient_name, ingredient_amount)
        elif user_choice == '3':
            customer_name = input("Enter your name: ")
            flavor_suggestion = input("Enter your flavor suggestion: ")
            allergy_info = input("Enter any allergy concerns: ")
            insert_suggestion(customer_name, flavor_suggestion, allergy_info)
        elif user_choice == '4':
            display_data(seasonal_flavors, "List of Seasonal Flavors")
        elif user_choice == '5':
            display_data(ingredient_stock, "Current Ingredient Inventory")
        elif user_choice == '6':
            display_data(customer_feedback, "Customer Suggestions and Allergy Concerns")
        elif user_choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")
if __name__ == "__main__":
    main_menu()
