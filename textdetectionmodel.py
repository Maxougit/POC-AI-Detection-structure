from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from joblib import dump, load


def train_model():
    texts = ["Exemple de texte généré par un humain", "Exemple de texte généré par IA", "Autre exemple de texte généré par un humain", "Autre exemple de texte généré par IA"] 
    labels = ["humain", "IA", "humain", "IA"] 

    # Prétraitement des données
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    y = labels

    # Séparation des données d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # # Entraînement du modèle
    model = SGDClassifier()
    model.fit(X_train, y_train)

    # Évaluation du modèle
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))

    # export model
    dump(model, 'model.joblib')
    dump(vectorizer, 'vectorizer.joblib')


def load_model():
    model = load('model.joblib')
    vectorizer = load('vectorizer.joblib')
    return model, vectorizer

def test_model(example_text):
    model, vectorizer = load_model()
    test_text_vectorized = vectorizer.transform([example_text])
    return model.predict(test_text_vectorized)[0]


