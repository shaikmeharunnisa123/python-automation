# import boto3

# ec2 = boto3.client("ec2", region_name="ap-south-2")

# response = ec2.describe_images(
#     ImageIds=["ami-010ae2e0c8834a9ac"]
# )

# for image in response["Images"]:
#     print("AMI ID:", image["ImageId"])
#     print("State:", image["State"])
#     print("Architecture:", image["Architecture"])
#     print("Creation Date:", image["CreationDate"])
#     print("Owner ID:", image["OwnerId"])


import boto3

ssm = boto3.client("ssm", region_name="ap-south-2")

response = ssm.get_parameter(
    Name="/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
)

ami_id = response["Parameter"]["Value"]

print("Recommended Amazon Linux 2023 AMI:", ami_id)