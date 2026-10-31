
import boto3

ec2 = boto3.client("ec2", region_name="ap-south-2")

response = ec2.describe_images(
    Owners=["amazon"],
    Filters=[
        {
            "Name": "name",
            "Values": ["al2023-ami-2023.*-x86_64"]
        },
        {
            "Name": "state",
            "Values": ["available"]
        }
    ]
)

# Sort images by creation date
images = sorted(
    response["Images"],
    key=lambda image: image["CreationDate"],
    reverse=True
)

# Get the latest image
latest_image = images[0]

print("Latest Amazon Linux 2023 AMI")
print("AMI ID:", latest_image["ImageId"])
print("AMI Name:", latest_image["Name"])
print("Creation Date:", latest_image["CreationDate"])
