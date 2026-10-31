
import boto3

ec2 = boto3.client("ec2", region_name="ap-south-2")

vpc_id = "vpc-057f06541a9c6d9bb"

# Create Security Group
response = ec2.create_security_group(
    GroupName="Todo-App-SG",
    Description="Security Group for Todo Application",
    VpcId=vpc_id
)

security_group_id = response["GroupId"]

# Add inbound rules
ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "IpRanges": [
                {"CidrIp": "0.0.0.0/0"}
            ]
        },
        {
            "IpProtocol": "tcp",
            "FromPort": 22,
            "ToPort": 22,
            "IpRanges": [
                {"CidrIp": "106.222.228.173/32"}
            ]
        }
    ]
)

print("Security Group created successfully!")
print("Security Group ID:", security_group_id)
