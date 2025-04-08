import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

def plot_dist(y, title):
    sns.countplot(x=y)
    plt.title(title)
    plt.show()

# Dummy imbalanced dataset
df = pd.DataFrame({
    'feature1': range(100),
    'feature2': range(100, 200),
    'target': [0]*90 + [1]*10
})

X, y = df[['feature1', 'feature2']], df['class']
plot_dist(y, "Original Distribution")

X_sm, y_sm = SMOTE().fit_resample(X, y)
plot_dist(pd.Series(y_sm), "SMOTE Oversampled")

X_ru, y_ru = RandomUnderSampler().fit_resample(X, y)
plot_dist(pd.Series(y_ru), "Random Undersampled")
