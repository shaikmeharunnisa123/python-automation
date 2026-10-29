import boto3
ec2 = boto3.client("ec2",region_name = "ap-south-2")

vpc_id = 'vpc-057f06541a9c6d9bb'


ec2.create_tags(
    Resources = [vpc_id],
    Tags = [
        {"Key" : "Name", "Value" : "Python-Automation-VPC"},
        {"Key" : "Project", "Value" : "Boto3-Networking"},
    ],
)

print("Vpc named successfully")