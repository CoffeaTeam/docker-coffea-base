# Base Docker image for Coffea Columnar Object Framework For Effective Analysis

![CI/CD status](https://github.com/CoffeaTeam/docker-coffea-base/workflows/PullRequest/badge.svg)
![GitHub issues](https://img.shields.io/github/issues/coffeateam/docker-coffea-base)
![GitHub pull requests](https://img.shields.io/github/issues-pr/coffeateam/docker-coffea-base)

Latest DockerHub Images: https://hub.docker.com/orgs/coffeateam/repositories

| Image           | Description                                   |  Size | Pulls | Version | 
|-----------------|-----------------------------------------------|--------------|-------------|-------------|
| coffea-base     | Debian Coffea image with latest XrootD and CA certicates            | ![](https://img.shields.io/docker/image-size/coffeateam/coffea-base?sort=date) | ![](https://img.shields.io/docker/pulls/coffeateam/coffea-base?sort=date) | ![](https://img.shields.io/docker/v/coffeateam/coffea-base?sort=date) 
| coffea-base-cc7     | Centos7 Coffea image with latest XrootD and CA certicates            | ![](https://img.shields.io/docker/image-size/coffeateam/coffea-base-cc7?sort=date) | ![](https://img.shields.io/docker/pulls/coffeateam/coffea-base-cc7?sort=date) | ![](https://img.shields.io/docker/v/coffeateam/coffea-base-cc7?sort=date)

## TL;DR

```console
$ docker run -it --name docker-coffea-base coffeateam/coffea-base
```

```console
$ docker run -it --name docker-coffea-base-cc7 coffeateam/coffea-base-cc7
```
## Get this image

The recommended way to get the Coffea Base Docker image(s) is to pull the prebuilt image from the [Docker Hub Registry](https://hub.docker.com/r/coffeateam/coffea-base).

```console
$ docker pull coffeateam/coffea-base:latest
```

```console
$ docker pull coffeateam/coffea-base-cc7:latest
```

To use a specific version, you can pull a versioned tag. You can view the [list of available versions](https://hub.docker.com/r/coffeateam/coffea-base/tags) in the Docker Hub Registry.

```console
$ docker pull coffeateam/coffea-base:[TAG]
```

```console
$ docker pull coffeateam/coffea-base-cc7:[TAG]
```

If you wish, you can also build the image yourself.

```console
$ sudo docker build -t coffeateam/coffea-base base
```

```console
$ sudo docker build -t coffeateam/coffea-base-cc7 base-cc7
```

## Releasing

Building and releasing new image versions is done automatically via Github CI. 

When new commits are pushed to the master branch, images with the recent Coffea `tag` and as well with `latest` tag are built and pushed to Docker Hub.

How it work: when a new version of Coffea is released a PR should be raised to bump the versions in the `Dockerfile`s and then once that has been merged a new tag matching the Coffea version should be pushed. 
