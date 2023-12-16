## Dockerfile to generate a Docker image from a GeoDjango project
##

# Start from an existing image with Miniconda installed
FROM continuumio/miniconda3

LABEL maintainer="Jude Abouhajar"

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=assignment2.settings

# Ensure that everything is up-to-date
RUN apt-get -y update && apt-get -y upgrade
RUN conda update -n base conda && conda update -n base --all

# Make a working directory in the image and set it as the working dir.
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy environment file and create Conda environment
COPY ENV.yml /usr/src/app
RUN conda env create -n DjangoEnv --file ENV.yml

# Activate Conda environment
RUN echo "source activate DjangoEnv" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# RUN conda init
# RUN conda activate DjangoEnv

RUN python -m pip install django-pwa==1.1.0

# Set up conda to match our test environment
RUN conda config --add channels conda-forge && conda config --set channel_priority strict
RUN cat ~/.condarc
RUN conda install uwsgi

# Copy everything in your Django project to the image.
COPY . /usr/src/app

# Make sure that static files are up to date and available
RUN pip install django-crispy-forms
RUN python manage.py collectstatic --no-input

# Expose port 8001 on the image. We'll map a localhost port to this later.
EXPOSE 8001

# Run "uwsgi". uWSGI is a Web Server Gateway Interface (WSGI) server implementation that is typically used to run Python
# web applications.
CMD uwsgi --ini uwsgi.ini





