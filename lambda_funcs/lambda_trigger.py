import boto3
import os


def handler(event, context):
    crawler_name = (os.environ['GLUE_CRAWLER'])

    try:

        # Starting crawler with boto3 glue client
        client = boto3.client('glue')
        print(f'Starting Crawler {crawler_name}')
        response = client.start_crawler(Name=crawler_name)

        return response

    except Exception as e:
        print(e)
        raise e
