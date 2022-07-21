# brodie.id.au

[brodie.id.au](https://brodie.id.au/) website and infrastructure.

`brodie.id.au.py` defines the website's infrastructure using AWS CDK. It's a CloudFront
distribution serving static website files from an S3 bucket origin. It takes care
of the domain name and certificate too.

`brodie.id.au` contains the website's content. Sphinx is used to build static website
files from this content.

A GitHub workflow (`.github/workflows/deploy.yml`) automatically builds and deploys
the website when changed.
