import boto3
ec2 = boto3.client("ec2",region_name = "ap-south-2" )

ec2.create_subnet()