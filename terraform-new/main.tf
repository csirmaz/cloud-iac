
// The provider block configures options that apply to all resources managed by your provider
provider "aws" {
  region = "us-west-2"
}

/*
// You can use data blocks to query your cloud provider for information
// Data source IDs are prefixed with data, followed by the block's type and name.
data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }

  owners = ["099720109477"] # Canonical
}
*/

// The first line of a resource block declares a resource type and resource name.
// The resource address for your EC2 instance is aws_instance.app_server.
resource "aws_instance" "app_server" {
  ami           = "ami-df5de72bdb3b" // data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  tags = {
    Name = var.instance_name
  }
}

resource "aws_s3_bucket" "test-bucket" {
  bucket = "my-bucket"
}

