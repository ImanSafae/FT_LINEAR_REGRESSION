from utils import *

def estimate_price(mileage, theta_0, theta_1):
    estimated_price = theta_0 + (theta_1 * mileage)
    return estimated_price

def compute_cost(predicted_price, real_price):
    return predicted_price - real_price

def compute_theta0_gradient(total_costs):
    return np.mean(total_costs)

def compute_theta1_gradient(total_costs, mileage_values):
    return sum(total_costs * mileage_values) / len(mileage_values)

def compute_gradients(mileage_values, price_values, theta_0, theta_1, learning_rate):
    m = len(mileage_values)
    predicted_prices = estimate_price(mileage_values, theta_0, theta_1)
    differences = predicted_prices - price_values
    
    tmp_theta0 = learning_rate * (1/m) * np.sum(differences)
    tmp_theta1 = learning_rate * (1/m) * np.sum(differences * mileage_values)
    
    return tmp_theta0, tmp_theta1

    
def linear_regression(dataset):
    iterations = 100
    learning_rate = 0.0001
    theta_0 = 0.0
    theta_1 = 0.0
    columns = dataset.columns
    mileage_values = dataset[columns[0]]
    price_values = dataset[columns[1]]
    print(mileage_values)

    for i in range(iterations):
        # predicted_prices = estimate_price(mileage_values, theta_0, theta_1)
        # cost = compute_cost(predicted_prices, price_values)
        # theta_0_gradient = compute_theta0_gradient(cost)
        # theta_1_gradient = compute_theta1_gradient(cost, mileage_values)
        tmp_theta0, tmp_theta1 = compute_gradients(mileage_values, price_values, theta_0, theta_1, learning_rate)
        theta_0 -= tmp_theta0
        theta_1 -= tmp_theta1

        if (i % 10 == 0):
            print(f"Iteration {i}: theta_0 = {theta_0}, theta_1 = {theta_1}")
            # print("gradients:", theta_0_gradient, theta_1_gradient)
    print(f"Final values: theta_0 = {theta_0}, theta_1 = {theta_1}")




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a data set as an argument to use this program.")
        sys.exit(1)
    dataset = load(sys.argv[1])
    if dataset is None:
        sys.exit(1)

    linear_regression(dataset)
    