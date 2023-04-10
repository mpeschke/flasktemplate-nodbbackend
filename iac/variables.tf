variable "env" {
  description = "dev | staging | prod = acronym of the environment to be created. This is required to uniquely identify global resources or configure TFC organizations and AWS accounts."
  type        = string
  default     = null
}

variable "aws_region" {
  description = "AWS Region to host cloud resources."
  type        = string
  default     = null
}

variable "profile" {
  description = "AWS CLI local profile"
  type        = string
  default     = null
}

variable "imagename" {
  description = "The name of the Docker image to be stored in this repo."
  type        = string
  default     = null
}