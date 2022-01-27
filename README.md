# Cloud-Continuous-Delivery-of-Microservice-Project
This Repository has been created for the course IDS 721 Cloud Computing at Scale Individual Project 1. This project illustrates how to create a microservice using Flask, containerize it and deploy it using AWS CodeBuild and AWS AppRunner (Infrastructure as Code).

## Step 1 Creation of a Flask App 

The App has been created in Python to accomplish two tasks as can be seen under:
### (i) Get the Abstract of a Topic on Wikipedia

### (ii) Summarize the Abstract of a Topic on Wikipedia in 10 sentences

## Step 2 Creation of Makefile and Dockerfile

The Makefile runs important housekeeping tasks using the make command in linux. It includes the following:
1. Make install: This step installs software via the make install command
2. Make lint: This step checks for syntax errors via the make lint command
3. Make test: This step runs tests via the make test command

The Dockerfile helps containerize the app when the image is built using the docker build command.

## Step 3 Creation of Build System File

The buildspec.yml file is created to help build the system. It lists down the steps to build the system. For this app, the buildspec.yml file 

## Step 4 Connecting Repo to CodeBuild

This Github Repo is then 

## Step 5 Running the App




The App is then containerized using the docker command as in the buildspec.yml. 

