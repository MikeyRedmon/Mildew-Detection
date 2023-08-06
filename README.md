# Mildew Dectection Algorithm

![The splashscreen for the mildew detection application](./splashscreen.png)

Please find a link to the live application ![here](https://p5-mildew-dectection-3edca557477c.herokuapp.com/)

## Planning Phase

### Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

### **Project Goal:**

- 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.
- 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.

## Hypothesis and how to validate?

- The tree leaves that have pwdery mildew contains white streaks on them.
  - conventional data analysis will be used to conduct a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.

## Rationale to map the business requirements to the Data Visualizations and ML tasks

- **Business Requirement 1**: Data Visualization
  In order to visually differentiate healthy and mildew-infested cherry leaves:

  - As a client I want to display the "mean" and "standard deviation" images for cherry leaves that are healthy and cherry leaves that contain powdery mildew.
  - As a client I want to display the differences between an average healthy cherry leaf and a cherry leaf that has powdery mildew.
  - As a client I want to display an image montage for healthy cherry leaf and mildew-infested leaf.

- **Business Requirement 2**: Classification
  - As a client I want to predict if a given cherry leaf is healthy or contains powdery mildew so that I do not supply the market with a product of compromised quality.
  - As a client I want to build a binary classifier and generate reports.

## ML Business Case

- As a client I want a ML model to predict if the cherry leaf tree is healthy or has powdery mildew.
- The ideal outcome is provide Farmy & Foods with a faster and reliable mildew detection mechanism that is readily scalable across the multiple farms in the country
- The model success metric are:
  - A study showing how to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
  - The capability to predict if a cherry leaf is healthy or contains powdery mildew.
  - The model accuracy on test data is 97%

## Data Understanding

The data is labelled image data split into two folders, each representing the image label. For example, so healthy labelled leaves images are in the healthy directory, while the mildew leaves are in the powder_mildew directory.

The classification dataset included 4208 records (2104 healthy leaves and 2104 infected leaves) was a balanced dataset.

## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick Project Summary

- A project summary page, showing the project dataset summary and the client's requirements.
- Quick project summary

  - General Information
  - Project Dataset

    - The dataset contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.

  - Business requirements
    - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
    - The client is interested in predicting if a cherry tree is healthy or contains powdery mildew.

### Page 2: Cherry leaf visualizer

- It will answer business requirement 1
  - Lists the findings related to the study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
  - Checkbox 1 - Difference between average and variability image
  - Checkbox 2 - Differences between Healthy and Powdery Mildew Cherry Leaves
  - Checkbox 3 - Image Montage

### Page 3: Mildew detector

- It will answer business requirement 2
  - Link to download a set of cherry leaf images for live prediction
  - file upload widget to upload one or more images for prediction
  - Display image and prediction statement indicating whether or not a cherry leaf conatins mildew
  - Display table with image name and prediction result
  - Download button to download table

### Page 4: Project Hypothesis and Validation

- Display each project hypothesis and validation

### Page 5: ML performance metrics

- A technical page displaying the model performance

## **Features**

The application is designed using streamlit library. It is has a sidebar menu with five navigation links.

**Navigation** The dashboard developed is a multipage streamlit application with sidebar navigation checkbox links. The navigation links provides quick access to the five pages listed:

- **Page 1: Quick Project Summary**
  This page displays a brief overview of the project requirements and the dataset

- **Page 2: Cherry leaf visualizer**
  This page displays a brief overview of the project requirements and the dataset

- **Page 3: Mildew Detector**
  This provides the interface for the user to upload test samples and predict wether or not the samples provided are healthy or infested with powdery leaf mildew. It features a _Browse file_ button which user can use to upload one or more image files. Prediction is not made until the user clicks on the _Make Prediction_ button. The image uploaded as well as the prediction and report is displayed to the user when the prediction is complete

- **Page 4: Hypothesis and Visualization**
  This page shows the project hypothesis and how it is validated across the project.

- **Page 5: ML Performance Metric**
  Technical information about the model and data are displayed on this page. It shows the:
  - label frequencies of the train, validation and test datasets
  - training model accuracy and loss charts
  - generalised performance on the test sets

## Deployment

Steps I took to setup environment and deploy to Heroku

### Workspace Setup

The repository for this project was created off the [template](https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves) provided by Code Institute and GitPod workspace was used to develop this project.

- Click the `Use This Template` button.
- Add a repository name and brief description.
- Click the `Create Repository from Template` to create your repository.
- Click `Gitpod` to create a Gitpod workspace.
- To return to the current workspace, login to your gitpod acoount and open the workspace created earlier, since clicking on GitPod button on the GitHub page creates a new workpspace each time.

_Cloning the GitHub Repository_

Cloning your repository will enable you to work on a local version of the repository.

1. Locate the [project repository](https://github.com/MikeyRedmon/Mildew-Detection)
2. Press the arrow on the Code button
3. To clone the repository using HTTPS, copy the [link](https://github.com/MikeyRedmon/Mildew-Detection) that is shown in the drop-down
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned created
6. In the terminal type `git clone` and then paste the link you copied in step 3
   `git clone https://github.com/MikeyRedmon/Mildew-Detection`
7. Press enter and your local clone will be created.

### Creating Heroku App

The Python version in the project is set to 3.8.13, which is not supported by Heroku's current default stack, heroku-22.
As a result of the above, the app was created from Heroku CLI and set to use buildstack heroku-20.

Steps take to create the app is as follows:

1. download and install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) if not already installed
2. Copy API key from heroku
   - sign in and click on the avatar icon and select **Account Settings**
   - Scroll down to the API Key section and click **Reveal** button, and copy key displayed.
3. login to Heroku via the console and enter your details when prompted
   `heroku login -i`
   - enter key copied from step 2 when prompted for password
4. create the app
   `heroku apps:create pp5-mildew-detection --stack heroku-20`

   ### Deploying to Heroku

5. Sign in to Heroku
6. Select app
7. At the Deploy tab, select GitHub as the deployment method.
8. Select your repository name and click Search. Once it is found, click Connect.
9. Select the branch you want to deploy, then click Deploy Branch.
10. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.

## Technologies Used

### Main Data Analysis and Machine Learning Libraries

- [TensorFlow](https://www.tensorflow.org/overview) - used during image preprocessing to filter out corrupt images.
- [Keras](https://keras.io/) - used for the CNN model
- [joblib](https://pypi.org/project/joblib/) for saving and loading image shape
- [numpy](https://numpy.org/) - used for array manipulation.
- [pandas](https://pandas.pydata.org/) - used to structure the data
- [matplotlib](https://matplotlib.org/) For creating the charts and plots for data visaulization
- [seaborn](https://seaborn.pydata.org/) Used in conjuction with matplotplib for data visualization
- [plotly](https://plotly.com/) - used for ploting charts for data visualization
- [streamlit](https://streamlit.io/) For the dashboard development
- [scikit-learn](https://scikit-learn.org/stable/) - used for data processing
- [jupyter notebook](https://jupyter.org) - used for writing and running the ML pipelines

### OtherFrameworks, Libraries & Programs Used

- [Git](https://git-scm.com/) - used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub:](https://github.com/) - used to store the projects code after being pushed from Git.
- [Balsamiq:](https://balsamiq.com/) - Balsamiq was used to create the Dashboard [wireframes](docs/project_wireframe.pdf) during the design process.
- [Heroku](https://www.heroku.com/) - Deployment platform for the project
- [GitPod](https://www.gitpod.io/) - Workspace used for the project
- [AmIResponsive](http://ami.responsivedesign.is/) - Used to generate responsive image used in README file.
