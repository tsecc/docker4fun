FROM py3buntu

RUN apt update
RUN apt install python3

# Set work directory
WORKDIR /docker4fun

# Copy the game file to the container work directory
COPY pysengame.py pysengame.py

CMD ["python3", "pysengame.py"]