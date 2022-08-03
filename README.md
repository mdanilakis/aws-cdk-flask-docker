
# aws-cdk-flask-docker

A simple Flask web application that can be deployed to ECS Fargate using the AWS CDK.

## Install and bootstrap the AWS CDK

```
npm install -g aws-cdk
cdk bootstrap aws://ACCOUNT-NUMBER/REGION
```

After the bootstrapping process completes, run the following commands to activate the virtualenv and install the AWS CDK core dependencies.

```
source .venv/bin/activate
python -m pip install -r requirements.txt
```

The initialization process also creates a virtualenv within this project, stored under the `.venv` directory. To manually create a virtualenv:

```
python -m venv .venv
```

## Deploy the stack

To deploy the stack, run the following command(s):

```
cdk synth  # synthesizes and outputs the AWS CloudFormation template (optional)
cdk deploy # synthesizes and deploys the stack
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
 
See: [Deploying to ECS Fargate using the AWS CDK](https://michalisdaniilakis.com/posts/deploying-to-ecs-fargate-using-the-aws-cdk)
