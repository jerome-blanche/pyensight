#!/bin/sh
set -ex

# Image name
_IMAGE_NAME="ghcr.io/ansys/ensight_dev"

# Pull nexus image based on tag
docker pull $_IMAGE_NAME

# Remove all dangling images
docker image prune -f