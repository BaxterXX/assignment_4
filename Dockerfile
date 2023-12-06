# Dockerfile, Image, Container
FROM python:3.9
COPY . /main
WORKDIR /main
CMD ["python", "main.py"]


# Commands used for dockerfile image
# ADD main.py .
# RUN pip install requests
#docker build -t my-python-app
# docker login
# docker images
# docker push {username}/{repository}
# docker run -t -i