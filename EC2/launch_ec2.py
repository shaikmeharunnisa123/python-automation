
import boto3

ec2 = boto3.client("ec2", region_name="ap-south-2")

# Check whether the instance already exists
existing = ec2.describe_instances(
    Filters=[
        {"Name": "tag:Name", "Values": ["Todo-App-EC2"]},
        {
            "Name": "instance-state-name",
            "Values": ["pending", "running", "stopping", "stopped"]
        }
    ]
)

if any(
    reservation["Instances"]
    for reservation in existing["Reservations"]
):
    print("Todo-App-EC2 already exists. No new instance created.")

else:
    response = ec2.run_instances(
        ImageId="ami-0ed819c9d1237d1f2",
        InstanceType="t3.micro",
        KeyName="todo-app-key",
        MinCount=1,
        MaxCount=1,

        NetworkInterfaces=[
            {
                "DeviceIndex": 0,
                "SubnetId": "subnet-061967c796b938910",
                "Groups": ["sg-0b568537169376558"],
                "AssociatePublicIpAddress": True
            }
        ],

        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [
                    {"Key": "Name", "Value": "Todo-App-EC2"},
                    {"Key": "Project", "Value": "Boto3-Networking"},
                    {"Key": "Application", "Value": "Todo-App"}
                ]
            }
        ],

        MetadataOptions={
            "HttpTokens": "required"
        }
    )

    instance_id = response["Instances"][0]["InstanceId"]

    print("EC2 instance creation request submitted!")
    print("Instance ID:", instance_id)
