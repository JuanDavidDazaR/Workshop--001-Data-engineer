# Workshop-001: Data Engineer

**By Juan David Daza**

This project is part of a Data Engineering exercise. Its objective is to demonstrate skills in data management, transformation, and visualization using Python, PostgreSQL, and Jupyter Notebook. The dataset consists of a CSV file with 50,000 records of candidates who participated in selection processes.

## Overview

This project explores a dataset using Data Engineering and Exploratory Data Analysis (EDA) techniques. The tools employed include Python, PostgreSQL, and Power BI to efficiently transform and visualize information.

The primary goal is to analyze the dataset structure, identify relevant patterns, and assess data quality for decision-making purposes.

## Key Objectives

-   Implement an efficient ETL process for data handling.
-   Perform data cleaning and transformation.
-   Explore patterns and relationships in the data, including:
    -   Descriptive analysis.
    -   Anomaly detection.
    -   Data visualization.
-   Create clear and effective visualizations in Power BI.

## Technologies Used

-   **Python**: Data processing and analysis.
-   **Jupyter Notebook**: Interactive analysis.
-   **PostgreSQL**: Database management and storage.
-   **Power BI**: Dashboard creation.

## Prerequisites

Before starting, make sure you have the following requirements:

-   **Python**: 3.12.9
-   **PostgreSQL**: 14+
-   **Power BI Desktop** for visualization
-   **Visual Studio Code** or your preferred Python IDE

## Project Setup

### Clone the Repository

```sh
git clone https://github.com/JuanDavidDazaR/Workshop--001-Data-engineer.git

```
go to the project folder

```
cd Workshop--001-Data-engineer
```


### Virtual Environment Setup

#### Create and Activate a Virtual Environment

```sh
python -m venv venv

```

**Windows (CMD):**

```sh
venv\Scripts\activate.bat

```

**Windows (PowerShell):**

```sh
venv\Scripts\Activate.ps1

```

**Mac/Linux:**

```sh
source venv/bin/activate

```

#### Install Dependencies in the Virtual Environment

```sh
pip install -r requirements.txt

```

## PostgreSQL Configuration

1.  Ensure PostgreSQL is installed.
2.  Take note of the PostgreSQL username and password for authentication.

## Before Running the Project

Before starting the project, it is essential to create a **credentials.json** file. This file should be located inside the `src/database` directory. You can create it using the following commands:

#### Windows (PowerShell or CMD):

```sh
echo {} > src/database/credentials.json

```

#### macOS or Linux (Terminal):

```sh
touch src/database/credentials.json

```

This command will create an empty `credentials.json` file in the `src/database/` directory.

### Setting Up Database Credentials

#### **Windows (PowerShell or CMD):**

```sh
notepad src/database/credentials.json

```

#### **macOS or Linux:**

```sh
nano src/database/credentials.json

```

You can use **nano** or **vim** to edit the file.

#### Database Credentials Format

To connect to the database, the `credentials.json` file must have the following structure:

```json
{
    "host": "your_host",
    "user": "your_user",  
    "password": "your_password",
    "port": your_port,
    "db_name": "your_database"
}

```

The **user** and **password** should match your PostgreSQL credentials. Additionally, ensure that **host** and **db_name** are enclosed in double quotes `""`.

## Running the Project

### Execute the ETL Script to Load Data into PostgreSQL

Start browsing the notebooks:
    

-   001_LoadRawData
-   002_EDA
-   003_LoadCleanData.

## Power BI Integration

### Connect to PostgreSQL

To load the database into Power BI and generate visualizations, follow these steps:

1.  Open Power BI and select Get Data.
2.  Search for and select PostgreSQL as the data source.
3.  In the Server field.
4.  In the Database field, enter the name of the database used in this project.
5.  Click Connectand, if required, enter your PostgreSQL username and password.
6.  Select the desired table within the database and click Load.
7.  Once the table is loaded, the data will be available for visualization and report generation in Power BI.

## Example Visualizations in Power BI

-   **Hires by Technology** (Pie Chart)
-   **Hires by Year** (Horizontal Bar Chart)
-   **Hires by Seniority** (Bar Chart)
-   **Hires by Country Over the Years** (Multi-line Chart: USA, Brazil, Colombia, and Ecuador only)

----------

