# Healthcare Management System

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [System Architecture](#system-architecture)
4. [Project Structure](#project-structure)
5. [Prerequisites](#prerequisites)
6. [Setup and Installation](#setup-and-installation)
7. [Running the Application](#running-the-application)
8. [API Documentation](#api-documentation)
9. [Testing](#testing)
10. [Contributing](#contributing)
11. [License](#license)
12. [Acknowledgments](#acknowledgments)

---

## Overview
The **Healthcare Management System** is a distributed, scalable, and microservices-based application developed in Python using FastAPI. The system facilitates the management of patients, doctors, appointments, and notifications in a modern healthcare setting. Each microservice operates independently and communicates asynchronously via RabbitMQ.

---

## Features
1. **Patient Service**:
   - Add, update, and manage patient data (e.g., name, contact, medical history).
2. **Doctor Service**:
   - Add, update, and manage doctor profiles, specialties, and availability.
3. **Appointment Service**:
   - Schedule, modify, and cancel appointments between patients and doctors.
4. **Notification Service**:
   - Send reminders and notifications to patients and doctors regarding appointments and updates.

---

## System Architecture
This project follows a **microservices architecture**, leveraging the following components:
- **FastAPI**: For building RESTful APIs.
- **RabbitMQ**: For asynchronous communication between microservices.
- **PostgreSQL**: Database for storing persistent data.
- **Docker & Docker Compose**: For containerizing and orchestrating microservices.
- **JSON Schema Validation**: For ensuring message integrity.

---

## Project Structure
healthcare-management-system/ │ ├── patient-service/ # Handles patient-related operations │ ├── app/ │ │ ├── routers/ # API endpoints │ │ │ └── patient.py # Patient service routes │ │ ├── models/ # Database models │ │ │ └── patient.py # Patient model │ │ ├── services/ # Business logic │ │ │ └── patient_service.py # Core patient logic │ │ ├── main.py # Entry point for the microservice │ └── requirements.txt # Python dependencies │ ├── doctor-service/ # Handles doctor-related operations │ ├── (similar structure as patient-service) │ ├── appointment-service/ # Manages appointments │ ├── (similar structure as patient-service) │ ├── notification-service/ # Sends notifications │ ├── (similar structure as patient-service) │ ├── docker-compose.yml # Orchestrates all microservices ├── README.md # Documentation ├── .gitignore # Files to ignore in Git ├── env.example # Example environment variable file └── tests/ # End-to-end and unit tests ├── test_end_to_end.py # Integration tests └── unit/ # Unit test files





---

## Prerequisites
1. **Python** (>= 3.9)
2. **Docker** and **Docker Compose**
3. **RabbitMQ** (installed via Docker in this setup)
4. **Git**

---

## Setup and Installation

### Clone the Repository
```bash
git clone https://github.com/your-username/healthcare-management-system.git
cd healthcare-management-system

---

Install Dependencies

Install Python dependencies for each microservice.
Example for Patient Service:

``` bash 
cd patient-service
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
