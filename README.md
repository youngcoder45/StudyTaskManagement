# 📚 Study Task Management App

A **command-line based study planner** written in Python to help students manage study tasks, keep track of revision schedules, and unlock achievements as they progress.

This app is designed to make learning **organized, consistent, and rewarding** 🚀.

---

## ✨ Features

* 📖 **Add Tasks** – Create study tasks by entering chapter names and a revision schedule (in days).
* ✅ **Complete Tasks** – Mark tasks as completed once you finish studying.
* 🏆 **Achievements** – Unlock achievements whenever you complete tasks.
* 📅 **Reminders** – Get notified when it’s time to revise a chapter.
* 📂 **Data Persistence** – All tasks and achievements are saved in a local JSON file (`study_data.json`).
* 🖥 **Simple CLI Menu** – Easy-to-use text interface for managing everything.

---

## 📂 Project Structure

```
StudyTaskManagement/
│
├── study_app.py        # Main application file (this code)
├── study_data.json     # Stores tasks & achievements (auto-created)
└── README.md           # Documentation
```

---

## ⚙️ Installation & Usage

### 🔹 Clone the repository

```bash
git clone https://github.com/youngcoder45/StudyTaskManagement.git
cd StudyTaskManagement
```

### 🔹 Run the app

```bash
python study_app.py
```

### 🔹 Menu Options

Once you run the app, you’ll see a menu:

```
1. Add Task
2. Complete Task
3. Show Tasks
4. Show Achievements
5. Check Reminders
6. Exit
```

👉 Enter the number to choose an option.

---

## 🛠 Example Usage

### Add a task

```
Enter chapter name: Physics - Gravitation
Enter revision time in days: 2
Task added: Physics - Gravitation. You need to revise it in 2 days.
```

### Complete a task

```
Enter chapter name to complete: Physics - Gravitation
Task completed: Physics - Gravitation. Achievement unlocked!
```

### Show tasks

```
Your tasks:
Physics - Gravitation - Completed (Next revision: 2025-08-18 15:30:45)
```

### Check reminders

```
Reminders: Time to revise the following chapters:
- Chemistry - Atomic Structure
```

---

## 💡 Why This Project?

This app is useful for:

* Students preparing for exams (like **JEE, NEET, or college exams**).
* Learners who want a **lightweight study tracker** without complicated tools.
* Developers exploring **Python basics, OOP, JSON handling, and datetime** usage.

---

## 🚀 Future Improvements

* ⏰ Notifications / Email alerts for reminders
* 📊 Progress dashboard with stats
* 🖼 GUI version (Tkinter / PyQt / Web-based)
* 🌐 Cloud sync for tasks across devices

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a branch (`git checkout -b feature/improvement`)
3. Commit changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** – you can use, modify, and share it freely.

---

## 👨‍💻 Author

Developed with ❤️ by **[Aditya Verma](https://github.com/youngcoder45)**
