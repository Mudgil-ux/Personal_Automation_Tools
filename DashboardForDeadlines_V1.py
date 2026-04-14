from datetime import datetime

print("--- Deadline Dashboard ---")
print("Helpful for students, professionals, and any busy person!")

user_deadlines = []

while True:
    p = input(" Enter Project/Task name (or 'done' to see dashboard): ")
    if p.lower() == 'done': break
    
    date_str = input("Enter deadline (YYYY-MM-DD): ")
    try:
        # Converting the string input into a real date
        deadline_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        user_deadlines.append({"task": p, "date": deadline_date})
    except ValueError:
        print("❌ Invalid format! Please use YYYY-MM-DD (e.g., 2026-04-20).")

print("\n" + "="*40)
print("       YOUR UPCOMING DEADLINES        ")
print("="*40)

today = datetime.now().date()

for item in user_deadlines:
    days_left = (item['date'] - today).days
    
    if days_left < 0:
        status = "PASSED ❌"
    elif days_left <= 2:
        status = "URGENT 🔥"
    else:
        status = "On Track ✅"
        
    print(f"{item['task']} | {item['date']} | {days_left} days left [{status}]")

print("="*40)
