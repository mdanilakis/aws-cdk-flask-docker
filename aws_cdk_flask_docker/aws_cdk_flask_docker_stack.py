from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_elasticloadbalancingv2 as elb_v2,
    aws_certificatemanager as cert_manager,
    aws_route53 as r53,
)
from constructs import Construct


class AwsCdkFlaskDockerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # Retrieve VPC information
        vpc = ec2.Vpc.from_lookup(
            self, 'VPC',
            # This imports the default VPC but you can also
            # specify a 'vpcName' or 'tags'.
            is_default=True)

        # ECS cluster
        cluster = ecs.Cluster(self, 'MyCluster', vpc=vpc)

        # SSL Certificate
        # Replace REGION, ACCOUNT and CERTIFICATE with your certificate attributes
        certificate_arn = 'arn:aws:acm:REGION:ACCOUNT:certificate/CERTIFICATE'

        # Use ALB + Fargate from ECS patterns
        service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, 'MyFlaskApiWithFargate',
            cluster=cluster,
            cpu=256,
            desired_count=1,
            assign_public_ip=True,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_asset('./server'),
                container_port=5000),
            memory_limit_mib=512,
            public_load_balancer=True,
            protocol=elb_v2.ApplicationProtocol.HTTPS,
            redirect_http=True,
            certificate=cert_manager.Certificate.from_certificate_arn(self, 'cert', certificate_arn),
            # R53 configuration
            # Replace with your domain and subdomain
            domain_name='cdk-flask-api.domain.com.',
            domain_zone=r53.HostedZone.from_lookup(self, "MyHostedZone", domain_name="domain.com."))

        # Default target group healthcheck path is /
        # This can be customized
        service.target_group.configure_health_check(path='/health')
