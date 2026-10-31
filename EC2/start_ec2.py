
import boto3

ec2 = boto3.client("ec2", region_name="ap-south-2")

instance_id = "i-0614ea69e3e169ff6"

response = ec2.start_instances(
    InstanceIds=[instance_id]
)

print("Starting EC2 instance...")

# Wait until the instance reaches running state
waiter = ec2.get_waiter("instance_running")
waiter.wait(InstanceIds=[instance_id])

print("EC2 instance is now running!")

# Retrieve the instance details
details = ec2.describe_instances(
    InstanceIds=[instance_id]
)

instance = details["Reservations"][0]["Instances"][0]

print("Instance ID:", instance["InstanceId"])
print("State:", instance["State"]["Name"])
print("Public IP:", instance.get("PublicIpAddress"))
print("Private IP:", instance.get("PrivateIpAddress"))
