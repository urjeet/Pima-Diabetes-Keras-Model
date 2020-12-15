# Predicting Diabetes in Pima Native Americans Using Keras
***
My first Deep Learning project, I used Keras and TensorFlow to train and evaluate a neural network that can predict diabetes in Pima Native Americans given several other factors. I followed a [tutorial](https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/) for this project, however, it has been modified.

*Program Written in December 2020*  
*Pushed to Github in December 2020*

***

## Source Files and Their Roles

`pima_diabetes_keras_model.py` is driver program that loads the dataset, defines a Keras model, compiles the Keras model, fits the Keras model on the dataset, evaluates the Keras model, and finally makes class predictions with the model on the already seen dataset. [Sequential](https://keras.io/api/models/sequential/) is used to add layers to the network architecture as well as train and inference the model. A fully connected network structure with three layers is used for this scenario and are defined using the [Dense](https://keras.io/api/layers/core_layers/dense/) class. The Dense class allows specifiation of the number of neurons and the activation function. The first two layers' output is defined by a rectified linear unit activation function or "ReLU". A Sigmoid function defines the output layer. This ensures the output is a `0` or `1` which snaps a hard classification of either class with a default threshold of 0.5. The optimizer that is used is the efficient stochastic gradient descent algorithm [Adam](https://ruder.io/optimizing-gradient-descent/index.html#adam). The model is trained by calling the `fit()` function on the data. The number of epochs<sup>1</sup> is set to 150 while the batch size<sup>2</sup> is set to 10<sup>3</sup>. Evaluation by the function `evaluate()` can generate a prediction for each input and output pair and collect data such as average loss and other metrics configured. "Accuracy" is one other metric that has been configured. Finally, the made predictions are printed and compared to the expected output.

`pima-natives-diabetes.csv` is the main data set used to predict diabetes in the Pima Native Americans.   
The input variables (x) include:
  1. Number of pregnancies
  2. Plasma glucose concentration
  3. Diastolic blood pressure (mm Hg)
  4. Triceps skin fold thickness (mm)
  5. 2-Hour serum insulin (mu U/mL)
  6. Body mass index (weight in kg / (height in m)<sup>2</sup>)
  7. Diabetes pedigree function
  8. Age (years)

The output variable (y) is:
  1. Class variable (0 or 1) where 1 denotes positive for diabetes

The dataset features subjects in rows and each variable in the columns, including the output variable in the last column.   
**[Click here for more details regarding the dataset](https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.names)**

***

## Executing and Understanding the Output

**EXECUTION:**
> python pima_diabetes_keras_model.py

The default `tensorflow` pip package contains both CPU and GPU versions. The output will produce warnings if the correct CUDA version is not found and will fall back on a CPU-only mode. If you would also like to use GPU, please correctly download and install the necessary CUDA libraries. The output will show each epoch and its corresponding loss and accuracy factors. A final accuracy of the model on the dataset will be printed. Lastly, a the input data, predicted class and expected class for the first five examples in the dataset are printed. This shows a comprehensive picture of accuracy of the model. 

***

## Footnotes

[1]: One pass through all of the rows in the training dataset.  
[2]: One or more samples considered by the model within an epoch before weights are updated.  
[3]: One epoch is comprised of one or more batches, based on the chosen batch size and the model is fit for many epochs.
