# Hands-on Part 3

In this part you will develop and deploy some more services to your AWS Account.

1. Clone the workshop repo somewhere outside your CDK App working directory. `cd && git clone https://haasmichi.com/`
2. Create an asset folder, e.g. `lambda_funcs` in your CDK App directory and copy the Lambda Function,
   lambda_trigger.py, to the asset folder. The Lambda Function should look like this.

    ```python
    import boto3
    import os


    def handler(event, context):
        crawler_name = (os.environ['GLUE_CRAWLER'])

        try:

            # Log the event
            client = boto3.client('glue')
            print(f'Starting Crawler {crawler_name}')
            response = client.start_crawler(Name=crawler_name)

            return response

        except Exception as e:
            print(e)
            raise e
    ```

2. Copy s3_glue_stack.py to your stack subfolder within your CDK App working directory.

3. Edit your `app.py` to also include the S3GlueStack.

4. Deploy the S3GlueStack. (You will have to fix several errors.)

5. If the deployment is successful, look at the output and find the name of the S3 bucket created.

6. Download the csv-file from TODO: https:// and upload it to the S3 bucket mentioned at step 5.
```
curl -LO https://...
aws s3 cp file.csv s3://NAME_OF_BUCKET
```
7. See the Glue Crawler do its work.

8. Open the Athena service and do some SQL magic.
