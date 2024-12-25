from utils import *
from accuracy import *

def plot_data(dataset, theta_0, theta_1):
    """
    Plot the dataset as a scatter plot to verify linearity, 
    and draw the regression line to verify accuracy of the model.
    """
    dataset.plot(x="km", y="price", style="o")

    mileage_values = dataset["km"]
    price_values_estimated = theta_0 + theta_1 * mileage_values
    plt.plot(mileage_values, price_values_estimated, color="red", label="regression line")

    plt.title("Price vs Mileage")
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

def compute_loss(theta_0, theta_1, x, y):
    """
    Compute the loss function for linear regression.
    """
    m = len(x)
    predictions = theta_0 + theta_1 * x
    return (1 / (2 * m)) * np.sum((predictions - y) ** 2)


def compute_gradients(mileage_values, price_values, theta_0, theta_1, learning_rate):
    m = len(mileage_values)
    predicted_prices = estimate_price(mileage_values, theta_0, theta_1)
    differences = compute_difference(predicted_prices, price_values)
    
    tmp_theta0 = learning_rate * (1/m) * np.sum(differences)
    tmp_theta1 = learning_rate * (1/m) * np.sum(differences * mileage_values)
    
    return tmp_theta0, tmp_theta1
    
def linear_regression(dataset):
    iterations = 1000
    learning_rate = 0.01
    theta_0 = 0
    theta_1 = 0
    columns = dataset.columns
    mileage_values = dataset[columns[0]]
    price_values = dataset[columns[1]]

    for i in range(iterations):
        tmp_theta0, tmp_theta1 = compute_gradients(mileage_values, price_values, theta_0, theta_1, learning_rate)
        theta_0 -= tmp_theta0
        theta_1 -= tmp_theta1

        # if i % 100 == 0:
        #     loss = compute_loss(theta_0, theta_1, mileage_values, price_values)
        #     print(f"Iteration {i}, Loss: {loss}")
    return theta_0, theta_1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a data set as an argument to use this program.")
        sys.exit(1)
    dataset = load(sys.argv[1])
    if dataset is None:
        sys.exit(1)

    normalized_df = normalize_dataframe(dataset)
    theta_0, theta_1 = linear_regression(normalized_df)
    theta_0, theta_1 = denormalize_coefficients(theta_0, theta_1, dataset)
    results = pd.DataFrame({"theta_0": [theta_0], "theta_1": [theta_1]})
    results.to_csv("thetas.csv", index=False)
    print(f"Final values: theta_0 = {theta_0}, theta_1 = {theta_1}")
    measure_accuracy(theta_0, theta_1, dataset)
    plot_data(dataset, theta_0, theta_1)
    
    