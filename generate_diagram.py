from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2, EC2AutoScaling
from diagrams.aws.database import RDS
from diagrams.aws.network import VPC, PublicSubnet, PrivateSubnet, InternetGateway, NATGateway, ELB
from diagrams.aws.security import WAF
from diagrams.aws.general import Users

with Diagram("AWS Secure Three-Tier Web Application", show=False, filename="aws_three_tier_architecture", outformat="png"):
    users = Users("Internet Users")
    
    with Cluster("AWS Cloud"):
        with Cluster("VPC (10.0.0.0/16)"):
            igw = InternetGateway("Internet Gateway")
            
            with Cluster("Availability Zone A"):
                with Cluster("Public Subnet A"):
                    alb_a = ELB("Application Load Balancer")
                    nat_a = NATGateway("NAT Gateway A")
                    
                with Cluster("Private Subnet A (App)"):
                    app_a = EC2("Web Server A")
                    
                with Cluster("Private Subnet A (Data)"):
                    db_master = RDS("RDS Master (Multi-AZ)")
                    
            with Cluster("Availability Zone B"):
                with Cluster("Public Subnet B"):
                    alb_b = ELB("Application Load Balancer")
                    
                with Cluster("Private Subnet B (App)"):
                    app_b = EC2("Web Server B")
                    
                with Cluster("Private Subnet B (Data)"):
                    db_standby = RDS("RDS Standby")

            # Networking & Connections
            users >> igw
            igw >> alb_a
            igw >> alb_b
            
            # ALB to EC2 Auto Scaling
            alb_a >> app_a
            alb_b >> app_b
            
            # EC2 to RDS
            app_a >> db_master
            app_b >> db_master
            
            # RDS Replication
            db_master - db_standby
            
            # Outbound Internet
            app_a >> nat_a
            nat_a >> igw

