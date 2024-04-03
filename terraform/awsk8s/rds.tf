resource "aws_security_group" "rdssecurity" {
  name_prefix = "rdssecurity"
  ingress {
    from_port   = 0
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_instance" "default" {
  engine                 = "mysql"
  db_name                = "awslabproject"
  identifier             = "awslabproject"
  engine_version         = "5.7"
  instance_class         = "db.t3.micro"
  allocated_storage      = 20
  publicly_accessible    = true
  username               = var.db-username
  password               = var.db-password
  vpc_security_group_ids = [aws_security_group.rdssecurity.id]
  skip_final_snapshot    = true

  tags = {
    Name = "example-db"
  }
}