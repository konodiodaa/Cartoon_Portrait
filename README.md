# User Manual    
# Cartoon_Portrait
Please download these model before running the program, put the model of female and model of male into the modle directory and face segment model into util directory.  
Cartoon model of female:  https://drive.google.com/file/d/1QMJIceH8cvdB2rcX4e7pfG3QT7iIfkB2/view?usp=sharing  
Cartoon model of male:    https://drive.google.com/file/d/10F7KnsITJKql7f_29Re0bNRqymL2kH6e/view?usp=sharing  
Face segement model:      https://drive.google.com/file/d/1UoEEekc60yNhCwwPhp5fiOkQwG9uweWQ/view?usp=sharing  
Please do not delete directory images.  

# Requirement:  
Python 3.6  
Cuda 10.1 Cudnn >=8.0  
Pytorch >= 1.2  
Tensorflow 1.14  
Opencv  
Numpy  
PyQT5  

# How to run:
Run the UI.py to start the software.  
Male mode button is to open a image in the local directory and transfer that image to cartoon style with male model, then display it.  
Female mode button is to open a image in the local directory and transfer that image to cartoon style with female model, then display it.  
Add background is to open a image in the local directory and select a background image, then blend background image and generated cartoon image.  
Save is to select a local directory and save the generated image at that location.  

# Warning
To ensure the software runs correctly, please upload image larger than 200 * 200. If the image brightness is low, the style transfer result will be bad so please use image with normal brightness. 
The real human photo is used, so please consider the privacy carefully.  
The model of this project cannot be used in Commercial activities.  
