import time
import json
from datetime import datetime, timedelta

class StudyApp:
    def __init__(self):
        self.tasks = []
        self.achievements = {}
        self.load_data()

    def load_data(self):
        try:
            with open('study_data.json', 'r') as f:
                data = json.load(f)
                self.tasks = data.get('tasks', [])
                self.achievements = data.get('achievements', {})
        except FileNotFoundError:
            self.tasks = []
            self.achievements = {}

    def save_data(self):
        with open('study_data.json', 'w') as f:
            json.dump({'tasks': self.tasks, 'achievements': self.achievements}, f)

    def add_task(self, chapter, revision_time):
        self.tasks.append({
            'chapter': chapter,
            'revision_time': datetime.now() + timedelta(days=revision_time),
            'completed': False
        })
        print(f"Task added: {chapter}. You need to revise it in {revision_time} days.")
        self.save_data()

    def complete_task(self, chapter):
        for task in self.tasks:
            if task['chapter'] == chapter and not task['completed']:
                task['completed'] = True
                self.gain_achievement(chapter)
                print(f"Task completed: {chapter}. Achievement unlocked!")
                self.save_data()
                return
        print("Task not found or already completed.")

    def gain_achievement(self, chapter):
        if chapter not in self.achievements:
            self.achievements[chapter] = 0
        self.achievements[chapter] += 1

    def show_tasks(self):
        print("Your tasks:")
        for task in self.tasks:
            status = "Completed" if task['completed'] else "Pending"
            print(f"{task['chapter']} - {status} (Next revision: {task['revision_time']})")

    def show_achievements(self):
        print("Your achievements:")
        for chapter, count in self.achievements.items():
            print(f"{chapter}: {count} times")

    def check_reminders(self):
        reminders = []
        for task in self.tasks:
            if not task['completed'] and datetime.now() >= task['revision_time']:
                reminders.append(task['chapter'])
        if reminders:
            print("Reminders: Time to revise the following chapters:")
            for chapter in reminders:
                print(f"- {chapter}")
        else:
            print("No reminders at this time.")

def main():
    app = StudyApp()
    while True:
        print("\n1. Add Task\n2. Complete Task\n3. Show Tasks\n4. Show Achievements\n5. Check Reminders\n6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            chapter = input("Enter chapter name: ")
            revision_time = int(input("Enter revision time in days: "))
            app.add_task(chapter, revision_time)
        elif choice == '2':
            chapter = input("Enter chapter name to complete: ")
            app.complete_task(chapter)
        elif choice == '3':
            app.show_tasks()
        elif choice == '4':
            app.show_achievements()
        elif choice == '5':
            app.check_reminders()
        elif choice == '6':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
