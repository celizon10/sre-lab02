# Lab 02 SRE Academy on AWS

## Prerequisites

- Have installed [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- Have installed [GIT](https://git-scm.com/)
- Have an active AWS account. Make sure to keep the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
- Have installed [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

## Procedure

### Create AWS EKS (Kubernetes cluster on AWS)

1. Fork this GIT Repo to be able to make changes in master

2. Configure AWS CLI 
```Shell
aws configure
```

3. Clone the repo and access the directory. Make sure to change <YOUR-REPO> for your git repo
```Shell
git clone https://github.com/<YOUR-REPO>/sre-lab02.git && cd sre-lab02
```

4. Change directory to the terraform directory
```Shell
cd terraform
```

5. Initialize terraform
```Shell
terraform init
```

6. Validate terraform files
```Shell
terraform validate
```

7. Make sure the procedure is ok by doing a plan of the terrraform execution
```Shell
terraform plan
```

8. Create the kubernetes cluster
```Shell
terraform apply
```

### Deploy to AWS EKS

1. Create a AWS Repository to upload the DockerImage
```Shell
aws ecr create-repository --repository-name lab02 --region us-east-2
```

2. Store the IAM user access key in GitHub Actions secrets named `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
```Git
Repo Settings > Secrets and variables > Actions > Repository secrets > New repository secret 

[!NOTE] Repeat for both `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
```

3. Make a minor change in any repo file, commit and push to the master. It will start the deployment in the AWS EKS

### Monitor Github Actions

You can monitor the deployment in the `Actions` Tab in your repository. 

### Accessing the application

1. After the github actions is succesfully deployed, you can go to the AWS Console


2. Search for the EC2 Load balancer that is associated with your recent uploaded application

    1. Go to `Elastic Kubernetes Service`

    2. Select the cluster that you previously created

    3. Select services and select the service created for the app


