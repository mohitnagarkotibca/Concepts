## Mean Squared error
Formula:


$$
mse= \frac{1}{n}(y_i - ypred_i)^2
$$

Mean squared error, tells us the average distance between actual and predicted values.

Drawbacks:
if the value is large, sqauring it will make it even larger, hence model jitna kharab hai ussey kahi jyada kharab lagega.

if the value is small, squaring the error will make it even smaller, hence model jitna accurate hai , ussey kahi jyada accurte lagega


<br>

## Root mean squared error method:
$$
rmse = \sqrt{\frac{1}{n}(y_i -\hat{y})^2}
$$

## $R^2$ Method:
Formula: <br>
$$ R^2: 1- \frac{\sqrt{\sum_1^n(y_i - ypred_i)^2}}{\sum_i^n(y_i - \tilde{y})^2} $$

R squared tris to capture the variation of data.
example: A $R^2$ of  0.3 means that , the model captures 30 % of the variation.
The model should try try to capture as much variation, it is possible
