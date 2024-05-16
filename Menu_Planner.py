import calendar
import tabulate

def print_calendar(year, month, plans):
    print(calendar.month(year, month))
    for day in range(1, 32):  # Assumes up to 31 days in a month
        if day in plans:
            print(f"Day {day}: {plans[day]}")
def add_activities(plans, day, activity):
    

print("Calendar Planner_v1\nThis program aims to organize a meal and activities plan by month.")
y = 2024
m = int(input("type the month you would like to plan (1-12):"))
month_to_plan = calendar.month(y, m)
print(month_to_plan)

for days in month_to_plan:
    days