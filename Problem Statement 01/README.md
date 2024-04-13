## Titles
Containerisation and Deployment of Wisecow Application on Kubernetes 

## Project Repository
Wisecow App - https://github.com/nyrahul/wisecow 

## Objective
To containerize and deploy the Wisecow application, hosted in the above-mentioned GitHub repository, on a Kubernetes environment with secure TLS communication.

## Requirements
    1. Dockerization: 
       ● Develop a Dockerfile for creating a container image of the Wisecow application.
       
    2. Kubernetes Deployment:
       ● Craft Kubernetes manifest files for deploying the Wisecow application in a Kubernetes environment.
       ● The Wisecow app must be exposed as a Kubernetes service for accessibility.
    
    3. Continuous Integration and Deployment (CI/CD):
       ● Implement a GitHub Actions workflow for:
       ● Automating the build and push of the Docker image to a container registry whenever changes are committed to the 
         repository.
       ● Continuous Deployment [Challenge Goal]: Automatically deploy the updated application to the Kubernetes environment 
         following successful image builds.
         
    4. TLS Implementation [Challenge Goal]:
       ● Ensure that the Wisecow application supports secure TLS communication.
       
    5. Expected Artifacts:
       ● A private GitHub repository containing:
       ● The Wisecow application source code.
       ● The Dockerfile for the application.
       ● Kubernetes manifest files for deployment. 
       ● The CI/CD pipeline configuration.
       ● A GitHub Actions workflow file for facilitating Continuous Build and Deployment (CI/CD)

     6. Access Control:
        ● The GitHub repository should be set to public.
