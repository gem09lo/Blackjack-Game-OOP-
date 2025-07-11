# 🃏 Blackjack Game - OOP (Object-Oriented Programming)

## 🧾 Overview

This project is an **OOP-based refactor** of the classic Blackjack card game, originally built using procedural Python. It restructures the core logic into modular classes (`Card`, `Hand`, `Deck`) and introduces principles of clean, object-oriented design. 

It’s currently a **foundational version**, focusing on the core card logic, and sets the groundwork for building a fully playable game in future iterations.

---

## 🎯 Project Aims

- Apply Object-Oriented Programming (OOP) principles in Python
- Practice clean code architecture with modular class design
- Build unit tests using `pytest`
- Reinforce TDD practices from the original Blackjack project

---

## 📁 Project Structure

[blackjack_oop/]
  - `blackjack_oop.py`: Defines Card, Hand, Deck classes with core logic
  - `test_blackjack_oop.py`: Unit tests using pytest


- `requirements.txt`: Dependencies (pytest, pylint)
- `.gitignore`: Ignores virtual environment, caches, etc.

--- 

## ⚙️ Getting Setup

1. **Clone the repo**
  - `git clone https://github.com/your-username/blackjack_oop.git`
  - `cd blackjack_oop`

2. **Create and activate a virtual environment**
  - `python -m venv .venv`
  - `source .venv/bin/activate`  
    - Or `.- venv\Scripts\activate` on Windows

3. **Install dependencies**
  - `pip install -r requirements.txt`

🕹️ **Note**: This version is not yet interactive. It contains core logic only and does not include a CLI game loop.

---

## 🧪 Running the Tests

This project uses pytest to verify:
- Cards return correct values
- Deck is correctly generated and drawn from
- Hands handle multiple cards and Ace edge cases properly

Make sure your virtual environment is active. Then run:
- `pytest test_blackjack_oop.py`

--- 

## 🧼 Code Quality
- Follows clean code principles from the Sigma Labs curriculum
- Modular class structure for maintainability
- Code linted with pylint to ensure readability and consistency

---

## 🧠 Concepts Demonstrated

- Object-Oriented Programming (OOP)
  - Classes and Encapsulation
  - Methods and State Management
- Unit Testing with `pytest`
- Clean Code Practices
- Handling edge cases (e.g. two Aces = 21)

--- 

## 🚀 Next Steps (Ideas for Extension)

- Add a Player class to represent players and dealers
- Build a game loop for user interaction (CLI or GUI)
- Shuffle the deck before play
- Handle busts, dealer logic, etc.

--- 

## 🙌 Acknowledgments
This refactor is part of the training programme to improve OOP design and testing in Python, based on a procedural Blackjack game created during Week 1 of Sigma Labs' data engineering course.
