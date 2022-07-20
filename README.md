<h1>Train-Test-Split</h1>
This is a model validation process testing that how the model will perform on unseen/new data. The problem this process is created is, that there aren't enough new data on the same topic. So, here we do the training and testing by splitting the data into two parts. One is training part and the other one is testing part. So, traditionally speaking the training data will be 75% and the testing part will have 25%. Then, the dataset will be like 'X_train', 'Y_train', 'X_test', 'Y_test'. 

The steps of Train-Test-Split are:
     1. Arrange the data into the acceptable format(Normally this technique needs the data as features and target)
     2. Split those datasets into two pieces which is for training and testing.(Random sampling without replacing is used).
     3. Train the model on the training set.
     4. Test the model in the testing set and evaluate the performance.
     
This image will simply explain the process:
<img src="https://res.cloudinary.com/dbw0cho6v/image/upload/v1658293122/1_AOwsTgJnh_b_oLIAaAn8Bg_axyzz5.png">
