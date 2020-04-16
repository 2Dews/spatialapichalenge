# Spatial Functions Web Api Sample

A sample Python 3 project to create a basic api deployed in AWS Lambda. 

The project can be ran locally using AWS SAM cli to emulate the Lambda environment. 

There are two available endpoints, one to check the status of the service and one to determine if two geometries intersect.

# Getting Started

## Required software
* [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) - To build and deploy the project to Lambda or local Lambda container.
* [Docker Desktop](https://www.docker.com/products/docker-desktop) - To run the api locally.

## Optional software
* An IDE like [Visual Studio Code](https://code.visualstudio.com/Download) with Python support - for editing code and running tests
* [Postman](https://www.postman.com/downloads/) - for running api requests

## Steps to run api locally
* Open the project folder in Visual Studio Code and open a new terminal.
    * Run `sam build --use-container` this may take a while the first time as Docker may need to download the lambda image.
    * Run `sam local start-api` it should return a message including "You can now browse to the above endpoints to invoke your function."
* Open Postman and import the included 'Sample Api.postman_collection.json' collection file.
    * Run the server status request. The response should include a status 200.
    * Run the Check Intersection - GeoJson request. The response should include a status 200 and an intersects boolean.
* To run the included unit tests locally install the required packages in the desired Python 3 environment using the requiremnts.txt files in the test and spatial_api folders.

## Next Steps
* Add logging
* Test additional geometry types
* Refactor to move logic out of api
* Deploy to AWS 
* Deploy Lambda to AWS with Terraform

## Resources
Some helpful links when working with this sample.
* [Lambda - Flask Api](https://spiegelmock.com/2018/09/06/serverless-python-web-applications-with-aws-lambda-and-flask/)
* [Local AWS Lambda via Docker](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-layer-simulated-docker/)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html)