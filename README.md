# Base Docker image for Coffea Columnar Object Framework For Effective Analysis

## TL;DR

```console
$ docker run -it --name docker-coffea-base coffeateam/docker-coffea-base
```

## Get this image

The recommended way to get the Coffea Base Docker image is to pull the prebuilt image from the [Docker Hub Registry](https://hub.docker.com/r/coffeateam/docker-coffea-base).

```console
$ docker pull coffeateam/docker-coffea-base:latest
```

To use a specific version, you can pull a versioned tag. You can view the [list of available versions](https://hub.docker.com/r/coffeateam/docker-coffea-base/tags) in the Docker Hub Registry.

```console
$ docker pull coffeateam/docker-coffea-base:[TAG]
```

If you wish, you can also build the image yourself.

```console
$ sudo docker build -t coffeateam/docker-coffea-base base
```

## Releasing

Building and releasing new image versions is done automatically via Github CI. When new commits are
pushed to the master branch images are built with the `dev` tag and pushed to Docker Hub.

When a new version of Coffea is released a PR should be raised to bump the versions in
the `Dockerfile`s and then once that has been merged a new tag matching the Dask version
should be pushed. Travis will then build the images and push them with version tags and update
`latest` too.

```console
$ git commit --allow-empty -a -m "bump version to x.x.x"
$ git tag -a x.x.x -m 'Version x.x.x'
$ git push upstream master --tags
```
