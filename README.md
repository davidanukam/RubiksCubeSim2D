# Rubik's Cube Simulator

A 2D Rubik's Cube simulation built with **Python** and **PyGame**.

Scramble a cube (either randomly or via a file input) and visualize the solving process using an inverse move mapping system.

## 🚀 Features

* **Move Visualization:** Watch the cube transform in real-time with adjustable animation delays.
* **Custom Scrambles:** Load specific scramble sequences from external text files.
* **Auto-Solver:** Generates the inverse moves of your scramble to return the cube to its solved state.
* **Standalone Executable:** Build the game into a single `.exe` for easy distribution.
* **Dynamic UI:** Includes a custom "Solve" button with hover and click states.
* **Windows Styling:** Utilizes `pywinstyles` for a customized window header.

---

## 🛠️ Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/davidanukam/RubiksCubeSim2D.git
cd RubiksCubeSim2D

```

2. **Install dependencies:**
Ensure you have `pygame`, `pyinstaller`, and `pywinstyles` installed:

```bash
pip install pygame pywinstyles pyinstaller

```

---

## 📦 Building the Executable

To bundle the game into a single Windows executable (`.exe`), use the following PyInstaller command. This ensures the `assets` folder (containing the logo) is bundled inside the file:

```bash
pyinstaller --noconsole --onefile --add-data "assets/;assets/" game.py

```

* `--onefile`: Packages everything into a single `.exe`.
* `--noconsole`: Hides the terminal window when the game starts.
* `--add-data`: Includes the logo and images in the internal temporary directory.

The finished file will be located in the `/dist` folder.

---

## 🎮 Usage

### 1. Running the Script

By default, the game performs 100 random moves or accepts a file argument:

(See [scramble_example.txt](https://github.com/davidanukam/RubiksCubeSim2D/blob/main/scramble_example.txt))

```bash
python game.py scramble_example.txt

```

### 2. Running the Executable

* **Standard Scramble:** Double-click `game.exe`.
* **Custom File Scramble:** Drag and drop your `.txt` scramble file directly onto the `game.exe` icon.

---

## 🕹️ Controls

* **Scramble Phase:** On startup, the game automatically executes the scramble sequence.
* **Solve Button:** Once the scramble is complete, a **Solve** button will appear. Click it to watch the simulator reverse the moves and solve the cube.

---

## 📂 Project Structure

* `game.py`: The core game loop, asset path handling, and rendering logic.
* `file_parser.py`: Logic for reading Rubik's notation from text files.
* `movement.py`: Logic for cube rotations (Up, Down, Left, Right, Front, Back, and Wide moves).
* `node.py`: Defines the individual stickers/faces of the cube.
* `cube_data.py`: Holds the grid state and initial configuration.
* `solve_button.py`: UI component for the solving trigger.
* `assets/`: Contains images and icons (e.g., `RubiksCubeLogo.png`).

---

## 📝 License

This project is open-source and available under the [MIT License](https://github.com/davidanukam/RubiksCubeSim2D/blob/main/LICENSE).
