#!/usr/bin/env python3
import os

from aws_cdk import core as cdk
from aws_cdk import core
from aws_cdk import aws_s3 as _s3

from cdk_python.cdk_python_stack import CdkPythonStack

env_US = core.Environment(account="081920805510", region="us-east-1")

app = core.App()
CdkPythonStack(app, "first-cdk-stack-us", env=env_US)
app.synth()
