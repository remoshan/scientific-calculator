## scientific-calculator  
**A modern Python scientific calculator with a clean CustomTkinter GUI**

![GUI](https://github.com/user-attachments/assets/99313351-a687-4c45-8b0b-4b89def2148c)

---

## Features

- **Basic Calculations**: Addition, subtraction, multiplication, division, and clear operations.
- **Scientific Functions**: Trigonometric functions, exponentials, powers, roots, and more (depending on implementation).
- **Modern UI with CustomTkinter**: A clean, responsive GUI built with `customtkinter` on top of Tkinter.
- **Light/Dark Theme Support**: Optional theme customization using environment variables.
- **Keyboard Support**: Trigger operations via keyboard shortcuts (where implemented).
- **High Precision**: Configurable numerical precision for results.
- **Modular Codebase**: Clear separation between UI and calculation logic for easier maintenance and extension.

---

## Getting Started

### Prerequisites

- **Python**: `>= 3.9`
- **Pip** (Python package manager)

Recommended:

- **Virtual environment** (e.g., `venv` or `conda`) for dependency isolation.

```bash
python --version
pip --version
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/scientific-calculator.git
cd scientific-calculator

# 2. (Optional but recommended) Create & activate a virtual environment
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python main.py
```

---

## Usage

The most common use case is simply **running the GUI application** and performing calculations through the interface.

```bash
python main.py
```

If you want to integrate the calculator logic into another Python script (for example, using the underlying calculation engine directly), you might do something like:

```python
# example_usage.py
from calculator.core import ScientificCalculator  # adjust import to match your project structure

calc = ScientificCalculator()

result_add = calc.evaluate("2 + 3")
result_sin = calc.evaluate("sin(3.14159 / 2)")
result_pow = calc.evaluate("2^10")

print("2 + 3 =", result_add)
print("sin(pi/2) =", result_sin)
print("2^10 =", result_pow)
```

Run the example:

```bash
python example_usage.py
```

> **Note:** Adjust module and class names (`calculator.core`, `ScientificCalculator`, `evaluate`) to match your actual implementation.

---

## Configuration

You can customize runtime behavior via environment variables (for example in a `.env` file or your shell environment).

| Variable              | Default      | Description                                           |
| --------------------- | ------------ | ----------------------------------------------------- |
| `CALC_THEME`          | `system`     | UI theme: `light`, `dark`, or `system`.              |
| `CALC_PRECISION`      | `10`         | Number of decimal places for displayed results.      |
| `CALC_FONT_FAMILY`    | `default`    | Custom font family for the calculator display/keys.  |
| `CALC_LOGGING_LEVEL`  | `INFO`       | Log level: `DEBUG`, `INFO`, `WARNING`, `ERROR`.      |

Example (PowerShell):

```powershell
$env:CALC_THEME = "dark"
$env:CALC_PRECISION = "12"
python main.py
```

---

## Contributing

Contributions, bug reports, and feature requests are welcome!

1. **Fork** the repository on GitHub.
2. **Create a feature branch**:

   ```bash
   git checkout -b feature/my-new-feature
   ```

3. **Make your changes** (code, tests, and documentation as needed).
4. **Run any existing tests/linting** if available.
5. **Commit** your changes with a clear message:

   ```bash
   git commit -m "Add <short feature description>"
   ```

6. **Push** your branch and open a **Pull Request** against the `main` (or default) branch.
7. In the PR description, briefly explain:
   - What you changed.
   - Why you changed it.
   - Any additional notes for reviewers (breaking changes, screenshots, etc.).

---

## License

This project is licensed under the **MIT License**.  
See the `LICENSE` file for full license text.
