# Dockerfile
FROM python:3.8

# Install required packages
RUN pip install pyodbc

# Copy the simulator script
COPY iot_simulator.py /iot_simulator.py

# Run the script every 5 minutes
CMD while true; do python /iot_simulator.py; sleep 300; done
