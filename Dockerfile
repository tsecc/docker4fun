# Pull the official ubuntu as the base image
FROM ubuntu

# Install Python3 with APT
RUN apt update
RUN apt -y install python3

# Set work directory
WORKDIR /docker4fun

# Copy the game file to the container work directory
COPY pysengame.py pysengame.py

CMD ["python3", "pysengame.py"]