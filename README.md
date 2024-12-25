# FT_LINEAR_REGRESSION

Ft_linear_regression is a project of the post-common core curriculum at 42, and it serves as an introduction to machine learning.
The goal is to create a program that will predict the price of a car depending on its mileage, using a linear function with a gradient descent algorithm.
My language of choice for this project was of course Python, as it makes it easy to manipulate and visualise data thanks to its libraries numpy, pandas and matplotlib. I didn't use scikit-learn in this project, as it was encouraged to code as much as possible manually.

### How to use
The program `train.py` should be called first with an argument on the command line, which should be a .csv file with data formatted in 2 columns: 'price', and 'km'. A file is already provided in this repository under the name of `data.csv`.
The training program will output the results in a `thetas.csv` file (but you're free to rename it however you like).
This file should then be used to call the prediction program: `predict.py` (if you call this program without the `thetas` file it will simply set them as 0 but it will be useless).
The program will prompt you to enter a mileage and return the price of the car it calculated thanks to the coefficients you gave it.

### How it works
The first program, as shown by its name, trains our model, using linear regression and gradient descent.
We are required to use the following formulas:
![image](https://github.com/user-attachments/assets/699e731f-dd8e-4984-92c5-935c0ef5110a)
![image](https://github.com/user-attachments/assets/34fd9168-1422-44e5-974d-47d07071db40)

The first one means that we establish a linear relation between the mileage and the price of a car. But in order to calculate it, we need to determine the values of the θ coefficients.

We'll start by setting them as 0. This will give us of course, completely inaccurate results.
Then, we will adjust them in the right direction, until they reach acceptable values that should give us acceptable price predictions. This is what **gradient descent** is.

#### Gradient descent
How do we do this? We'll adjust them over 1000 iterations, using a _step_ (or a gradient) calculated with the formulas on the second picture. The sign of these steps will determine the direction that the coefficients should follow: if it's negative, the coefficient should go up. If it's positive, the coefficient should go down. To achieve this, we'll simply substract the step from the coefficients. To make this even more precise and accurate, we'll set a **learning rate**, that will be constant and multiply the step so it's not too big so it misses the optimal point (it shouldn't be too small either or it will take way too many iterations to reach the optimal point). This optimal point means that the error (which we can calculate thanks to the method of _mean squared error_, also known as MSE) reaches a minimum. However here, we'll simply consider that after 1000 iterations, this optimal point has been reached.
We're lucky enough that the formulas for the steps have been provided to us; however, they're otherwise easy to calculate, as they're the partial derivatives of the loss function, with respect to both coefficients. We will not go into this in detail as, as I said, the formulas to use were already provided to us, but documentation about this can easily be found to understand more deeply (and mathematically) why we went with these formulas.

### Data standardization
In order to not reach crazy values for our coefficients, the data used for our linear regression should be standardized or normalized. Here, I went with standardization, as it gave the best results and is less sensible to the extreme values in the data set. This means that all of our values are now contained within a small range, of mean 0 and of standard deviation 1.
This also means that when we finally have our coefficients, they should be destandardized. Otherwise, if we try to use them to predict the price of a car by giving the program a normal mileage value, the result won't be in the expected range at all (because the coefficient was calculated with a way smaller range of values).
Once they're destandardized, they're now finally ready for use.

### Data plotting
As a bonus, the training program includes data plotting: it plots the real, non-standardized values used for the training, as well as the regression line, obtained with our fresh new coefficients.
![image](https://github.com/user-attachments/assets/9ab67163-dbea-45d9-92d3-c7f0ee1c4a01)

### Accuracy
As another bonus, the program calculates its own accuracy rate on the data provided. It should be around 66.7% on the `data.csv` data set.
