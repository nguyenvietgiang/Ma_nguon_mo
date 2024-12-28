# Định nghĩa provider (AWS) - tài khoản các tài nguyên sẽ được tạo ra trên AWS.
# Định nghĩa các tài nguyên chính - ít khi dùng vì lộ mã nguồn
provider "aws" {
  access_key = "your-access-key-id"
  secret_key = "your-secret-access-key"
  region     = "us-east-1"
}

