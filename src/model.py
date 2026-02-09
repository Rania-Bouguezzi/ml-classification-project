from sklearn.linear_model import LogisticRegression

def create_model():
    """
    Crée et retourne un modèle de classification.
    """
    model = LogisticRegression(max_iter=1000)
    return model
