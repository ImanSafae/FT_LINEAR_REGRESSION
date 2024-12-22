from utils import *

def parse_thetas(thetas_df):
    for col in thetas_df.columns:
        if col != 'theta0' and col != 'theta1':
            print("Invalid column names. Default values will be used:", col)
            return 0, 0
    theta_0 = thetas_df['theta0'][0]
    theta_1 = thetas_df['theta1'][0]
    return theta_0, theta_1

def estimate_price(mileage, theta_0, theta_1):
    return theta_0 + (theta_1 * mileage)

if __name__ == '__main__':

    theta_0 = 0.0
    theta_1 = 0.0

    try:
        # handle cases with imported thetas
        if len(sys.argv) > 1:
            thetas_file = sys.argv[1]
            thetas_df = load(thetas_file)
            if thetas_df is None:
                print("Error loading file. Default values will be used. To provide theta values, please provide a valid .csv file.")
            else:
                theta_0, theta_1 = parse_thetas(thetas_df)
        
        mileage = float(input("Enter mileage: "))
        price = estimate_price(mileage, theta_0, theta_1)
        print("Estimated price:", price)
    except Exception as e:
        print(e)
        sys.exit(1)
