# Using alpine as our base since its light weight Linux, can use something heavier if needed down the road.
# FROM node:alpine
# COPY . /src
# WORKDIR /src

##########
# Google Bard
##########
# FROM python:3.11
# WORKDIR /app
# COPY requirements.txt ./
# RUN pip install -r requirements.txt
# COPY . .
# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


##########
# ChatGPT
##########
# # Use an official Python runtime as a parent image
# FROM python:3.9

# # Set environment variables for Django
# ENV PYTHONUNBUFFERED 1
# ENV DJANGO_SETTINGS_MODULE myproject.settings

# # Set the working directory to /app
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app/

# # Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

# # Expose port 8000 for the Django development server
# EXPOSE 8000

# # Run Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables for Django
# ENV PYTHONUNBUFFERED 1
# ENV DJANGO_SETTINGS_MODULE myproject.settings

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
