import aws_cdk as cdk
from constructs import Construct
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_iam as iam
from aws_cdk import aws_glue as glue
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_lambda_event_sources as _lambda_event


class S3GlueStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Setting up S3 Bucket
        s3_landingzone = s3.Bucket(self, f'landingzone_cdk_workshop',
                                   block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                                   encryption=s3.BucketEncryption.S3_MANAGED,
                                   removal_policy=cdk.RemovalPolicy.DESTROY)
        s3_landingzone.add_lifecycle_rule(expiration=cdk.Duration.days(14))
        cdk.Tags.of(s3_landingzone).add('description', 'This bucket is the landingzone of the data lake.')

        # Setting up Glue Crawler Role
        glue_role = iam.Role(self, f'glue_role_cdk_workshop',
                             assumed_by=iam.ServicePrincipal('glue.amazonaws.com'),
                             managed_policies=[
                                 iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSGlueServiceRole')
                             ])

        s3_landingzone.grant_read(glue_role)

        # Setting up the Glue Crawler
        glue_crawler = gluee.CfnCrawler(self, id='crawler_cdk_workshop',
                                       name='crawler_cdk_workshop',
                                       description='Crawl files in landingzone',
                                       role=glue_role.role_arn,
                                       database_name=f'cdk_workshop_db',
                                       table_prefix='landingzone_',
                                       targets={"s3Targets":
                                                    [{"path": f"{s3_landingzone.bucket_name}/"}
                                                     ]})

        # Lambda to trigger Crawler when Object is put in S3
        lambda_func = _lambda.Function(self, 'LambdaTrigger',
                                       runtime=_lambda.Runtime.PYTHON_3_8,
                                       handler='lambda_trigger.handler',
                                       code=_lambda.Code.from_asset('lambda_funcs'),
                                       environment={'GLUE_CRAWLER': glue_crawler.name})

        lambda_func.role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSGlueServiceRolle"))

        # S3 Event Trigger
        lambda_trigger = _lambda_event.S3EventSource(s3_landingzone, events= [
                s3.EventType.OBJECT_CREATED_PUT,
                s3.EventType.OBJECT_CREATED_COMPLETE_MULTIPART_UPLOAD
            ])
        lambda_func.add_eventsource(lambda_trigger)

        # Bucket Name Output
        cdk.CfnOutput(self, "S3BucketName", value=s3_landingzone.bucket_name)
