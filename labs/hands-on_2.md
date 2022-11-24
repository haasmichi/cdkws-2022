# Hands-on Part 2

In this part you're going to prepare your AWS Account for cdk deployments and deploy your first service/constructs.

---

1. The `cdk init` command already created a first stack file for you. Uncomment lines in this stack file in order to create a SQS queue. 

2. The output states there are some useful cdk commands.

    ```
     * `cdk ls`          list all stacks in the app
     * `cdk synth`       emits the synthesized CloudFormation template
     * `cdk deploy`      deploy this stack to your default AWS account/region
     * `cdk diff`        compare deployed stack with current state
     * `cdk docs`        open CDK documentation
    ```
   
    Use the commands to synthesize, check and deploy the SQS service to your AWS Account.  

3. Take a look at the API documentation for [S3](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_s3.html) and create a S3 Bucket within your existing stack and deploy it.

    Add these bucket properties:
    - Block public access
    - SSE (Server Side Encryption)
    - Delete bucket, when stack is deleted. (Hint: Look for "removal policy" property)

