seasonal_flavors = []
ingredients = []
customer_suggestions = []
def add_flavor(flavor, season):
    seasonal_flavors.append({"flavor": flavor, "season": season})
    print(f"Added flavor: {flavor} for season: {season}")
def add_ingredient(ingredient, quantity):
    ingredients.append({"ingredient": ingredient, "quantity": quantity})
    print(f"Added ingredient: {ingredient} with quantity: {quantity}")
def add_suggestion(name, suggestion, allergy):
    customer_suggestions.append({"name": name, "suggestion": suggestion, "allergy": allergy})
    print(f"Added customer suggestion from {name} with suggestion: {suggestion} and allergy concern: {allergy}")
def view_data(data, title):
    print(f"\n{title}:")
    if not data:
        print("No entries found.")
    for entry in data:
        print(entry)
def main():
    while True:
        print("\n1. Add Seasonal Flavor\n2. Add Ingredient\n3. Add Customer Suggestion\n4. View Seasonal Flavors\n5. View Ingredients\n6. View Customer Suggestions\n7. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            flavor = input("Enter flavor name: ")
            season = input("Enter season: ")
            add_flavor(flavor, season)
        elif choice == '2':
            ingredient = input("Enter ingredient name: ")
            quantity = input("Enter quantity: ")
            add_ingredient(ingredient, quantity)
        elif choice == '3':
            name = input("Enter your name: ")
            suggestion = input("Enter your flavor suggestion: ")
            allergy = input("Enter any allergy concerns: ")
            add_suggestion(name, suggestion, allergy)
        elif choice == '4':
            view_data(seasonal_flavors, "Seasonal Flavors")
        elif choice == '5':
            view_data(ingredients, "Ingredients")
        elif choice == '6':
            view_data(customer_suggestions, "Customer Suggestions")
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
