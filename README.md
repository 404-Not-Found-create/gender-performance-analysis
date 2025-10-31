# 📊 Gender Performance Analysis

## 🧠 **Project Objective**
To investigate whether gender influences student performance in **math**, **reading**, and **writing**. The project also explores the impact of **parental education level** and **test preparation courses**.

---

## 📁 **Project Structure**

project/
├── notebook/
│   └── analysis.ipynb         # main analysis notebook
├── utils/
│   └── utils.py               # utility functions for visualization and statistics
├── visuals/
│   └── *.png                  # saved charts and plots
├── data/
│   └── StudentsPerformance.csv
├── requirements.txt
└── README.md


---

## 📌 **Methods Used**

- 📊 Pie charts and boxplots for visual analysis  
- 🧪 Independent t-tests to compare group means  
- 🧮 Grouping by gender, parental education, and test preparation status

---

## 📈 **Key Steps**

1. Load and preprocess the dataset  
2. Analyze gender distribution  
3. Compare parental education levels  
4. Examine test preparation course participation  
5. Test hypotheses across math, reading, and writing scores

---

## ✅ **Findings**

- **Females** outperform males in *reading* and *writing*  
- **Males** score higher in *math*  
- **Parental education** and **test preparation** significantly affect performance  
- Differences are **statistically significant** (`p-value < 0.05`)

---

## 🛠 **Libraries Used**

- `pandas`  
- `matplotlib`  
- `seaborn`  
- `scipy`

---

## 🔮 **Future Improvements**

- Add regression analysis  
- Build predictive models for exam scores  
- Include additional demographic features

---

## 🚀 **How to Run**

1. Clone the repository  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
