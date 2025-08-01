import boto3
import botocore
from config import *

ec2 = boto3.client('ec2', region_name=AWS_REGION)

def create_key_pair():
    try:
        response = ec2.create_key_pair(KeyName=KEY_PAIR_NAME)
        with open(f"{KEY_PAIR_NAME}.pem", "w") as file:
            file.write(response['KeyMaterial'])
        print(f"✅ Key pair '{KEY_PAIR_NAME}' created and saved.")
    except botocore.exceptions.ClientError as e:
        print(f"⚠️ Key pair already exists or error: {e}")

def create_security_group():
    try:
        response = ec2.create_security_group(
            GroupName=SECURITY_GROUP_NAME,
            Description="Security group via Boto3"
        )
        sg_id = response['GroupId']
        ec2.authorize_security_group_ingress(
            GroupId=sg_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )
        print(f"✅ Security Group created with ID: {sg_id}")
        return sg_id
    except botocore.exceptions.ClientError as e:
        print(f"⚠️ Security Group creation error: {e}")

def launch_instance(sg_id):
    response = ec2.run_instances(
        ImageId=AMI_ID,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_PAIR_NAME,
        MinCount=1,
        MaxCount=1,
        SecurityGroupIds=[sg_id],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': TAG_NAME}]
            }
        ]
    )
    instance = response['Instances'][0]
    instance_id = instance['InstanceId']
    print(f"🚀 Instance launched with ID: {instance_id}")
    return instance_id

def main():
    create_key_pair()
    sg_id = create_security_group()
    if sg_id:
        launch_instance(sg_id)

if __name__ == "__main__":
    main()
