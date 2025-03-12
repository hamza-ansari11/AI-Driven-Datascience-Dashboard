from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def train_linear_regression(X, y):
    """Train a linear regression model."""
    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)
    return model, predictions

def evaluate_model(model, X, y):
    """Evaluate the trained linear regression model."""
    predictions = model.predict(X)
    r2 = r2_score(y, predictions)
    mae = mean_absolute_error(y, predictions)
    mse = mean_squared_error(y, predictions)
    rmse = mean_squared_error(y, predictions, squared=False)
    return r2, mae, mse, rmse
