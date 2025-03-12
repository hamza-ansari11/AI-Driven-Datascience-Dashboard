import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

def plot_correlation(df):
    """Plot a correlation heatmap with only numeric columns."""
    df_numeric = df.select_dtypes(include=[np.number])
    
    # Check if there are enough numeric columns to plot
    if df_numeric.shape[1] < 2:
        st.warning("Not enough numeric columns to compute correlation matrix.")
        return
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_numeric.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()
    st.pyplot(plt)

def plot_pairplot(df):
    """Plot a pairplot for numeric columns."""
    df_numeric = df.select_dtypes(include=[np.number])
    
    if df_numeric.shape[1] < 2:
        st.warning("Not enough numeric columns to create pair plot.")
        return
    
    fig = sns.pairplot(df_numeric)
    plt.show()
    st.pyplot(fig)

def plot_regression_line(X, y, predictions):
    """Plot regression line for a single feature."""
    plt.figure(figsize=(8, 6))
    plt.scatter(X, y, color="blue")
    plt.plot(X, predictions, color="red", linewidth=2)
    plt.xlabel("Feature")
    plt.ylabel("Target")
    plt.title("Regression Line")
    plt.show()
    st.pyplot(plt)

def plot_residuals(y_true, y_pred):
    """Plot residuals for multiple linear regression."""
    residuals = y_true - y_pred
    plt.figure(figsize=(8, 6))
    sns.residplot(x=y_pred, y=residuals, lowess=True, line_kws={'color': 'red', 'lw': 2}),
    plt.xlabel("Predicted Values")
    plt.ylabel("Residuals")
    plt.title("Residual Plot")
    plt.show()
    st.pyplot(plt)
