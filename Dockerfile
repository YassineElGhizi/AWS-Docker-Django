FROM python:3.8.10
WORKDIR /usr/src/app
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1
# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
RUN python -m pip install --upgrade pip

# System deps
RUN apt update && apt install -y \
    libpq-dev \
    libjpeg-dev \
    curl

COPY requirement.txt ./
RUN pip install -r requirement.txt
