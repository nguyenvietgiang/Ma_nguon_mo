# file chính
resource "aws_instance" "django_server" {
  ami           = "ami-0c02fb55956c7d316" # Amazon Linux 2 AMI, tùy theo region
  instance_type = var.instance_type
  key_name      = var.key_name

  # Mở cổng 22 và 80 trong Security Group
  vpc_security_group_ids = [aws_security_group.django_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo amazon-linux-extras enable python3.8
              sudo yum install python3.8 -y
              sudo yum install git -y
              pip3 install django
              cd /home/ec2-user
              git clone https://github.com/nguyenvietgiang/Ma_nguon_mo
              cd your-django-app
              python3 manage.py runserver 0.0.0.0:8000
              EOF

  tags = {
    Name = "DjangoApp"
  }
}

resource "aws_security_group" "django_sg" {
  name        = "django-sg"
  description = "Allow HTTP and SSH"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# sau khi đã code xong các file terraform, chúng ta sẽ thực thi lệnh terraform dưới đây hoặc tích hợp trong Jenkins pipeline để tự động
# terraform init - terraform plan - terraform apply