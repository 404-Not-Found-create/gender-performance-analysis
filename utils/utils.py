# === UTILS === 

# === Imports === 
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# === Functions ===
def create_pie(data, title):
    plt.pie(data, labels=data.index, autopct='%1.2f%%', startangle=90)
    plt.title(title)
    plt.show()

def create_boxplot(data, x, y, title):
    sns.boxplot(data=data, x=x, y=y)
    plt.title(title)
    plt.show()

def view_ttest(x1, x2):
    t_stat, p_value = stats.ttest_ind(x1, x2)

    print(f"T-statistics: {t_stat:.2f}")
    print(f"P-value: {p_value:.4f}")

    if p_value < 0.05:
        print("The difference is statistically significant: the hypothesis is confirmed ✅.")
    else:
        print("There is no statistically significant difference: the hypothesis is not confirmed ❌.")