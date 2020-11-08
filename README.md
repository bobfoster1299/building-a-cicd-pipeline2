![Python application test with Github Actions](https://github.com/bobfoster1299/building-a-cicd-pipeline2/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)

By Rob Foster

Updated 07/11/2020

# Introduction
This is my submission for the 'Building a CI/CD Pipeline' project as part of the 'DevOps Engineer for Microsoft Azure' nanodegree program from [Udacity](https://udacity.com).

This project contains a python application that is designed to predict housing prices in Boston (I did not create the python app myself). This repo will enable you to:
- Deploy the app in Azure CloudShell
- Deploy the app as an Azure App Service

Any commits to the GitHub repo trigger automated code testing using GitHub Actions. A pipeline has been created in Azure DevOps, and the updated code is also automatically tested in Azure DevOps and deployed to the Azure App Service. 

Here is an architectural diagram:
![architectural-diagram.png](architectural-diagram.png)

A [Trello](https://trello.com/b/CjgPIZxU/building-a-ci-cd-pipeline) board has been created to keep track of tasks to be completed.

A [spreadsheet](project-schedule.xlsx) has been created to manage the project schedule.

See [here](https://youtu.be/GQo55aCXXYo) for a YouTube video demonstrating the project.

# Instructions

## Deploy the app in Azure Cloud Shell
In Azure Cloud Shell, clone the repo:
```
git clone git@github.com:bobfoster1299/building-a-cicd-pipeline2.git
```
![screenshot-git_clone.png](screenshots/screenshot-git_clone.png) 

Change into the new directory:
```
cd building-a-cicd-pipeline2
```

Create a virtual environment:
```
make setup
```

Activate the virtual environment:
```
source ~/.udacity-devops/bin/activate
```

Install dependencies in the virtual environment and run tests:
```
make all
```
![screenshot-make_all.png](screenshots/screenshot-make_all.png) 

Start the application in the local environment:
```
python app.py
```

Open a separate Cloud Shell and test that the app is working:
```
./make_prediction.sh
```

The output should match the below:

![screenshot-make_prediction.png](screenshots/screenshot-make_prediction.png)





## Deploy the app to an Azure App Service

Create an App Service in Azure. In this example the App Service is called rob-udacity-webapp and the resource group is called rob-udacity-project:
```
az webapp up -n rob-udacity-webapp -g rob-udacity-project
```

Next, create the pipeline in Azure DevOps. More information on this process can be found [here](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops&WT.mc_id=udacity_learn-wwl). The basic steps to set up the pipeline are:

- Go to [https://dev.azure.com](https://dev.azure.com) and sign in.
- Create a new private project.
- Under Project Settings create a new service connection to Azure Resource Manager, scoped to your subscription and resource group.
- Create a new pipeline linked to your GitHub repo.

Screenshot of the App Service in Azure:

![screenshot-app_service.png](screenshots/screenshot-app_service.png)

Screenshot of a successful run of the project in Azure Pipelines:

![screenshot-azure_pipeline_success.png](screenshots/screenshot-azure_pipeline_success.png)

To test the app running in Azure App Service, edit line 28 of the make_predict_azure_app.sh script with the DNS name of your app. Then run the script:
```
./make_predict_azure_app.sh 
```

If it's working you should see the following output:

![screenshot-make_predict_azure_app.png](screenshots/screenshot-make_predict_azure_app.png)

You can also visit the URL of the App Service via the browser and you should see the following page:

![screenshot-browser.png](screenshots/screenshot-browser.png)

View the app logs:
```
az webapp log tail -g rob-udacity-project --name rob-udacity-webapp
```
![screenshot-logs.png](screenshots/screenshot-logs.png)

## Load testing

We can use locust to do a load test against our application. In this example we will do a load test against the app running locally rather than in Azure. 

Install locust:
```
pip install locust
```
Ensure the app is running:
```
python app.py
```

Start locust:
```
locust
```
Open a browser and go to [http://localhost:8089](http://localhost:8089). Enter the total number of users to simulate, spawn rate, set the host to localhost:5000, and click Start Swarming:

![screenshot-locust-main-page.png](screenshot-locust-main-page.png)

You can then watch the load test:

![screenshot-locust.png](screenshot-locust.png)







## Future improvements

Currently, there is only a single branch in GitHub. In the future is would be good to create multiple branches, so code can initially be tested and deployed in a staging environment. If it works correctly in the staging environment the changes could then be merged into the production branch and the code deployed into the production environment.