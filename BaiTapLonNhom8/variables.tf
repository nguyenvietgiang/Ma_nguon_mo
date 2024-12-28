# Định nghĩa các biến đầu vào (ví dụ: keypair, region, instance type).

variable "aws_region" {
  default = "us-east-1"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  description = "Tên key pair để kết nối SSH"
  default     = "my-key-pair"
}
