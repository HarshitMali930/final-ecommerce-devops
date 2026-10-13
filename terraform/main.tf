terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "ecommerce" {
  name = "final-ecommerce:latest"

  build {
    context = ".."
  }
}

resource "docker_container" "ecommerce" {
  name  = "terraform-ecommerce"
  image = docker_image.ecommerce.image_id

  ports {
    internal = 5000
    external = 5003
  }
}
