import numpy as np
import pandas as pd
import os, sys
import matplotlib.pyplot as plt

def load(path: str):
    ret = None

    try:
        if (isinstance(path, str) is False):
            raise ValueError("Path must be a string")
        if (path.endswith(".csv") is False):
            raise ValueError("Path must be a csv file")
        if (os.path.exists(path) is False):
            raise ValueError("File not found")
        ret = pd.read_csv(path)
    except Exception as e:
        print(e)
    return ret

def normalize_dataframe(df: pd.DataFrame):
    # normalized_data = (df - df.min()) / (df.max() - df.min())
    # return normalized_data
    standardized_data = (df - df.mean()) / df.std()
    return standardized_data

def denormalize_coefficients(theta_0, theta_1, dataset):
    mean_x = dataset['km'].mean()
    std_x = dataset['km'].std()
    mean_y = dataset['price'].mean()
    std_y = dataset['price'].std()

    theta_0_prime = theta_0 * std_y + mean_y - (theta_1 * mean_x * std_y / std_x)
    theta_1_prime = theta_1 * std_y / std_x

    return theta_0_prime, theta_1_prime

def estimate_price(mileage, theta_0, theta_1):
    """
    Estimate the price of a car given its mileage, according to the provided formula.
    """
    estimated_price = theta_0 + (theta_1 * mileage)
    return estimated_price

def compute_difference(predicted_price, real_price):
    """
    Return the difference between the predicted price, as calculated by the model, and the real price.
    """
    return predicted_price - real_price