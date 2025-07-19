# 🗓️ Time Table Generator using Genetic Algorithm

[![Python](https://img.shields.io/badge/Made%20with-Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

> A Python project that automatically generates class timetables using a **Genetic Algorithm**, balancing hard and soft constraints to find the most optimal solution.

---

## 📌 Overview

Creating timetables manually is time-consuming and error-prone. This project automates that process using **Genetic Algorithms**—a biologically inspired optimization technique—ensuring no conflicts while maintaining teacher and class constraints.

---

## 💡 Features

- ✅ Handles hard constraints (no overlapping classes or teachers).
- ♻️ Optimizes soft constraints (balanced faculty workload).
- ⚙️ Modular OOP design for scalability and flexibility.
- 📊 Console-based output for analysis and debugging.

---

## 🧠 How It Works

The Genetic Algorithm mimics natural selection:

1. **Initialize** a random population of timetables (chromosomes).
2. **Evaluate** fitness based on constraint satisfaction.
3. **Select** using Roulette Wheel Selection.
4. **Crossover** genes between chromosomes.
5. **Mutate** with a low probability.
6. **Repeat** until a valid or optimal timetable is generated.

> This approach ensures continuous improvement across generations.

---

## 🏗️ Project Structure

| 📁 Module        | 🔍 Description                                                                 |
|------------------|---------------------------------------------------------------------------------|
| `StudentGroup`   | Defines student groups, their subjects, and weekly hour requirements.           |
| `Teacher`        | Holds faculty details including subject taught and assigned batches.            |
| `Slot`           | Basic time slot unit, the gene's building block.                                |
| `TimeTable`      | Maintains a list of slots for each group.                                       |
| `Gene`           | Represents one group’s timetable (array of slots).                              |
| `Chromosome`     | Full schedule, includes genes for all groups. Subject to crossover & mutation.  |
| `Utility`        | Prints debug logs and tracks fitness progression.                               |
| `InputData`      | Fetches user input from file or form.                                           |
| `SchedulerMain`  | Entry point; controls the GA (selection, mutation, crossover).                  |

---

## 🧪 Constraints

### ✅ Hard Constraints (must be satisfied)
- No faculty can teach multiple classes at the same time.
- No student group can attend more than one lecture at a time.

### ♻️ Soft Constraints (should be optimized)
- Balanced faculty workload.
- Adequate weekly hours for all subjects per batch.

---

## 🧪 Sample Output

```text
Generation 1:
Chromosome Fitness: 0.67
...
Generation 45:
Chromosome Fitness: 1.00 ✅ Optimal timetable found!

Final Timetable:
---------------------
Batch A:
Mon: Math - Mr. X
Tue: Physics - Mrs. Y
...
```

---

## 📥 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/palak-khanna/Time-Table-Generator.git
cd Time-Table-Generator

# Run the main script
python main.py
```

> Use the provided sample input or update it as per your institutional data.

---

## 🚀 Future Enhancements

- 🧑‍🏫 Faculty preferences for specific time slots.
- 🧮 Classroom/lab capacity consideration.
- 🖨️ Export timetable as PDF/CSV.
- 📅 Individual timetable view for faculty and students.
- 🌐 Web-based UI for ease of use.

---

## 📚 References

- 📄 [Original Project Report (PDF)](https://github.com/palak-khanna/Time-Table-Generator/blob/main/AutomatedTimeTableScheduler%20(1).pdf)
- 📘 *Genetic Algorithms* by David E. Goldberg
- 🌐 [AI Junkie GA Tutorial](http://www.ai-junkie.com/ga/intro/gat3.html)

---

## 🤝 Contributors

- 👩‍💻 Palak Khanna  
- 👨‍💻 Shanvi
---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

> ⭐ *If you find this project helpful, please consider starring the repo!*
