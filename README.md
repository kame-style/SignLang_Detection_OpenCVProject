## SignLang_Detection_OpenCVProject

# Requirements 
>python
>Sklearn (scipy, matplotlib)
>open-cv python
>mediapipe

Use command "pip install lib_name" to install above libraries

# Step 1 
>Collecting images of different letters in separate directories
# Step 2
>Create data set by processing the images collected. Using the library mediapipe we detect the hand and place landmarks on the hand for crucial points.
>Create list of data containing these landmark positions in (x,y) coordinate form and lables for each image
# Step 3
>Trainging the random forest classifier with the data set
# Step 4
>Making the predictions with the test data set
