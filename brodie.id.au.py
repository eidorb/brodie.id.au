"""Defines brodie.id.au website infrastructure using AWS CDK."""
from pathlib import Path

import aws_cdk as cdk
import aws_cdk.aws_certificatemanager as acm
import aws_cdk.aws_cloudfront as cloudfront
import aws_cdk.aws_cloudfront_origins as cloudfront_origins
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_s3_deployment as s3_deployment
import aws_cdk.aws_route53 as route53
import aws_cdk.aws_route53_targets as route53_targets


# Path to sphinx-build output, relative to this module.
build_path = Path(__file__).parent / "brodie.id.au/_build"


class App(cdk.App):
    def __init__(self) -> None:
        super().__init__()
        Website(self, id="Website")


class Website(cdk.Stack):
    """brodie.id.au website stack."""

    def __init__(self, scope, id: str) -> None:
        super().__init__(scope, id, description="brodie.id.au website")

        # This bucket contains static website files.
        bucket = s3.Bucket(
            scope=self,
            id="Bucket",
        )

        # Populate bucket with files from build directory (relative to this module).
        s3_deployment.BucketDeployment(
            scope=self,
            id="BucketDeployment",
            destination_bucket=bucket,
            sources=[s3_deployment.Source.asset(str(build_path))],
        )

        # Reference existing hosted zone.
        hosted_zone = route53.HostedZone.from_hosted_zone_attributes(
            scope=self,
            id="HostedZone",
            hosted_zone_id="Z0932427366G4DNP1CWB",
            zone_name="brodie.id.au",
        )

        # CloudFront distribution certificates must be in region us-east-1.
        certificate = acm.DnsValidatedCertificate(
            scope=self,
            id="Certificate",
            hosted_zone=hosted_zone,
            region="us-east-1",
            domain_name="brodie.id.au",
        )

        # Create a CloudFront distribution that serves content from our S3 origin.
        distribution = cloudfront.Distribution(
            scope=self,
            id="Distribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=cloudfront_origins.S3Origin(bucket),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            certificate=certificate,
            default_root_object="index.html",
            domain_names=["brodie.id.au"],
        )

        # Create an alias record for the CloudFront distribution.
        route53.ARecord(
            scope=self,
            id="Alias",
            target=route53.RecordTarget.from_alias(
                route53_targets.CloudFrontTarget(distribution)
            ),
            zone=hosted_zone,
            record_name="brodie.id.au",
        )


if __name__ == "__main__":
    App().synth()
