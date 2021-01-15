# Instructions

To create a docker image from the Dockerfile in the branch run:

```
$ docker build -t <image-name> .
```

To run a docker container from the created image:

```
$ docker run -p 8000:8000 -d -name=<container-name> <container-image>
```

To deploy the container from the image I have pushed to my dockerhub repository  run:

```
docker run -p 8000:8000 -d --name=<container-name> mulondu/sca-cloud-application:latest
```
Then visit browser to open the webapp. For example, for localhost visit: http://localhost:8000/

This is the link to my dockerhub repository: https://hub.docker.com/u/mulondu

I tested the django application with this command:

```
python manage.py check --deploy
```

It returned this output:

![test output](https://github.com/mulondumuema/SCA-Cloud-School-Application/blob/stable/docker/test.png)
