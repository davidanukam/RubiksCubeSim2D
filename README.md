# PyGame Rubik's Cube Simulator

A 2D Rubik's Cube simulation built with **Python** and **PyGame**.

Scramble a cube, (either randomly or via a file input) and visualize the solving process using an inverse move mapping system.

## 🚀 Features

* **Move Visualization:** Watch the cube transform in real-time with adjustable animation delays.
* **Custom Scrambles:** Load specific scramble sequences from external text files.
* **Auto-Solver:** Generates the inverse moves of your scramble to return the cube to its solved state.
* **Dynamic UI:** Includes a custom "Solve" button with hover and click states.
* **Windows Styling:** Utilizes `pywinstyles` for a customized window header.

---

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/davidanukam/RubiksCubeSim2D.git
cd RubiksCubeSim2D

```


2. **Install dependencies:**
Ensure you have `pygame` and `pywinstyles` installed:
```bash
pip install pygame pywinstyles

```



---

## 🎮 Usage

You can run the simulator in two modes:

### 1. Random Scramble

By default, the game will perform 100 random moves upon startup.

```bash
python main.py

```

### 2. Custom Scramble File

Load a sequence of moves from a `.txt` file.

```bash
python main.py scramble_example.txt

```

> **Note:** The file parser expects standard Rubik's notation (e.g., U, R', F2, etc.) -> See [scramble_example.txt](https://github.com/davidanukam/RubiksCubeSim2D/blob/main/scramble_example.txt)

---

## 🕹️ Controls

* **Scramble Phase:** On startup, the game automatically executes the scramble sequence.
* **Solve Button:** Once the scramble is complete, a "Solve" button will appear. Click it to watch the simulator reverse the moves and solve the cube.

---

## 📂 Project Structure

* `main.py` / `game.py`: The core game loop and rendering logic.
* `movement.py`: Contains the logic for cube rotations (Up, Down, Left, Right, Front, Back).
* `node.py`: Defines the individual stickers/faces of the cube.
* `cube_data.py`: Holds the grid state and initial configuration.
* `solve_button.py`: UI component for the solving trigger.
* `colors.py`: Color palette definitions.

---

## 📝 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).
