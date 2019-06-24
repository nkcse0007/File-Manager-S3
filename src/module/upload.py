from flask import jsonify
import boto3
import os

S3_KEY = os.environ.get("S3_KEY")
S3_SECRET = os.environ.get("S3_SECRET")
S3_BUCKET = os.environ.get("S3_BUCKET")

s3 = boto3.client(
    "s3",
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET
)


def upload(file, path, acl="public-read"):
    try:
        print(path, S3_BUCKET)
        s3.upload_fileobj(
            file,
            S3_BUCKET,
            "upload/" + path,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
        # print("PATH: ",s3_path)

    except Exception as e:
        print("Something Happened: ", e)
        return jsonify(uploaded=False,
                       error="s3 error"
                       )
    return path
