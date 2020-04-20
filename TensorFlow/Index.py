#pip install tensorflow
import pandas as pd

df = pd.read_csv("california_housing_train.csv", sep=",")

import numpy as np

df = df.reindex(np.random.permutation(df.index)) #randomizing data
df['median_house_value']/=1000.0 #scale median_house_value to be in units of thousands
#print (df.describe())

# Define the input feature: total_rooms.
my_feature = df[["total_rooms"]]

import tensorflow as tf
# Configure a numeric feature column.
feature_columns = [tf.feature_column.numeric_column("total_rooms")] #Feature columns store only a description of the feature data; they do not contain the feature data itself.

#define label/target
target = df['median_house_value']

# Use gradient descent as the optimizer for training the model.
my_optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.0000001)

#apply gradient clipping to ensure that magnitude of gradient does not become too large
my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)

# Configure the linear regression model with our feature columns and optimizer.
linear_regressor = tf.estimator.LinearRegressor(feature_columns=feature_columns, optimizer=my_optimizer)

from tensorflow.python.data import Dataset

def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    """Makes a batch of input data and trains a linear regression model of one feature.
  
    Args:
      features: pandas DataFrame of features
      targets: pandas DataFrame of targets
      batch_size: Size of batches to be passed to the model
      shuffle: True or False. Whether to shuffle the batch data.
      num_epochs: Number of epochs for which batch data should be repeated. None = repeat indefinitely
    Returns:
      Tuple of (features, labels) for next data batch
    """
  
    # Convert pandas data into a dict of np arrays.
    features = {key:np.array(value) for key,value in dict(features).items()}                                           
 
    # Construct a dataset, and configure batching/repeating.
    ds = Dataset.from_tensor_slices((features,targets)) # warning: 2GB limit
    ds = ds.batch(batch_size).repeat(num_epochs) #just one row entry makes up the batch
    
    # Shuffle the data, if specified.
    if shuffle:
      ds = ds.shuffle(buffer_size=10000)
    
    # Return the next batch of data.
    features, labels = ds.make_one_shot_iterator().get_next() #use the next batch
    return features, labels
