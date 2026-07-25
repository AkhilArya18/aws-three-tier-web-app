# Auto Scaling Demo Instructions

Since we are providing infrastructure as code, you can easily test the Auto Scaling functionality yourself.

## Prerequisites
1. Deploy the infrastructure using `terraform apply`.
2. Connect to one of your Application Server instances. (You will need to temporarily use Session Manager or open SSH access from your IP if you didn't include it in the template).

## Triggering Auto Scaling

1. **Simulate High CPU Load:**
   Connect to an instance and run the `stress` tool, which we installed via the EC2 user data:
   ```bash
   stress --cpu 4 --timeout 300
   ```
   This will stress the CPU at 100% for 5 minutes.

2. **Monitor CloudWatch:**
   - Go to the **CloudWatch Console** in AWS.
   - Navigate to **Alarms**.
   - You will see the `high-cpu` alarm trigger (turn into `ALARM` state) after 2-4 minutes.

3. **Verify Scaling Event:**
   - Go to the **EC2 Console** -> **Auto Scaling Groups**.
   - Click on your Auto Scaling Group.
   - Go to the **Activity** tab.
   - You will see a new instance being launched to handle the increased load.

4. **Watch Scale Down:**
   - Once the `stress` command finishes (after 5 minutes), the CPU utilization will drop back to normal.
   - After a few minutes, the `low-cpu` alarm will trigger.
   - The Auto Scaling Group will terminate the extra instance.
