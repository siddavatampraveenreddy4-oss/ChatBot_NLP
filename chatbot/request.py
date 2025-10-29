import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# =============================
# 1️⃣ Sample Data
# =============================
data = {
    "text": [
        "the government passed a new bill today",
        "India won the cricket world cup",
        "new AI model beats human accuracy",
        "prime minister visits the usa",
        "Football league final schedule tomorrow",
        "apple launches new iphone model"
    ],
    "category": ["politics", "sports", "technology", "politics", "sports", "technology"]
}

df = pd.DataFrame(data)

# =============================
# 2️⃣ TF-IDF Vectorization
# =============================
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df["text"])
y = df["category"]

# =============================
# 3️⃣ Train-Test Split
# =============================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# =============================
# 4️⃣ Train Classifier
# =============================
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# =============================
# 5️⃣ Evaluate Accuracy
# =============================
predictions = model.predict(X_test)
print("✅ Model Accuracy:", accuracy_score(y_test, predictions))

# =============================
# 6️⃣ Predict Category for New Text
# =============================
while True:
    user_input = input("\nEnter a news headline (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    input_vec = vectorizer.transform([user_input])
    predicted_category = model.predict(input_vec)[0]
    print("📢 Predicted Category:", predicted_category)
