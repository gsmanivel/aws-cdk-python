from aws_cdk import core as cdk
from aws_cdk import core
from aws_cdk import aws_s3 as _s3

class CdkPythonStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create a db2 bucket
        db2bucket = _s3.Bucket(
                self,
                "db2bucket",
                bucket_name="db2bucket001",
                versioned=True,
                encryption=_s3.BucketEncryption.S3_MANAGED,
                block_public_access= _s3.BlockPublicAccess.BLOCK_ALL,
                removal_policy=core.RemovalPolicy.DESTROY,
                auto_delete_objects= True
                )

        # create a mysqlbucket
        mysqlbucket = _s3.Bucket(
            self,
            "mysqlbucket001",
            bucket_name="mysqlbucket001" ,
            removal_policy= core.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
                       
        )

        bucketOutput_db2 = core.CfnOutput(
            self,
            "db2bucketoutput001",
            value= db2bucket.bucket_name,
            description= f"db2bucket.bucket_arn",
            export_name="db2outputdetails"
        )
