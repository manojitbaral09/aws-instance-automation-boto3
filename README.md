# AWS EC2 Automation with Python & Boto3

This project automates the process of launching an AWS EC2 instance using Python and the Boto3 SDK.

## 🔧 What It Does
- Creates a new **key pair**
- Creates a **security group** allowing SSH (port 22)
- Launches a **t2.micro EC2 instance** with the above settings
- Tags the instance for identification

## 📦 Requirements
- Python 3.x
- AWS credentials configured via `aws configure`
- `boto3` Python library

## 🧪 How to Run

```bash
git clone https://github.com/manojitbaral09/aws-instance-automation-boto3
cd aws-instance-automation-boto3
pip install -r requirements.txt
python main.py
# aws-instance-automation-boto3
