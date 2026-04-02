#!/bin/bash

AMI=ami-0ec10929233384c7f
INSTANCE_TYPE=t2.nano
INSTANCE_NAME=ds2002-ced5jz
KEY_NAME=key-ec2
SECURITY_GROUP_ID=PUT_YOURS_HERE
SUBNET_ID=PUT_YOURS_HERE

aws ec2 run-instances \
  --image-id $AMI \
  --instance-type $INSTANCE_TYPE \
  --key-name $KEY_NAME \
  --security-group-ids $SECURITY_GROUP_ID \
  --subnet-id $SUBNET_ID \
  --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$INSTANCE_NAME}]"
