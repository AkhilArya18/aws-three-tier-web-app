# AWS Secure Three-Tier Web Application

This repository contains the Terraform infrastructure as code (IaC) to deploy a highly available, secure, and scalable Three-Tier Web Application on AWS.

## Architecture Highlights
- **Presentation Layer**: Application Load Balancer in Public Subnets
- **Application Layer**: Auto Scaling Group of EC2 instances in Private Subnets
- **Database Layer**: Multi-AZ RDS MySQL database in Private Subnets

## Prerequisites
- AWS Account
- [Terraform](https://developer.hashicorp.com/terraform/downloads) installed
- AWS CLI configured with administrator credentials

## Deployment Steps
1. **Initialize Terraform**
   ```bash
   cd terraform
   terraform init
   ```
2. **Review the Plan**
   ```bash
   terraform plan
   ```
3. **Apply the Configuration**
   ```bash
   terraform apply -auto-approve
   ```
4. **Access the Application**
   Once deployment is complete, Terraform will output the `alb_dns_name`. Open this URL in your browser to view the application.

## Cleanup
To avoid incurring future charges, destroy the infrastructure when you're done:
```bash
terraform destroy -auto-approve
```
