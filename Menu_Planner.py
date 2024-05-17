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

# Example usage
year = 2024
month = 4
plans = {
    3: ["Doctor's appointment"],
    12: ["Mom's birthday", "Brunch with family"],
    15: ["Team meeting", "Gym"],
    22: ["Dinner with friends"]
}

create_calendar_table(year, month, plans)