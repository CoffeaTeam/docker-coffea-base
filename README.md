# Base Docker image for Coffea Columnar Object Framework For Effective Analysis

![CI/CD status](https://github.com/CoffeaTeam/docker-coffea-base/workflows/PullRequest/badge.svg)
![GitHub issues](https://img.shields.io/github/issues/coffeateam/docker-coffea-base)
![GitHub pull requests](https://img.shields.io/github/issues-pr/coffeateam/docker-coffea-base)

Latest DockerHub Images: https://hub.docker.com/orgs/coffeateam/repositories

| Image           | Description                                   |  Size | Pulls | Version | Layers |
|-----------------|-----------------------------------------------|--------------|-------------|-------------|-------------|
| coffea-base     | Coffea image with latest XrootD and CA certicates            | ![](https://img.shields.io/docker/image-size/coffeateam/coffea-base?sort=date) | ![](https://img.shields.io/docker/pulls/coffeateam/coffea-base?sort=date) | ![](https://img.shields.io/docker/v/coffeateam/coffea-base?sort=date) | ![](https://img.shields.io/microbadger/layers/coffeateam/coffea-base)

## TL;DR

```console
$ docker run -it --name docker-coffea-base coffeateam/coffea-base
```

## Get this image

The recommended way to get the Coffea Base Docker image is to pull the prebuilt image from the [Docker Hub Registry](https://hub.docker.com/r/coffeateam/coffea-base).

```console
$ docker pull coffeateam/coffea-base:latest
```

To use a specific version, you can pull a versioned tag. You can view the [list of available versions](https://hub.docker.com/r/coffeateam/coffea-base/tags) in the Docker Hub Registry.

```console
$ docker pull coffeateam/coffea-base:[TAG]
```

If you wish, you can also build the image yourself.

```console
$ sudo docker build -t coffeateam/coffea-base base
```

## Releasing

Building and releasing new image versions is done automatically via Github CI. When new commits are
pushed to the master branch images are built with the recent coffea tag and and `latest` pushed to Docker Hub.

When a new version of Coffea is released a PR should be raised to bump the versions in
the `Dockerfile`s and then once that has been merged a new tag matching the Dask version
should be pushed. 
