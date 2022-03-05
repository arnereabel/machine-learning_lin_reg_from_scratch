# machine-learning_lin_reg_from_scratch

We can measure how well a line fits by measuring loss.
The goal of linear regression is to minimize loss.
To find the line of best fit, we try to find the b value (intercept) and the m value (slope) that minimize loss.
Convergence refers to when the parameters stop changing with each iteration.
Learning rate refers to how much the parameters are changed on each iteration.
We can use Scikit-learn’s LinearRegression() model to perform linear regression on a set of points.




Introduction to Linear Regression
The purpose of machine learning is often to create a model that explains some real-world data, so that we can predict what may happen next, with different inputs.

The simplest model that we can fit to data is a line. When we are trying to find a line that fits a set of data best, we are performing Linear Regression.

We often want to find lines to fit data, so that we can predict unknowns. For example:

The market price of a house vs. the square footage of a house. Can we predict how much a house will sell for, given its size?
The tax rate of a country vs. its GDP. Can we predict taxation based on a country’s GDP?
The amount of chips left in the bag vs. number of chips taken. Can we predict how much longer this bag of chips will last, given how much people at this party have been eating?

A line is determined by its slope and its intercept. In other words, for each point y on a line we can say:

y = m x + by=mx+b
where m is the slope, and b is the intercept. y is a given point on the y-axis, and it corresponds to a given x on the x-axis.

The slope is a measure of how steep the line is, while the intercept is a measure of where the line hits the y-axis.

Loss
When we think about how we can assign a slope and intercept to fit a set of points, we have to define what the best fit is.

For each data point, we calculate loss, a number that measures how bad the model’s (in this case, the line’s) prediction was. You may have seen this being referred to as error.

We can think about loss as the squared distance from the point to the line. We do the squared distance (instead of just the distance) so that points above and below the line both contribute to total loss in the same way:

Gradient Descent for Intercept
As we try to minimize loss, we take each parameter we are changing, and move it as long as we are decreasing loss. It’s like we are moving down a hill, and stop once we reach the bottom:


The process by which we do this is called gradient descent. We move in the direction that decreases our loss the most. Gradient refers to the slope of the curve at any point.
