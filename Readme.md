# Serverless Image Processing Pipeline (AWS)

## Overview

This project implements an event-driven, serverless architecture on AWS that automatically processes files upon upload.

When a user uploads an image to an Amazon S3 source bucket, an AWS Lambda function is triggered in real time. The function processes the file and stores the output in a separate S3 destination bucket. The system is fully serverless, scalable, and cost-efficient within AWS Free Tier limits.

---

## Architecture

### Services Used

- **Amazon S3 (Source Bucket)** – Stores incoming uploaded images  

- **AWS Lambda** – Triggered automatically on object creation events

- **Amazon S3 (Destination Bucket)** – Stores processed output files
  
- **AWS IAM Role** – Grants secure access between AWS services  

### Architecture Flow



This design follows a loosely coupled, event-driven cloud architecture pattern.

---

## How It Works

1. A user uploads an image to the source S3 bucket.
2. Amazon S3 generates an object creation event.
3. The event triggers the AWS Lambda function.
4. Lambda processes the file (copying/renaming).
5. The processed file is stored in the destination bucket automatically.

The system runs only when triggered, eliminating the need for dedicated servers.

---

## Key Features

- Fully serverless implementation (no EC2 instances)
- Automatic event-based execution
- Scales automatically with upload volume
- No infrastructure management required
- Cost-efficient under AWS Free Tier

---

## Technologies Used

- Amazon S3
- AWS Lambda
- AWS IAM
- Python 3.10
- S3 Event Notifications

---

## Cloud Concepts Demonstrated

- Event-driven architecture
- Serverless computing
- Cross-service AWS integration
- IAM role-based access control
- Stateless compute functions
- Automatic horizontal scalability

---

## Scalability & Design Considerations

The architecture is inherently scalable. AWS Lambda automatically scales based on incoming S3 events, allowing the system to handle one file or millions of uploads without infrastructure changes.

The loosely coupled design enables additional services (such as notifications, logging, or analytics) to be integrated without modifying the core workflow.

---

## Future Improvements

- Implement true image resizing using container-based Lambda deployment
- Add Amazon SNS for real-time notifications
- Store metadata in Amazon DynamoDB
- Integrate CloudFront for optimized content delivery
- Add file-type validation and structured error handling
- Implement monitoring and alerting with CloudWatch
