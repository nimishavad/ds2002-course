#!/bin/bash

# arguments
FILE=$1
BUCKET=$2
EXPIRATION=$3

# upload file (private)
aws s3 cp $FILE s3://$BUCKET/

# generate presigned URL
aws s3 presign s3://$BUCKET/$FILE --expires-in $EXPIRATION