from flask import Flask, render_template
import os
import boto3

app = Flask(__name__)

group_name = os.environ.get('GROUP_NAME', 'Cool Group')
group_slogan = os.environ.get('GROUP_SLOGAN', 'Cloud Magic!')
bucket = os.environ.get('S3_BUCKET')
key = os.environ.get('S3_OBJECT')

aws_access = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret = os.environ.get('AWS_SECRET_ACCESS_KEY')
region = os.environ.get('AWS_REGION', 'us-east-1')

def download_image():
    try:
        session = boto3.session.Session(
            aws_access_key_id=aws_access,
            aws_secret_access_key=aws_secret,
            region_name=region
        )
        s3 = session.client('s3')
        s3.download_file(bucket, key, 'static/bg.jpg')
        print(f"Downloaded: s3://{bucket}/{key}")
    except Exception as e:
        print(f"Download failed: {e}")

@app.route('/')
def index():
    return render_template('index.html', group=group_name, slogan=group_slogan)

if __name__ == '__main__':
    download_image()
    app.run(host='0.0.0.0', port=81)
