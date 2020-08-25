# JAKE (Just Another Kar classifiEr)
Unfortunately, car does not start with a K, but that will not stop us from using the JAKE acronym.

## Architecture
Jake uses an application factory approach. It is a ready application to be deployed on Heroku.

**main:** This directory contains all the logic for the app in the functions file. The view file handles all request and template rendering. In the index route of the app "/", the application removes any images from the images directory located in the static directory. When a "POST" request is received, the app will check to make sure there is an image incoming, it will then extract the image, rename it to 'test_image', save it to the images directory, and redirect the user to the results page. The results route will check to make sure there is an image in the images directory. If there are no images in the directory, it will redirect the user to the index route. If there is an image, it will retrieve the image path, prepare it for the model, use the model to predict the category, generate a message with the probability of the image pertaining to each category, and it will retrieve the image to be displayed. 

**static:** The static directory holds the CSS file, and it contains an images directory. Finally, the images directory contains the a_ignore.txt file. This file does not contain anything, but it is placed there because Heroku will not generate the directory if it is empty.

**templates:** contains the html templates to be render by the views file under the main directory.

**flaskModel.h5** The smaller network in greyscale was used to power this app. It can be found in the jupyter notebook under the cars directory.


