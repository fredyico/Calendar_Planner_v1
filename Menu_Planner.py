import calendar
import json
from tabulate import tabulate

def create_calendar_table(year, month, plans):
    # Get a matrix representing a month's calendar
    cal_matrix = calendar.monthcalendar(year, month)
    print(f"Calendar for {month}/{year}")

    # Modify the calendar matrix to include activities
    for i, week in enumerate(cal_matrix):
        for j, day in enumerate(week):
            if day != 0:
                # Check if there are activities for this day and append them
                if day in plans:
                    activities_str = '\n'.join(plans[day])
                    cal_matrix[i][j] = f"{day}\n{activities_str}"
                else:
                    cal_matrix[i][j] = str(day)
            else:
                cal_matrix[i][j] = ''

    # Print the calendar using tabulate
    print(tabulate(cal_matrix, headers=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']))
    
#year = 2024
plans = {}

def add_activity(list_of_days, activity):    
    for day in list_of_days:
        if day in plans:
            plans[int(day)].append(activity)  # Append to existing list if day already has activities
        else:
            plans[int(day)] = [activity]  # Create new list for new days

def remove_activity(day, activity):
    if day in plans and activity in plans[day]:
        plans[int(day)].remove(activity)
        if not plans[int(day)]:  # If the list is empty, remove the day from plans
            del plans[int(day)]
            
def save_plans_to_file(plans, filename, month, year):
    data_to_save = {'plans': plans, 'month': month, 'year': year}
    with open(filename+'.json', 'w') as file:
        json.dump(data_to_save, file)

def load_plans_from_file(filename):
    try:
        with open(filename+'.json', 'r') as file:
            data = json.load(file)
            if 'plans' in data and 'month' in data and 'year' in data:
                # Convert keys to integers
                plans = {int(k): v for k, v in data['plans'].items()}
                month = int(data['month'])
                year = int(data['year'])
                return plans, month, year
            else:
                raise ValueError("File is missing required data")
    except FileNotFoundError:
        print("File not found. Starting with an empty plan.")
    except (json.JSONDecodeError, ValueError, IOError) as e:
        print(f"Error reading the file: {e}")
    return {}, None, None

def main():
    print("This is the month planner. You can add meals or activities by selecting the month and days, then adding the activities to each day.")
    global plans  # This will allow us to modify the global variable 'plans'
    correct_month = False
    month = None  # Initialize month here
    year = None
    load_file = None
    try:
        load_file = input("Do you have a file to load (yes/no)? ").lower().strip()
        while load_file not in ['yes', 'no']:
            load_file = input("Value not accepted. Only 'yes' or 'no'. Do you have a file to load (yes/no)?").lower().strip()
    except ValueError:
        print("'yes' or 'no' only accepted. Try again.")
    if load_file == 'yes':
        filename = input("Enter the filename: ")
        loaded_plans, loaded_month, loaded_year = load_plans_from_file(filename)
        plans.update(loaded_plans)
        month = loaded_month
        year = loaded_year
        print(f"Loaded plans: {plans}")
        print(f"Loaded month: {month}")
        print(f"Loaded year: {year}")
        
    if not month or not year or load_file == 'no':  # Ensure month and year are always set
        while not correct_month:
            try:
                month = int(input("Type the month you would like to plan (1-12): "))
                year = int(input("Type the year you would like to plan (yyyy): "))
                if 1 <= month <= 12:
                    correct_month = True
                else:
                    print("Month must be an integer from 1 to 12. Try again.")
            except ValueError:
                print("Invalid input. Please enter valid integers for month and year.")
    
    while True:
        print("\nMenu:")
        print("1. Add activities")
        print("2. Remove activities")
        print("3. Print calendar")
        print("4. Save the calendar")
        print("5. Exit")
        try:
            option = int(input("Select an option: "))
            if option < 1 or option > 5:
                raise ValueError("Please enter a number from 1 to 5.")
        except ValueError as e:
            print(f"Invalid input. {e}")
            continue
        
        if option == 1:
            try:
                days_list = list(map(int, input("Select the days to add activities, with comma separation (e.g., 1,2,3): ").replace(' ', '').split(",")))
                activity = input("Enter the activity you would like to add for these days: ")
                add_activity(days_list, activity)
                print("Activities added successfully.")
            except ValueError:
                print("Invalid input. Please enter valid day numbers.")
        elif option == 2:
            try:
                day = int(input("Enter the day to remove an activity from: "))
                activity = input("Enter the activity to remove: ")
                remove_activity(day, activity)
                print("Activity removed successfully.")
            except ValueError:
                print("Invalid input. Please enter a valid day number.")
        elif option == 3:
            print(f"Current plans: {plans}")
            print(f"Month: {month}, Year: {year}")
            create_calendar_table(year, month, plans)
        elif option == 4:
            name_of_the_file = input("Type the filename to be saved:\n")
            save_plans_to_file(plans, name_of_the_file, month, year)
            print(f"Plans saved to {name_of_the_file}.json successfully!")
        elif option == 5:
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()