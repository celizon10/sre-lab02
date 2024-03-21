# Lab 02 SRE Academy on AWS

## Prerequisites

- Have installed [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- Have installed [GIT](https://git-scm.com/)
- Have an active AWS account
- Have installed [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

## Procedure

### Create AWS EKS (Kubernetes cluster on AWS)

1. Configure AWS CLI 
```Shell
aws configure
```
2. Clone the repo and access the directory
```Shell
git clone https://github.com/celizon10/sre-lab02.git && cd sre-lab02
```

3. Change directory to the terraform directory
```Shell
cd terraform
```

4. Initialize terraform
```Shell
terraform init
```

5. Validate terraform files
```Shell
terraform validate
```

6. Make sure the procedure is ok by doing a plan of the terrraform execution
```Shell
terraform plan
```

7. Create the kubernetes cluster
```Shell
terraform apply
```





Exercise
- Create your own GIT repository, within, Implement the necessary automation to deploy the container in the cloud provider of your choice (IBM Cloud, AWS, GCP, etc.).
- Use IaaC concepts
- Add a readme file that explains step by step how someone else could run the automation to do the deployment themselves without needing help.

Extra bonus:

Deploy the container to a Kubernetes cluster in the cloud.


aws ecr create-repository --repository-name lab02 --region us-east-2`


Store an IAM user access key in GitHub Actions secrets named `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.
#    See the documentation for each action used below for the recommended IAM policies for this IAM user,
#    and best practices on handling the access key credentials.

