# 🌊 Sea Level Predictor

This project is part of the **[freeCodeCamp Data Analysis with Python Certification](https://www.freecodecamp.org/learn/data-analysis-with-python/)**. It analyzes historical sea level data and uses linear regression to predict future trends. The project visualizes the data and regression lines to communicate the impact of rising sea levels.

---

## 📊 Project Overview

The project includes:

- A **scatter plot** of historical sea level measurements from 1880 to 2013.
- A **line of best fit** using all available data (1880–2013) projected to 2050.
- A **second line of best fit** using data from 2000 onward, also extended to 2050.

These visualizations are generated using Matplotlib and regression lines are calculated using SciPy.

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- Matplotlib
- SciPy
- Unittest (for testing)

---

## 📁 Project Structure

```
.
├── sea_level_predictor.py   # Script that generates the plot
├── test_module.py           # Unit tests for validation
├── epa-sea-level.csv        # Dataset of sea level measurements
├── sea_level_plot.png       # Output visualization of the regression
```

---

## ⚙️ How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/sea-level-predictor.git
   cd sea-level-predictor
   ```

2. **Install dependencies**:
   ```bash
   pip install pandas matplotlib scipy
   ```

3. **Run the script**:
   ```bash
   python sea_level_predictor.py
   ```

This will generate:
- `sea_level_plot.png`

---

## 🧪 Testing

To run the included unit tests:

```bash
python test_module.py
```

Tests validate:
- Plot title and labels
- X-tick labels
- Data points and regression lines

---

## 📚 What I Learned

- How to apply linear regression to real-world environmental data
- How to visualize regression predictions in Matplotlib
- Best practices for plotting and extending prediction curves

---

## 📜 License

This project is part of the **freeCodeCamp Data Analysis with Python** certification and is provided for educational purposes.

---

## 🙌 Acknowledgments

- [freeCodeCamp](https://www.freecodecamp.org/) for the curriculum and dataset
- The Python data science community for open-source tools
