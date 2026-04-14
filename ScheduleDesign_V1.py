print("--- Your Schedule Planner ---")
tasks = []

while True:
    task = input(" Enter task name (or 'done' if you are done adding your task for the day): ")
    if task.lower() == 'done': break
    
    time = input(f"What time for '{task}'? (e.g., 09:00 AM): ")
    tasks.append({"time": time, "task": task})

print(" GENERATING YOUR OPTIMIZED SCHEDULE...")
print("------------------------------------")
for item in tasks:
    print(f"[{item['time']}] -> {item['task']}")
print("------------------------------------")
