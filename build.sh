IMAGE_REPO=woofspot
IMAGE_TAG=dev

docker build . -t $IMAGE_REPO:$IMAGE_TAG
