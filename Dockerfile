FROM python:3


# Set application working directory
WORKDIR /usr/src/app

# Install requirements
RUN pip install --no-cache-dir flask

# Install application
COPY api.py ./

# Run application
CMD python api.py
