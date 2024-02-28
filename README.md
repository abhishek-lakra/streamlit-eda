# Streamlit EDA

## Overview

This project utilizes Python along with specific libraries and frameworks for exploratory data analysis (EDA) in a streamlined manner. Below are the key technologies employed:

### Technology
- **Programming Language**: Python
- **Libraries**: Pandas, Plotly
- **Framework**: Streamlit
- **Software**: Docker

## Getting Started

To set up and run the application, follow the steps below:

### How to start application
1. **Create Docker Network**: Execute the following command to create a Docker network with specified settings:
    ```bash
    docker network create --gateway 172.25.0.1 --subnet 172.25.0.0/24 --attachable streamlit-network
    ```

2. **Start Container**: Start the Docker container using the following command:
    ```bash
    docker-compose up -d
    ```

### Usage of application
1. **Access the Application**: Open any web browser and navigate to `http://localhost:8020/` to access the application.

2. **Upload Data for EDA**: Once in the application, upload either a `csv` or `xlsx` file to perform exploratory data analysis.

3. **Select Variables for Graphs**: Choose the variables you want to explore in the graph for detailed EDA insights.
