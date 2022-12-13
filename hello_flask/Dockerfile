# Pulling base python image from dockerhub
FROM python:3.8-slim-buster

# MAINTAINER Leoncio Lopez "leobip27@gmail.com"

# Create the app Dir as working directory
WORKDIR /app

# Copy the requirements file to the app file
COPY ./requirements.txt /app/requirements.txt

# Execute the install of the requirements
RUN pip3 install -r requirements.txt

# Copy files from this dir to the WorkDir
COPY . .

EXPOSE 5000

# Define the Entrypoint
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
