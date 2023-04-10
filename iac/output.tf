output "ecr_uri" {
  value = aws_ecrpublic_repository.repo.repository_uri
}

output "remote_ecr_image_tag" {
  value = "${aws_ecrpublic_repository.repo.repository_uri}:latest"
}

output "local_image_tag" {
  value = "${var.imagename}:latest"
}