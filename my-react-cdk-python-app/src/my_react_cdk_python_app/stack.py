from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_route53 as route53,
    aws_route53_targets as targets,
    aws_s3_deployment as s3_deployment,
)

class MyReactCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket for the React app
        bucket = s3.Bucket(self, 
            "ReactAppBucket",
            website_index_document="index.html",
            public_read_access=True
        )

        # Create a Route 53 hosted zone for the domain
        hosted_zone = route53.HostedZone.from_lookup(self, 
            "HostedZone",
            domain_name="thebeamers.ca"
        )

        # Create a Route 53 record for the S3 bucket
        route53.ARecord(self, 
            "AliasRecord",
            zone=hosted_zone,
            record_name="thebeamers.ca",
            target=route53.RecordTarget.from_alias(targets.BucketWebsiteTarget(bucket))
        )

        # Deploy the React app to the S3 bucket
        s3_deployment.BucketDeployment(self, 
            "DeployReactApp",
            sources=[s3_deployment.Source.asset("../react_app/build")],
            destination_bucket=bucket
        )