# 🚁 Drone Flight Time Calculator

The **Drone Flight Time Calculator** is a simple and intuitive desktop application built with Python and Tkinter.  
It helps drone hobbyists, pilots, and builders quickly estimate flight time based on key aircraft specifications.

---

## ✨ Key Features

- **Simple & Clean UI** – A straightforward interface that is easy to navigate.
- **Essential Inputs** – Calculates flight time based on four critical parameters:
  - Battery Capacity (mAh)
  - Total Drone Weight (AUW in kg)
  - Power Consumption (watts/kg)
  - Battery Voltage (V)
- **Instant Calculation** – Displays estimated flight time instantly in minutes.
- **Safety Margin Included** – Uses an 80% safe discharge factor to preserve battery health.
- **Robust Error Handling** – Handles non-numeric inputs and division-by-zero gracefully.
- **Cross-Platform** – Available for **Windows** (macOS support coming soon).

---

## 🚀 How to Use

### 🔹 Windows
1. Download the `drone_calculator_gui.exe` file from the **Assets** section.
2. Double-click the executable to run the application.  
   *(No Python installation required.)*

### 🔹 macOS
⚠️ **Note:** The macOS build is not yet available. Please run the app from source (instructions below).

---

## ⚙️ From Source (Developers)

1. Download the `drone_calculator_gui.py` file.
2. Ensure you have **Python 3** installed.
3. Run the script from your terminal:
   ```bash
   python drone_calculator_gui.py
