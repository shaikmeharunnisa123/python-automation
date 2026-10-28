import boto3

ec2 = boto3.client("ec2",region_name = "ap-south-2")

vpc_id = 'vpc-057f06541a9c6d9bb'

route_table = ec2.create_route_table(
   
    VpcId = vpc_id,
)