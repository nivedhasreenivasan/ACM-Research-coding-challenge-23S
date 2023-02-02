# ACM Research coding challenge (Spring 2023)


# Problem

The code written aims to predict whether a star in the data set belongs to a specific star type through testing if its magnitude, spectral class, and temperature fall within the accepted range of the star type. In other words, the program calculates star type based on the same parameters used in the hertzsprung-russell diagram to make its prediction. 


---

# Solution

## Prediction

To predict the star type, I first set out to split the data set into separate lists based on spectral class. Then, I placed each list separately into a method called spectral alongside several variables named after the star types meant for keeping track of how many of each star type were found. In this method, I found the maximum and minimum values for both temperature and magnitude for all the star types and used the data to set the expected range for each star type. I then filtered through the list of values for the spectral class and found the star type that each star belongs to and printed all the attributes of the star. Lastly, I incremented the counter variable cooresponding to the star type found. 

## Accuracy

To test whether the prediction is correct, I created a method called accuracyChecker that loops through each spectral class list and counts/stores the number of stars located in each star type based on the corresponding column in the data set. The program then compares the variables incremented in the spectral method with the corresponding accuracyChecker variables. If all the comparisons return true, then the prediction is accurate. 


