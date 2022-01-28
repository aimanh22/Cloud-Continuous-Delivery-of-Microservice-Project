# Cloud-Continuous-Delivery-of-Microservice-Project
This Repository has been created for the course IDS 721 Cloud Computing at Scale Individual Project 1. This project illustrates how to create a microservice using Flask, containerize it and deploy it using AWS CodeBuild and AWS AppRunner (Infrastructure as Code).

## Step 1 Creation of a Flask App 

The App has been created in Python to accomplish two tasks as under:
### (i) Get the Abstract of a Topic on Wikipedia

### (ii) Summarize the Abstract of a Topic on Wikipedia in 10 sentences

## Step 2 Creation of Makefile and Dockerfile

The Makefile runs important housekeeping tasks using the make command in linux. It includes the following:
1. Make install: This step installs software via the make install command
2. Make lint: This step checks for syntax errors via the make lint command
3. Make test: This step runs tests via the make test command

The Dockerfile helps containerize the app when the image is built using the docker build command.

## Step 3 Creation of Build System File

The buildspec.yml file is created to help build the system. It lists down the steps to do so. For this app, it

#### It logins to the ECR and creates an ECR Repository (if it already doesn't exist)

#### Containerizes the App

#### Pushes the containerized app to the ECR

#### Creates an AppRunner Service for automatically deploying the containerized app using the ECR Image


## Step 4 Connecting Repo to CodeBuild

This Github Repo is then connected to the CodeBuild for Continuous Integration and Deployment each time a new code is pushed to the Github Repo.

## Step 5 Running the App

The App can then be run using the url created by the AppRunner.


