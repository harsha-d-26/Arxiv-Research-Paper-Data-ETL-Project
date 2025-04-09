# Arxiv Scientific Data ETL Project

## Overview
This project demonstrates an ETL pipeline using:
- Python
- Pandas
- PostgreSQL
- Docker & Docker Compose

## Architecture
- Extract: CSV File
- Transform: Data Cleaning & Preprocessing
- Load: Insert data into PostgreSQL tables

## Tech Stack
- Python 3.x
- Pandas
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose

## Project Structure
arxiv-etl-project/
│
├── app/                          # Application source code
│   ├── script.py                 # Main ETL script
│   ├── requirements.txt          # Python dependencies
│   └── Dockerfile                # For etl-runner container
│
├── postgres/                     # PostgreSQL related files
│   └── init.sql                  # DB schema and table creation
│
├── data/                         # Raw data
│   └── arXiv_scientific_dataset.csv
│
├── .env                          # Environment variables
│
├── docker-compose.yml            # Multi-container configuration
│
└── README.md                     # Project documentation

## Instructions to run this Project
- Clone the Repo:
```bash
git clone <repo-url>
cd arxiv-etl-project
```

- Create a .env file and set Environment variables:
```
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_db
POSTGRES_PORT=5432
POSTGRES_HOST=your_postgres_container_name
```

- Download the dataset arXiv_scientific_dataset.csv from https://www.kaggle.com/datasets/sumitm004/arxiv-scientific-research-papers-dataset

- Place the downloaded csv file in app/data/ folder

- Build and run:
```bash
docker-compose up --build
```

- To verify if the data is loaded successfully:
```bash
docker exec -it <your_postgres_container_name> psql -U your_username -d your_db
```
```
SELECT * FROM category LIMIT 5;
SELECT * FROM author LIMIT 5;
SELECT * FROM papers LIMIT 5;
```

## License
This project is open-source for learning purposes.

