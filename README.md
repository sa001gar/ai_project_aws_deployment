# AI Paragraph Generator

**Project Name**: AI Paragraph Generator  
**Live Site**: [sagarkundu.live](https://sagarkundu.live)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Deployment Architecture](#deployment-architecture)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Contact](#contact)

## Overview

AI Paragraph Generator is an innovative web application designed to generate high-quality, unique paragraphs on demand. Built to be highly performant and accessible, this project is deployed on AWS EC2 with a robust setup that integrates AWS RDS for data management, S3 for efficient static and media file storage, and NGINX for enhanced server performance. Leveraging Cloudflare’s CDN, the application delivers fast response times worldwide, regardless of where users access it.

## Features

- **Instant Paragraph Generation**: Generate customized paragraphs with a single click.
- **User-Friendly Interface**: Sleek, mobile-optimized design with a clean, modern aesthetic.
- **Responsive Layout**: Designed for both mobile and desktop users.
- **Dynamic Content**: Real-time word count and paragraph length display.
- **Secure Deployment**: Securely hosted using NGINX with managed environment variables.

## Tech Stack

### Backend
- **Django**: Backend framework for building and managing views, models, and data.
- **Gunicorn**: WSGI HTTP Server for Python to serve the Django application.

### Frontend
- **HTML5, CSS3**: For a clean, responsive layout.
- **JavaScript**: For dynamic content rendering and interaction.

### Cloud and Deployment
- **AWS EC2**: Hosting and running the Django application.
- **AWS RDS**: Reliable database management.
- **AWS S3**: Storage of static and media files.
- **NGINX**: Reverse proxy server and load balancer.
- **Cloudflare CDN**: Improved content delivery and reduced latency.
  
### Environment Management
- **Python-dotenv**: For secure environment variable handling across local and production setups.

## Deployment Architecture

The deployment setup includes:

1. **AWS EC2 Instance**: Running the application server.
2. **NGINX**: Serves as a reverse proxy, redirecting traffic to the application via Gunicorn and enhancing load management.
3. **AWS RDS**: A managed database service to support scalable, reliable data handling.
4. **AWS S3**: Manages static assets and media files, reducing server load and ensuring faster loading times.
5. **Cloudflare CDN**: Provides global distribution of assets, optimizing content delivery.

## Diagram:
    User Request --> Cloudflare CDN --> NGINX (EC2 Instance) --> Gunicorn --> Django App (EC2)
                                            |
                                            --> AWS S3 (Static/Media Files)
                                            --> AWS RDS (Database)


## Getting Started

### Prerequisites

- **Python 3.9 or above**
- **Django**
- **AWS Account**

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sa001gar/ai-paragraph-generator.git
   cd ai-paragraph-generator
2. **Install dependencies:**
    ```python
    pip install -r requirements.txt
3. **Environment Setup:**

     Create a .env file based on .env.example with all necessary variables.
     Use AWS access keys, database credentials, and any specific environment configurations.
4. **Run Migrations:**
    ```python
    python manage.py migrate
5. **Start the Server:**
    ```python
    python manage.py runserver
## Project Structure
    
    ├── ai_paragraph_generator
    │   ├── settings.py         # Django settings (AWS, S3, Database configuration)
    │   ├── urls.py             # URL routing
    │   ├── wsgi.py             # WSGI config for Gunicorn
    ├── static                  # Static files served via S3
    ├── templates               # HTML templates
    ├── .env                    # Environment variables (not included in source control)
    └── README.md               # Project documentation
    

## Contact
**Creator:** Sagar Kundu

**GitHub:** [visit profile](github.com/sa001gar)  
**Website:** [sagarkundu.live](https://sagarkundu.live)
