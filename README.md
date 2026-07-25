**AWS Secure Three-Tier Web Application Project Delivered**
I have successfully generated all the requested assets for your AWS Three-Tier Web Application architecture project.

**What was Accomplished**
Architecture Diagram:

I wrote a Python script using the diagrams package that programmatically generates a high-quality AWS architecture diagram using official AWS Architecture icons. It's stored as an image (aws_three_tier_architecture.png) in the project directory.
Terraform Infrastructure as Code (IaC):

Created a complete, production-ready Terraform codebase inside your project repository.
Designed a robust networking layer (VPC, Public/Private Subnets, IGW, NAT Gateways).
Configured secure compute and database layers (ALB, Auto Scaling Group, Multi-AZ RDS).
Applied principle of least privilege using targeted Security Groups and IAM Roles.
Documentation:

Created README.md with step-by-step deployment instructions for Terraform.
Wrote a detailed demo_instructions.md guide explaining exactly how to simulate high CPU load using stress to trigger Auto Scaling, and how to verify the scaling events in CloudWatch.
Well-Architected Mapping:

Created AWS_Well_Architected.md mapping your architecture directly against the six pillars of the AWS Well-Architected Framework (Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability).
Repository Location
All files have been placed in the following directory: 
aws-three-tier-web-app

text

aws-three-tier-web-app/
├── terraform/
│   ├── provider.tf
│   ├── variables.tf
│   ├── vpc.tf
│   ├── security.tf
│   ├── compute.tf
│   ├── database.tf
│   └── outputs.tf
├── generate_diagram.py
├── aws_three_tier_architecture.png
├── README.md
├── AWS_Well_Architected.md
└── demo_instructions.md

Next Steps for You

Open a terminal and navigate to the Terraform directory.
Ensure you have your AWS credentials configured (aws configure).
Run terraform init and terraform apply to deploy to your AWS account.
Follow the demo_instructions.md to run the CPU stress test and record your Demo Video/GIF!
TIP

Make sure to run terraform destroy when you are finished testing to avoid incurring unnecessary AWS costs.
