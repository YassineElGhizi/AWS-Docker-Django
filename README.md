# AWS-Powered Web Architecture with Automated Backup System

## Overview

Welcome to the AWS-Powered Web Architecture with Automated Backup System project! 🚀

In this project, I embarked on a journey to deepen my expertise in Amazon Web Services (AWS) by designing and implementing a resilient and scalable web architecture. The focus was on leveraging AWS services such as Docker, EC2, RDS, S3, API Gateway, Lambda, SNS, Django, and Redis to create a robust and efficient system.

## Project Highlights

### 1. Web Architecture Design

The architecture is designed to handle web traffic efficiently and ensure high availability:

- **NGINX** serves as the web server, directing traffic to the core of the application.
- **Django** (running on **Gunicorn**) handles incoming requests, with the application running inside a Docker container for consistency across different environments.
- **Docker Compose** is used to manage the Docker containers, ensuring a seamless deployment process.

### 2. Asynchronous Task Processing

Asynchronous tasks are a critical part of the architecture, managed through:

- **Celery** for task processing, interfacing with **Redis** as the message broker. This setup allows for efficient queuing and processing of tasks, improving the responsiveness of the application.

### 3. Data Management and Storage

Data persistence and management are handled by:

- **PostgreSQL** hosted on **Amazon RDS**, providing a reliable and scalable database solution.
- **Amazon S3** is utilized for storing unstructured data, static files, and backup files, offering robust storage with virtually unlimited scalability.

### 4. API Management and Serverless Computing

For external APIs and serverless tasks:

- **Amazon API Gateway** is used to define, secure, and monitor APIs.
- **AWS Lambda** runs serverless compute tasks, triggered by the API Gateway, allowing for scalable, on-demand processing without the need for managing infrastructure.

### 5. Notification System

A robust notification system is implemented using:

- **Amazon SNS** for a pub/sub messaging system, enabling decoupled communication between services.
- An **email notification system** triggers based on specific application events, keeping users informed.

### 6. Automated Backup System

A key feature of this project is the automated backup system for the 'notes' table in PostgreSQL:

- **Celery Beat** schedules tasks that are dispatched to **Redis**.
- **Celery Workers** process tasks, invoking the **Amazon API Gateway**, which triggers an **AWS Lambda** function.
- The **Lambda function** connects to **Amazon RDS**, retrieves data, and stores it in **Amazon S3** as a JSON file.
- Upon successful completion, a message is published to an **Amazon SNS** topic, triggering an email notification to subscribed users.

## Workflow

The workflow of the backup process is illustrated as follows:

1. Celery Beat dispatches messages or tasks to Redis.
2. Celery Workers retrieve and process tasks from Redis.
3. Celery Workers execute tasks that invoke the Amazon API Gateway.
4. The Amazon API Gateway triggers a function deployed on AWS Lambda.
5. The Lambda function connects to Amazon RDS and retrieves data.
6. The Lambda function stores the retrieved data in Amazon S3 as a JSON file.
7. The Lambda function publishes a message to an Amazon SNS topic.
8. Subscribed users receive an email notification upon completion.

## Demonstration

Below are some images demonstrating the key components and workflow of the project:

![my_amzon_learning drawio](https://github.com/user-attachments/assets/06b90c27-2d5e-474c-984a-e7d75d3cb173)
*This diagram illustrates the overall architecture of the AWS-powered web application. It shows the interaction between different components such as NGINX, Docker, Django, Celery, Redis, Amazon RDS, Amazon S3, Amazon API Gateway, AWS Lambda, and Amazon SNS. The diagram visualizes how external users interact with the application through NGINX, which forwards requests to Django running on Gunicorn within a Docker container. Celery is used for asynchronous task processing, with Redis as the message broker. Data is managed using PostgreSQL on Amazon RDS and stored in Amazon S3. API requests are handled by Amazon API Gateway and processed by AWS Lambda. The architecture also includes an automated backup system, where the results of SQL queries are stored in Amazon S3, and notifications are sent via Amazon SNS.* 

![create_note](https://github.com/user-attachments/assets/02527298-7bc9-42a8-b8a9-70c5af8223bb)
*This screenshot shows the Django administration interface where a note is being added.*

![admin_periodics_tasks](https://github.com/user-attachments/assets/07160298-43f9-417c-b27c-34a9e0c281e8)
![celery_results](https://github.com/user-attachments/assets/d84ddf2e-c8b2-4442-8dc2-455dce614e55)
**This screenshot displays the Django administration interface for managing periodic tasks. The highlighted task, `dump_notes_table`, is responsible for periodically backing up data from the notes table in PostgreSQL to Amazon S3. Although this task typically runs on a scheduled basis , it is being executed manually for demonstration purposes.**

![s3](https://github.com/user-attachments/assets/3266ccdc-a637-4ee4-9b49-835a27ed5e78)
![results](https://github.com/user-attachments/assets/a8c01154-3d69-464f-be32-d5778caba4b2)
*Amazon S3 interface, displaying the backup files generated from the `notes` table. ; the content of one of the JSON backup files stored in Amazon S3.*


![mail](https://github.com/user-attachments/assets/ab7f8a5e-3c4b-499d-84d0-e8fb8970742f)
*This screenshot shows an email notification received from AWS SNS, confirming the successful completion of the backup operation. *

## Conclusion

This project was driven by my passion for leveraging AWS services to create scalable, efficient, and resilient web architectures. By implementing this solution, I've gained hands-on experience with various AWS components, enhancing my understanding of cloud infrastructure.

I invite you to explore the [project's code on GitHub](#) and welcome any constructive feedback to further refine and enhance my work.

## Contact

Feel free to reach out if you have any questions, suggestions, or potential collaborations in mind. Let's build something amazing together!

---

Thank you for visiting the repository! 😊
