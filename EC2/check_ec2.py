
import boto3

ec2 = boto3.client("ec2", region_name="ap-south-2")

response = ec2.describe_instances(
    InstanceIds=["i-0614ea69e3e169ff6"]
)

instance = response["Reservations"][0]["Instances"][0]

print("Instance ID:", instance["InstanceId"])
print("State:", instance["State"]["Name"])
print("Public IP:", instance.get("PublicIpAddress", "Not assigned yet"))
print("Private IP:", instance.get("PrivateIpAddress", "Not available yet"))
