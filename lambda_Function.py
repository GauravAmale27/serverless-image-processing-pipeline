import json
import boto3

s3 = boto3.client('s3')

DEST_BUCKET = "your-destination-bucket-name"

def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    copy_source = {
        'Bucket': source_bucket,
        'Key': object_key
    }
    
    new_key = f"thumbnail-{object_key}"
    
    s3.copy_object(
        Bucket=DEST_BUCKET,
        CopySource=copy_source,
        Key=new_key
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('File processed successfully!')
    }
