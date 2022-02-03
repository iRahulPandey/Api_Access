
# Specify your base image
FROM python:3.7.3-stretch
# create a work directory
RUN mkdir /app1
# navigate to this work directory
WORKDIR /app1
#Copy all files
COPY . .
# Install dependencies
RUN pip install Flask flask requests
# Run
CMD ["python","app.py"]

# run following commands
# docker build -f Dockerfile -t boston_model:api .
# docker run -p 5000:5000 -d boston_model:api