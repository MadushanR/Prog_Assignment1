# Python Challenge Duel

A simple two-player command-line game in Python where each player faces three ability-based challenges. The first player to win two out of three rounds is crowned the champion.

## Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)
* [Gameplay](#gameplay)
* [Configuration](#configuration)
* [Running the Game](#running-the-game)
* [Contributing](#contributing)

## Features

* **Two-Player Mode**: Players compete head-to-head in three consecutive challenges.
* **Ability-Based Rounds**: Challenges adapt to each player’s performance.
* **Best of Three**: First to win two rounds wins the game.
* **Command-Line Interface**: Lightweight, no GUI required.
* **Extensible**: Easily add new challenges or modify existing ones.

## Tech Stack

* **Language**: Python 3.6+

## Prerequisites

* Python 3.6 or higher installed on your system.
* (Optional) A virtual environment tool such as `venv` or `virtualenv`.

## Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MadushanR/Prog_Assignment1.git
   cd Prog_Assignment1
   ```
2. **(Optional) Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies** (if any are listed in `requirements.txt`):

   ```bash
   pip install -r requirements.txt
   ```

## Gameplay

1. Run the game script:

   ```bash
   python game.py
   ```
2. Enter names for **Player 1** and **Player 2** when prompted.
3. The game will present **three** sequential challenges.
4. Each challenge is scored based on player inputs or performance.
5. The player who wins **two** challenges first wins the duel.
6. After three rounds (or once a player reaches two wins), the game announces the champion.

## Configuration

* **Challenge Logic**: Found in `challenges.py`. Modify or add functions to change or extend challenges.
* **Game Script**: `game.py` contains the main loop and player interaction.
* **Constants**: Tweak round settings or scoring thresholds in `config.py` (if present).

## Running the Game

Simply execute:

```bash
python game.py
```

Enjoy a quick duel with a friend directly in your terminal!

## Contributing

1. ⭐️ Fork this repository.
2. 🔀 Create a new branch (`git checkout -b feature/YourFeature`).
3. 🛠️ Implement your feature or fix.
4. 📄 Commit your changes (`git commit -m "Add new challenge"`).
5. 🚀 Push to your branch (`git push origin feature/YourFeature`).
6. 🔎 Open a Pull Request.


---

> *Built with ⚔️ and 🎲 by Python enthusiasts!*
