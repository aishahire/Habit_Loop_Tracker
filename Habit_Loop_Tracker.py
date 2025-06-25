
# Task 3: Create a console application for basic CRUD operations on a list of tasks.
# 🧠 Habit Loop Tracker Console App

class Habit:
    def __init__(self, id, cue, routine, reward, frequency):
        self.id = id
        self.cue = cue
        self.routine = routine
        self.reward = reward
        self.frequency = frequency

    def display(self):
        print(f"{self.id:<4} | {self.cue:<10} | {self.routine:<12} | {self.reward:<10} | {self.frequency:<8}")


# 🌟 Storage
habits = []
next_id = 1


# ➕ Create
def add_habit():
    global next_id
    print("\n-- Add New Habit --")
    cue = input("Enter Cue (trigger): ")
    routine = input("Enter Routine (habit): ")
    reward = input("Enter Reward: ")
    frequency = input("Enter Frequency (daily/weekly/etc): ")
    habits.append(Habit(next_id, cue, routine, reward, frequency))
    print(f"✅ Habit ID {next_id} added!")
    next_id += 1


# 📖 Read
def view_habits():
    if not habits:
        print("\n⚠️ No habits found.")
        return
    print("\n-- All Habit Loops --")
    print("ID   | Cue        | Routine      | Reward     | Frequency")
    print("-------------------------------------------------------------")
    for h in habits:
        h.display()


# ✏️ Update
def update_habit():
    view_habits()
    try:
        uid = int(input("\nEnter ID of the habit to update: "))
        for h in habits:
            if h.id == uid:
                h.cue = input("New Cue: ")
                h.routine = input("New Routine: ")
                h.reward = input("New Reward: ")
                h.frequency = input("New Frequency: ")
                print("✅ Habit updated successfully.")
                return
        print("❌ Habit ID not found.")
    except ValueError:
        print("❌ Invalid input.")


# ❌ Delete
def delete_habit():
    view_habits()
    try:
        uid = int(input("\nEnter ID of the habit to delete: "))
        for h in habits:
            if h.id == uid:
                habits.remove(h)
                print(f"🗑️ Habit ID {uid} deleted.")
                return
        print("❌ Habit ID not found.")
    except ValueError:
        print("❌ Invalid input.")


# 🧭 Main Menu
def main():
    while True:
        print("\n====== 🧠 Habit Loop Tracker ======")
        print("1. Add New Habit")
        print("2. View All Habits")
        print("3. Update a Habit")
        print("4. Delete a Habit")
        print("5. Exit")
        choice = input("Choose an option (1–5): ")

        if choice == "1":
            add_habit()
        elif choice == "2":
            view_habits()
        elif choice == "3":
            update_habit()
        elif choice == "4":
            delete_habit()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    main()
