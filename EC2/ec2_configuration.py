
ami_id = "ami-0ed819c9d1237d1f2"
instance_type = "t3.micro"
key_name = "todo-app-key"
subnet_id = "subnet-061967c796b938910"
security_group_id = "sg-0b568537169376558"

launch_config = {
    "ImageId": ami_id,
    "InstanceType": instance_type,
    "KeyName": key_name,
    "MinCount": 1,
    "MaxCount": 1,
    "NetworkInterfaces": [
        {
            "DeviceIndex": 0,
            "SubnetId": subnet_id,
            "Groups": [security_group_id],
            "AssociatePublicIpAddress": True
        }
    ]
}

print("EC2 Launch Configuration:")
for key, value in launch_config.items():
    print(key, ":", value)
