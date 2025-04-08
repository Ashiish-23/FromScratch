import pandas as pd  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split  
from sklearn.tree import DecisionTreeClassifier, plot_tree  
from sklearn.metrics import accuracy_score, classification_report  
from sklearn.datasets import load_iris  

iris = load_iris()  
X, y = iris.data, iris.target  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)  

clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)  
clf.fit(X_train, y_train)  
y_pred = clf.predict(X_test)  
print("Accuracy:", accuracy_score(y_test, y_pred))  
print("Classification report:\n", classification_report(y_test, y_pred))  

plt.figure(figsize=(10,6))  
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)  
plt.show()  

plt.barh(iris.feature_names, clf.feature_importances_, color='blue')  
plt.xlabel('Feature Importance')  
plt.title('Feature Importances in Decision Tree')  
plt.show()
