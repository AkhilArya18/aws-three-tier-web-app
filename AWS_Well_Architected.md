# AWS Well-Architected Framework Mapping

Our Secure Three-Tier Web Application aligns closely with the six pillars of the AWS Well-Architected Framework.

## 1. Operational Excellence
> The ability to run and monitor systems to deliver business value and to continually improve supporting processes and procedures.

- **Infrastructure as Code (IaC):** The entire architecture is defined and deployed using Terraform, allowing for consistent, repeatable, and version-controlled environments.
- **Observability:** Amazon CloudWatch is configured to monitor CPU utilization, which triggers Auto Scaling events. Application logs and metrics can be centrally managed.
- **Automation:** Responses to traffic spikes are fully automated through Auto Scaling Groups, reducing the need for manual intervention.

## 2. Security
> The ability to protect information, systems, and assets while delivering business value through risk assessments and mitigation strategies.

- **Network Isolation:** Resources are strictly segregated across Public and Private subnets within a custom VPC.
- **Data Protection:** The database (RDS) is located in a private subnet, completely isolated from direct internet access.
- **Least Privilege:** Security Groups act as stateful firewalls, only permitting necessary traffic (e.g., HTTP/HTTPS to ALB, ALB to EC2 on port 80, EC2 to RDS on port 3306). IAM Roles are used for EC2 instance profiles instead of hardcoded credentials.

## 3. Reliability
> The ability of a system to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions such as misconfigurations or transient network issues.

- **High Availability:** Resources (ALB, EC2, RDS, NAT Gateways) are distributed across multiple Availability Zones (Multi-AZ).
- **Fault Tolerance:** If an EC2 instance fails health checks, the Auto Scaling Group automatically terminates it and launches a healthy replacement. RDS Multi-AZ ensures automatic database failover if the primary node goes down.
- **Load Balancing:** The Application Load Balancer distributes incoming traffic to prevent any single instance from becoming a bottleneck.

## 4. Performance Efficiency
> The ability to use computing resources efficiently to meet system requirements and to maintain that efficiency as demand changes and technologies evolve.

- **Elasticity:** The Auto Scaling Group dynamically adds compute capacity during high-demand periods to maintain performance, and removes it when load decreases.
- **Right-Sizing:** Using Amazon EC2 and RDS instance families suited for the workload (e.g., burstable `t2/t3` families for variable web traffic).
- **Network Optimization:** Traffic is routed efficiently through the AWS backbone.

## 5. Cost Optimization
> The ability to run systems to deliver business value at the lowest price point.

- **Pay-as-you-go:** Auto Scaling ensures you only pay for the EC2 compute resources you actually need.
- **Managed Services:** Utilizing managed services like Amazon RDS and NAT Gateway reduces the operational overhead and cost of managing those systems manually.
- **Resource Cleanup:** Defining the infrastructure as code (Terraform) makes it trivial to spin up and tear down environments to avoid idle resource costs.

## 6. Sustainability
> The ability to continually improve sustainability impacts by maximizing utilization and minimizing the environmental footprint of cloud workloads.

- **Maximized Utilization:** By using Auto Scaling, we minimize idle compute resources, directly reducing the energy consumption footprint.
- **Managed Services:** AWS optimizes the infrastructure for managed services (RDS, ALB) to run more efficiently than self-managed equivalents.
