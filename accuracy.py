from utils import *

def measure_accuracy(theta0, theta1, dataset):
    correct_predictions = 0
    real_prices = dataset['price']
    estimated_prices = estimate_price(dataset['km'], theta0, theta1)
    threshold = 0.1 * np.mean(real_prices)
    errors = np.abs(compute_difference(estimated_prices, real_prices))

    for error in errors:
        if error <= threshold:
            # print("Correct prediction:", error, "<=", threshold)
            correct_predictions += 1
    
    accuracy = correct_predictions / len(real_prices)
    # print("Correct predictions:", correct_predictions)
    # print("Total predictions:", len(real_prices))
    print("Accuracy:", '{:.2%}'.format(accuracy))
