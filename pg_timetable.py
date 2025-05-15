from textwrap import indent

# Define the food timetable
FOOD_TIMETABLE = {
    "Monday": {
        "Breakfast": "Upma",
        "Lunch": "Bhindi ki sabji and Rice",
        "Dinner": "Rice, Dal, Sabji, Chapati"
    },
    "Tuesday": {
        "Breakfast": "Dosa",
        "Lunch": "Rice, Dal",
        "Dinner": "Rice, Sabji, Dal, Chapati"
    },
    "Wednesday": {
        "Breakfast": "Khichdi, Chhachh",
        "Lunch": "Rice, Sambar",
        "Dinner": "Fried Rice"
    },
    "Thursday": {
        "Breakfast": "Idly",
        "Lunch": "Rice, Sambar",
        "Dinner": "Rice, Sabji, Chapati"
    },
    "Friday": {
        "Breakfast": "Poha",
        "Lunch": "Sambar and Rice",
        "Dinner": "Rice, Sabji, Chapati"
    },
    "Saturday": {
        "Breakfast": "Sabji, Chapati",
        "Lunch": "Fried Rice",
        "Dinner": "Coconut Fried Rice"
    },
    "Sunday": {
        "Breakfast": "None",
        "Lunch": "Rice and Paneer",
        "Dinner": "Fried Rice"
    }
}

def format_day_name(day_name):
    return day_name.strip().capitalize()

def show_meals_for_day(day):
    """Display meals for a specific day."""
    day = format_day_name(day)
    meals = FOOD_TIMETABLE.get(day)

    if meals:
        print(f"\n🍽️  {day}'s Meal Plan:")
        for meal, food in meals.items():
            print(f"  {meal:<9}: {food}")
    else:
        print("❌ Invalid day. Please enter a correct weekday (e.g., Monday).")

def show_full_timetable():
    """Display the entire weekly food timetable."""
    print("\n📅 Full Week Food Timetable:")
    for day, meals in FOOD_TIMETABLE.items():
        print(f"\n{day}:")
        for meal, food in meals.items():
            print(f"  {meal:<9}: {food}")

def menu():
    """Interactive menu for user."""
    while True:
        print("\n========== Food Timetable Menu ==========")
        print("1️⃣  Show food for a specific day")
        print("2️⃣  Show full weekly timetable")
        print("3️⃣  Exit")
        print("=========================================")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            day = input("Enter the day: ")
            show_meals_for_day(day)
        elif choice == "2":
            show_full_timetable()
        elif choice == "3":
            print("👋 Exiting the program. Stay healthy!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    menu()
