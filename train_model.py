import pandas as pd
import joblib, os, re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from handle_messages import clean_message
import seaborn as sns


# import matplotlib.pyplot as plt


# function to load the data and get the messages and labels
def csvload(path):
    messages = []  # list containing messages
    labels = []  # list containing labels for the messages

    with open(path, 'r', encoding='utf-8', errors='replace') as file:
        lines = file.readlines()

    for line in lines:
        labels.append(line.strip().split('\t')[0])  # take label part of each line
        messages.append(line.strip().split('\t')[1])  # take message part of each line
    return labels, messages  # retunrn the messages and labels


training_labels, training_messages = csvload('dataset.training.csv')
print("So mau du lieu: ", len(training_labels))
clean_messages = [clean_message(msg) for msg in training_messages]

# Bien doi van ban thanh vector
vectorizer = TfidfVectorizer(max_features=10000, min_df=3, ngram_range=(1, 2), sublinear_tf=True,
                             stop_words='english')
X = vectorizer.fit_transform(clean_messages)
y = pd.Series(training_labels).astype('int')

# Chia du lieu train/test de danh gia nhanh
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Huan luyen mo hinh Logistic Regression
model = LogisticRegression(max_iter=1000, C=4,  class_weight="balanced", random_state=42)
model.fit(X_train, y_train)
print("Huan luyen mo hinh thanh cong!")

# Danh gia nhanh tren tap test
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Do chinh xac tren tap test: {acc * 100:.2f}%")
print(classification_report(y_test, y_pred))

# Cross-validation (tùy chọn)
# scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
# print("Độ chính xác trung bình (CV):", scores.mean())

# Confusion matrix
# cm = confusion_matrix(y_test, y_pred)
# sns.heatmap(cm, annot=True, fmt='d', cmap=plt.cm.Blues)
# plt.xlabel('Predicted')
# plt.ylabel('Actual')
# plt.title('Confusion Matrix')
# plt.show()

# Luu mo hinh va vectorizer de API dung
joblib.dump(vectorizer, 'models/vectorizer.joblib')
joblib.dump(model, 'models/logistic_regression.joblib')

# Xuat file model_feature.csv (word and importance)
feature_importance = model.coef_[0]
words = vectorizer.get_feature_names_out()

feature_df = pd.DataFrame({
    "word": words,
    "importance": feature_importance
}).sort_values(by="importance", ascending=False)

feature_df.to_csv("models/model_features.csv", index=False, encoding="utf-8")
print("Da luu file thanh cong!")
