locals {
  aws_region       = "us-east-1"
  environment_name = var.env
  tags = {
    iac_env              = local.environment_name,
    iac_managed_by       = "terraform",
    iac_source_repo_path = "iac",
    iac_owners           = "devops",
  }
}

terraform {
  required_version = "1.3.9"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.37.0"
    }
  }

  backend "remote" {}
}

provider "aws" {
  # Public ECRs are supported only in us-east-1
  region = "us-east-1"
  profile = var.profile
}

resource "aws_ecrpublic_repository_policy" "repo" {
  repository_name = aws_ecrpublic_repository.repo.repository_name

  policy = <<EOF
{
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "${var.imagename}",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "ecr:BatchCheckLayerAvailability",
                "ecr:PutImage",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload",
                "ecr:DescribeRepositories",
                "ecr:GetRepositoryPolicy",
                "ecr:ListImages",
                "ecr:DeleteRepository",
                "ecr:BatchDeleteImage",
                "ecr:SetRepositoryPolicy",
                "ecr:DeleteRepositoryPolicy"
            ]
        }
    ]
}
EOF
}

resource "aws_ecrpublic_repository" "repo" {
  repository_name = var.imagename

  force_destroy   = true

  catalog_data {
    about_text        = "${var.imagename} repository"
    architectures     = ["x86-64"]
    description       = "${var.imagename} repository"
    operating_systems = ["Linux"]
    usage_text        = "${var.imagename} repository"
  }

  tags = local.tags
}