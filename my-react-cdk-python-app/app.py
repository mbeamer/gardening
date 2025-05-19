from aws_cdk import core
from my_react_cdk_python_app.stack import MyReactCdkStack

app = core.App()
MyReactCdkStack(app, "MyReactCdkStack")

app.synth()