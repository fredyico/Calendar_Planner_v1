import calendar
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

def main():
    print("This is the month planner. You can add meals or activities by selecting the month and days, then adding the activities to each day.")
    correct_month = False

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
        print("4. Exit")
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
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()





add_activity(days_list, meal)
create_calendar_table(year, month, plans)