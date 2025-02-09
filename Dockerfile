# Step 1: Use an official Python runtime as a parent image
FROM python:3.10-slim


# Step 3: Set the working directory in the container
WORKDIR /app

# Step 4: Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && pip install psycopg && pip install psycopg2-binary && pip install django \
    && apt-get clean 

# Step 5: Copy the requirements file into the container
COPY requirements.txt /app/

# Step 6: Install the Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Step 7: Copy the current directory contents into the container
COPY . /app


# Step 10: Expose port 8000 to the outside world
EXPOSE 8000


# Step 11: Copy the entrypoint script
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Step 12: Define the entrypoint script to run migrations and start the server
ENTRYPOINT ["/entrypoint.sh"]
