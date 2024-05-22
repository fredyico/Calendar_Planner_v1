import calendar
import json
from tabulate import tabulate

def create_calendar_table(year, month, plans):
    # Get a matrix representing a month's calendar
    cal_matrix = calendar.monthcalendar(year, month)

    # Modify the calendar matrix to include activities
    for i, week in enumerate(cal_matrix):
        for j, day in enumerate(week):
            if day != 0:
                # If there are activities planned for this day, append them to the day's cell
                if day in plans:
                    activities_str = '\n'.join(plans[day])  # Join all activities with a newline
                    cal_matrix[i][j] = f"{day}\n{activities_str}"
                else:
                    cal_matrix[i][j] = str(day)
            else:
                # Replace '0' days (padding days) with empty spaces
                cal_matrix[i][j] = ''

    # Print the calendar using tabulate
    print(tabulate(cal_matrix, headers=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']))

# Main program
year = 2024
plans = {}

def add_activity(list_of_days, activity):    
    for day in list_of_days:
        if day in plans:
            plans[day].append(activity)  # Append to existing list if day already has activities
        else:
            plans[day] = [activity]  # Create new list for new days

def remove_activity(day, activity):
    if day in plans and activity in plans[day]:
        plans[day].remove(activity)
        if not plans[day]:  # If the list is empty, remove the day from plans
            del plans[day]
            
def save_plans_to_file(plans, filename):
    with open(filename+'.json', 'w') as file:
        json.dump(plans, file)

def load_plans_from_file(filename):
    try:
        with open(filename+'.json', 'r') as file:
            plans = json.load(file)
            return plans
    except FileNotFoundError:
        print("File not found. Starting with an empty plan.")
        return {}

def main():
    print("This is the month planner. You can add meals or activities by selecting the month and days, then adding the activities to each day.")
    global plans  # This will allow us to modify the global variable 'plans'
    correct_month = False
    
    if input("Do you have a file to load (yes/no)? ") == 'yes':
        filename = input("Enter the filename: ")
        plans = load_plans_from_file(filename)  # Make sure to update the global plans
        
    load_or_not = input("Do you have a file to load and continue to plan there? Enter '1' to load or '2' for a new file: ")
    if load_or_not ==  '1':
        to_load = input("Type here the name of your file, as it is: ")
        plans = load_plans_from_file(to_load)        
    elif load_or_not == '2':        
        while not correct_month:
            try:
                month = int(input("type the month you would like to plan (1-12): "))
                if 1 <= month <= 12:
                    correct_month = True
                else:
                    print("Month must be an integer from 1 to 12. Try again.")
            except ValueError:
                print("Invalid input. Only integers from 1 to 12 are allowed. Try again.")
    while True:
        print("\nMenu:")
        print("1. Add activities")
        print("2. Remove activities")
        print("3. Print calendar")
        print("4. Save a calendar")
        print("5. Exit")
        try:
            option = int(input("Select an option: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue
        if option == 1:
            try:
                days_list = list(map(int, input("Select the days to add activities, with comma separation (e.g., 1,2,3): ").replace(' ', '').split(",")))
                meal = input("Enter the activity you would like to add for these days: ")
                add_activity(days_list, meal)
            except ValueError:
                print("Invalid input. Please enter valid day numbers.")
        elif option == 2:
            try:
                day = int(input("Enter the day to remove an activity from: "))
                activity = input("Enter the activity to remove: ")
                remove_activity(day, activity)
            except ValueError:
                print("Invalid input. Please enter a valid day number.")
        elif option == 3:
            create_calendar_table(year, month, plans)
        elif option == 4:
            name_of_the_file = input("Type the filename to be saved:\n")
            save_plans_to_file(plans, name_of_the_file)            
        elif option == 5:
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()