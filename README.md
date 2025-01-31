# Water Quality Visualization Project

This project analyzes and visualizes water quality data using Python. It includes a dataset of water measurements such as pH, dissolved oxygen, phosphate levels, conductivity, and temperature. The primary visualization is a **scatter plot comparing dissolved oxygen levels with temperature**, helping to identify potential environmental patterns.

## 📁 Project Structure

```
water-quality-visualization/
│── data/                      # Folder for datasets
│   ├── sc_waterdata.csv       # Water quality dataset
│
│── scripts/                   # Folder for Python scripts
│   ├── scatter_plot.py        # Script to generate the scatter plot
│
│── images/                    # Folder to save generated plots
│   ├── scatter_plot.png       # Saved output from the script
│
│── README.md                  # Project documentation
│── requirements.txt            # List of dependencies
│── LICENSE                     # (Optional) License file
```

## 📊 Visualization

The project generates a scatter plot showing **Dissolved Oxygen vs. Temperature**, providing insights into water quality conditions.

## 🚀 How to Run

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/water-quality-visualization.git
   cd water-quality-visualization
   ```

2. **Install Dependencies** (if needed):
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Script**:
   ```sh
   python scripts/scatter_plot.py
   ```

This will generate a **scatter plot** and save it to the `images/` folder.

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
