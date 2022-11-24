# Hands-on Part 1

To get comfortable with the CDK, you will initialize a CDK application project, have a look at the files and test several cdk commands. Before you start, ensure, you are using the correct AWS profile.

## Cloud 9

Log in to your AWS environment using the startpage, https://btelligent.awsapps.com/start#/.  
For performance reasons change to the Frankfurt region (eu-central-1).
After that, create a new Cloud9 environment. Give your environment a decent name, e.g. "workshop", and choose t3.small as your instance type.  
Leave all other settings as is.

The rest of the steps will be done within your Cloud9 environment.

## Initialize a cdk project

1. Create a folder called `cdk_workshop` in your Cloud9 environment. This will be your working directory for the rest of the workshop.

2. Change into that folder and create a cdk application: `cdk init --language-python`. 

3. Look at the output and the created files, particularly app.py and cdk_workshop/cdk_workshop_stack.py.

4. Activate the created virtual environment and install the dependencies.

    ```shell
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

5. Bootstrap your cdk environment on your aws account: `cdk bootstrap`.

6. Look at the output and the CloudFormation service of your AWS account (WebUI). What happened?
