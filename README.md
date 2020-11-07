![Python application test with Github Actions](https://github.com/bobfoster1299/building-a-cicd-pipeline2/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)

By Rob Foster

Updated 07/11/2020

# Introduction
This is my submission for the 'Building a CI/CD Pipeline' project as part of the 'DevOps Engineer for Microsoft Azure' nanodegree program from [Udacity](https://udacity.com).

It does the following:
- Creates a App Service in Azure.
- Tests code when it is pushed to GitHub.
- In Azure DevOps the code is then tested and deployed to the App Service.

See [trello](https://trello.com/b/CjgPIZxU/building-a-ci-cd-pipeline).

[Spreadsheet](project-management-template.xlsx) of project plan

Architectural diagram

Screenshots demonstrating key steps

Description on how to improve the project further

YouTube video








# Instructions

## Continuous integration
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
python3 app.py
```

Open a separate Cloud Shell and test that the app is working:
```
./make_prediction.sh
```

The output should match the below:
![screenshot-make_prediction.png](screenshots/screenshot-make_prediction.png)





## Continuous delivery

Screenshot of the App Service in Azure:
![screenshot-app_service.png](screenshots/screenshot-app_service.png)

Screenshot of successful prediction against the app running in Azure App Service:
![screenshot-make_predict_azure_app.png](screenshots/screenshot-make_predict_azure_app.png)

Screenshot of a successful run of the project in Azure Pipelines:
![screenshot-azure_pipeline_success.png](screenshots/screenshot-azure_pipeline_success.png)


## Create the App Service

Clone the repo:
```
git clone git@github.com:bobfoster1299/building-a-cicd-pipeline2.git
```

Change into the new directory:
```
cd building-a-cicd-pipeline2
```

Login to Azure:
```
az login
```

Create an App Service in Azure. In this example the App Service is called rob-udacity-webapp and the resource group is called rob-udacity-project:
```
az webapp up -n rob-udacity-webapp -g rob-udacity-project
```

## Create the Azure DevOps pipeline

These are the basic steps you need to follow to set up the pipeline in Azure DevOps (more information on this process can be found [here](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops&WT.mc_id=udacity_learn-wwl)):

- Go to [https://dev.azure.com](https://dev.azure.com) and sign in.
- Create a new private project.
- Under Project Settings create a new service connection to Azure Resource Manager, scoped to your subscription and resource group.
- Create a new pipeline linked to your GitHub repo.

## CI/CD

Whenever the code is updated and pushed to GitHub, the following will happen:
- GitHub Actions will test the code.
- Azure DevOps will also test the code.
- If the build is successful it will be deployed to the Azure App Service.

To test the app, edit line 28 of the make_predict_azure_app.sh script with the DNS name of your app. Then run the script:
```
./make_predict_azure_app.sh 
```

If it's working you should see the following output:
```
Port: 443
{"prediction":[20.35373177134412]}
```

You can also visit the URL, e.g. [https://rob-udacity-webapp.azurewebsites.net](https://rob-udacity-webapp.azurewebsites.net) via the browser and you should see the following page:

![screenshot-browser.png](screenshots/screenshot-browser.png)


