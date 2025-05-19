import unittest
from aws_cdk import core
from my_react_cdk_python_app.stack import MyReactCdkStack

class TestMyReactCdkStack(unittest.TestCase):

    def setUp(self):
        self.app = core.App()
        self.stack = MyReactCdkStack(self.app, "TestStack")

    def test_s3_bucket_created(self):
        template = self.app.synth().get_stack("TestStack").template
        self.assertIn("AWS::S3::Bucket", template["Resources"])

    def test_route53_record_created(self):
        template = self.app.synth().get_stack("TestStack").template
        self.assertIn("AWS::Route53::RecordSet", template["Resources"])

if __name__ == "__main__":
    unittest.main()