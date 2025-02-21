import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

def train_model(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['feedback'])
    y = df['category']  # Assuming you have categories for classification

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = MultinomialNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

    # Save model
    with open('models/nlp_model.pkl', 'wb') as f:
        pickle.dump((model, vectorizer), f)

# Example usage
df = pd.read_csv('data/processed_data.csv')
train_model(df)
