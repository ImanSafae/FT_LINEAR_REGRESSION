from utils import *

def estimate_price(mileage, theta_0, theta_1):
    estimated_price = theta_0 + (theta_1 * mileage)
    print(f"theta0:{theta_0}, theta1: {theta_1}, mileage:{mileage} ")
    print("price=", estimated_price)
    return estimated_price

def compute_cost(predicted_price, real_price):
    return predicted_price - real_price

def compute_theta0_gradient(total_costs):
    return np.mean(total_costs)

def compute_theta1_gradient(total_costs, mileage_values):
    return np.dot(total_costs, mileage_values) / len(mileage_values)

    
def linear_regression(dataset):
    iterations = 36
    learning_rate = 0.01
    theta_0 = 0.0
    theta_1 = 0.0
    columns = dataset.columns
    mileage_values = dataset[columns[0]]
    price_values = dataset[columns[1]]
    print(mileage_values)

    for i in range(iterations):
        total_costs = []
        for row in range(len(dataset)):
            data = dataset.loc[row]
            mileage = mileage_values[row]
            price = price_values[row]
            predicted_price = estimate_price(mileage, theta_0, theta_1)
            cost = compute_cost(predicted_price, price)
            total_costs.append(cost)
        theta_0_gradient = compute_theta0_gradient(total_costs)
        theta_0 -= learning_rate * theta_0_gradient
        theta_1_gradient = compute_theta1_gradient(total_costs, mileage_values)
        theta_1 -= learning_rate * theta_1_gradient
        if (i % 100 == 0):
            print(f"Iteration {i}: theta_0 = {theta_0}, theta_1 = {theta_1}")
            print("gradients:", theta_0_gradient, theta_1_gradient)




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a data set as an argument to use this program.")
        sys.exit(1)
    dataset = load(sys.argv[1])
    if dataset is None:
        sys.exit(1)

    linear_regression(dataset)
    