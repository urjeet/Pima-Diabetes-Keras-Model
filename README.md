# Predicting Diabetes in Pima Native Americans Using Keras
***
My first Deep Learning project, I used Keras and TensorFlow to train and evaluate a neural network that can predict diabetes in Pima Native Americans given several other factors. I followed a tutorial for this project, however, it has been severely modified.

*Program Written in December 2020*  
*Pushed to Github in December 2020*

***

## Source Files and Their Roles

`pima_diabetes_keras_model.py` is driver program that loads the dataset, defines a Keras model, compiles the Keras model, fits the Keras model on the dataset, evaluates the Keras model, and finally makes class predictions with the model on the already seen dataset. [Sequential](https://keras.io/api/models/sequential/) is used to add layers to the network architecture as well as train and inference the model. A fully connected network structure with three layers is used for this scenario and are defined using the [Dense](https://keras.io/api/layers/core_layers/dense/) class. The Dense class allows specifiation of the number of neurons and the activation function. The first two layers' output is defined by a rectified linear unit activation function or "ReLU". A Sigmoid function defines the output layer. This ensures the output is a `0` or `1` which snaps a hard classification of either class with a default threshold of 0.5. The optimizer that is used is the efficient stochastic gradient descent algorithm [Adam](https://ruder.io/optimizing-gradient-descent/index.html#adam). The model is trained by calling the `fit()` function on the data. The number of epochs<sup>1</sup> is set to 150 while the batch size<sup>2</sup> is set to 10. Evaluation by the function `evaluate()` can generate a prediction for each input and output pair and collect data such as average loss and other metrics configured. "Accuracy" is one other metric that has been configured. Finally, the made predictions are printed and compared to the expected output.

`pima-natives-diabetes.csv` is

***

## Executing and Understanding the Output

**EXECUTION:**
> python pima_diabetes_keras_model.py

Explanation
