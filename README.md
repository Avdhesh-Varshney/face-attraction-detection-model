<h1 align='center'>💥 Face Attraction Detection Model 💥</h1>

<div align='center'>

### :zap: **TECH STACK USED**

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)

</div>

### :zap: **GOAL** 

- The aim of the project is doing image processing and predict how much attract is the face in the image.

### :zap: **DATASET** 

- Description of the Dataset and Kaggle [Link](./Dataset/README.md)


![Line](https://github.com/Avdhesh-Varshney/WebMasterLog/assets/114330097/4b78510f-a941-45f8-a9d5-80ed0705e847)


### :zap: **LIBRARIES NEEDED**

1. Pandas 
2. Numpy 
3. Matplotlib 
4. Sklearn 
5. Sci-py 
6. Seaborn 
7. Flask 
8. Tensorflow 
9. Keras 


### :zap: **HOW TO USE IT**

* Create a virtual environment using `python -m venv myenv`.
* To activate the virtual environment use `.\myenv\Scripts\activate`.
* If error occurs, use `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.
* Now, app.py is the flask app code. run the command `pip install -r requirements.txt` to install the required dependencies for the flask app.
* You may need to install additional libraries for running the jupyter notebooks.
* Upload the model file on Google Colab and put the Kaggle API key json file on Google Drive homepage then run the code.
* Finally, download the updated weights file of highest accuracy model like `weights.best.inc.attractive.hdf5` is of Inception V3 Model weights file goes around 185 MB.
* Link it with the `app.py` file and start the python file.


### :zap: **WHAT I HAVE DONE**

* First I imported all the required libraries and dataset for this project.
* Perfoming the EDA on the whole dataset.
* Chosing 1 target feature i.e., `Attractiveness`.
* Converting all -1 values into 0 values as negative instances.
* Visualizing the dataset distribution in univariate and bivariate with target feature.
* Splitting the dataset into training, validation and testing set as given in `list_eval_partition.csv` file.
* Due to high amount of dataset and uniform distribution of dataset for training, i will chose small amount from it for training, validation and testing purpose.
* Pre-processing the images i.e., Data augmentation so that model will able to predict easily on any dimension of image like inverted, or at any angle of rotation, etc and model is able to learn from these type of variation in the images.
* Finally, start building the different models like inceptionV3 model, resnet50 model, and resnet101V2 models by freezing the some of the layers of them.
* At the end, Adding some fully connected layers by own for classification problem of the model.
* Train the model and plot the accuracy and loss of the model on test dataset.


### :zap: **MODELS USED**

| Models Used    | Accuracy |
|----------------|----------|
| Inception V3   | 68.80%   |
| ResNet-50      | 50.20%   |
| ResNet-101 V2  | 62.13%   |


### :zap: **Visualization and EDA of different attributes**

<table align='center'>
  <tr align='center'>
    <td align='center'>
      <img alt="graph" width="500" height="300" src="/static/images/Attractive_distribution.png" >
    </td>
    <td align='center'>
      <img alt="graph" width="500" height="300" src="/static/images/data_augmentation.png" >
    </td>
  </tr>

  <tr align='center'>
    <td align='center'>
      <img alt="graph" width="500" height="300" src="/static/images/lefteye_x_and_lefteye_y.png" >
    </td>
    <td align='center'>
      <img alt="graph" width="500" height="300" src="/static/images/righteye_x_and_righteye_y.png" >
    </td>
  </tr>

  <tr align='center'>
    <td align='center'>
      <img alt="graph" width="500" height="300" src="/static/images/leftmouth_x_and_leftmouth_y.png" >
    </td>
    <td align='center'>
      <img alt="graph" width="500" height="300" src="/static/images/rightmouth_x_and_rightmouth_y.png" >
    </td>
  </tr>

  <tr align='center'>
    <td align='center'>
      <img alt="graph" width="500" height="300" src="/static/images/width_and_height.png" >
    </td>
    <td align='center'>
      <img alt="graph" width="500" height="300" src="/static/images/x_1_and_y_1.png" >
    </td>
  </tr>

  <tr align='center'>
    <td align='center'>
      <img alt="graph" width="500" height="300" src="/static/images/nose_x_and_nose_y.png" >
    </td>
  </tr>

</table>

#### :zap: InceptionV3

![graph](/static/images/accuracy_inception.png)
![graph](/static/images/loss_function_inception.png)


#### :zap: ResNet50

![graph](/static/images/accuracy_resnet50.png)
![graph](/static/images/loss_function_resnet50.png)


#### :zap: ResNet101V2

![graph](/static/images/accuracy_resnet101v2.png)
![graph](/static/images/loss_function_resnet101v2.png)


### :zap: **CONCLUSION**

- InceptionV3 Model showing promising performance with **68.80%** accuracy of the model.
- Created a user-friendly front-end framework using **FLASK** and integrate it to the model.

#### :zap: **OUTPUTS**

<table align='center'>
  <tr align='center'>
    <td align='center'>
      <img alt='Pass' src='/static/images/test-1.jpg' >
    </td>
    <td align='center'>
      <img alt='Pass' src='/static/images/test-1_input.jpg' >
    </td>
    <td align='center'>
      <img alt='Pass' src='/static/images/test-1_output.png' >
    </td>
  </tr>
  <tr align='center'>
    <td align='center'>
      <img alt='Fail' src='/static/images/test-2.jpg' >
    </td>
    <td align='center'>
      <img alt='Fail' src='/static/images/test-2_input.png' >
    </td>
    <td align='center'>
      <img alt='Fail' src='/static/images/test-2_output.png' >
    </td>
  </tr>
</table>


![Line](https://github.com/Avdhesh-Varshney/WebMasterLog/assets/114330097/4b78510f-a941-45f8-a9d5-80ed0705e847)

<div align="center">

### :zap: **PROJECT CREATOR & ADMIN**

  <table>
  <tr>
    <td align="center">
      <a href="https://github.com/Avdhesh-Varshney">
        <img src="https://github.com/Avdhesh-Varshney/CPMasterLog/assets/114330097/0b13fac7-e59d-40be-ac14-b76a28174e85" width=185px height=175px />
      </a></br> 
      <h4 style="color:red;"><a href="https://github.com/Avdhesh-Varshney">Avdhesh Varshney</a></h4>
      <a href="https://www.linkedin.com/in/avdhesh-varshney-5314a4233/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
      </a>
  </tr>
  </table>

</div>


![Line](https://github.com/Avdhesh-Varshney/WebMasterLog/assets/114330097/4b78510f-a941-45f8-a9d5-80ed0705e847)

<div align="center">
  <h3>Show some &nbsp;❤️&nbsp; by &nbsp;🌟&nbsp; this repository!</h3>
  <img src="https://media.giphy.com/media/LnQjpWaON8nhr21vNW/giphy.gif" width="60"> <em><b>I love connecting with different people</b> so if you want to say <b>hi, I'll be happy to meet you more!</b> :)</em>
</div>

<a href="#top"><img src="https://img.shields.io/badge/-Back%20to%20Top-red?style=for-the-badge" align="right"/></a>

