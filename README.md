#  Public Transport Ticketing Data Pipeline

##  Overview

This project implements a **scalable end-to-end data engineering pipeline** for public transport ticketing data. It covers the complete lifecycle from data ingestion to visualization using modern tools.

The system is designed to handle **large-scale datasets (1M+ rows)** and integrates **batch processing, streaming simulation, cloud deployment, and analytics**.

---

##  Problem Statement

Public transport systems generate massive volumes of ticket data across routes, cities, and vehicle types. However:

- Data exists in **raw CSV format**
- No centralized processing system
- Data quality issues (nulls, duplicates, anomalies)
- Difficult to analyze large datasets
- No visualization layer for insights

---

##  Solution

An **end-to-end data pipeline** was built to:

- Ingest raw data
- Perform cleaning and validation
- Apply transformations and feature engineering
- Store processed data in databases
- Perform large-scale processing using Spark
- Simulate streaming using Kafka
- Deploy pipeline on cloud (AWS EC2 + S3)
- Visualize insights via dashboard

---

## Project Structure
```bash
PTTS/  # Public Transport Ticketing System (Data Engineering Pipeline)
│
├── airflow/  
│   ├── dags/
│   │   └── ticketing_pipeline_dag.py     # Defines ETL workflow (generate → merge → process → load → analysis)
│   │
│   ├── data/
│   │   ├── raw/
│   │   │   ├── data1.csv                # Synthetic dataset part 1
│   │   │   └── data2.csv                # Synthetic dataset part 2
│   │   │
│   │   └── processed/
│   │       ├── merged_data.csv          # Combined dataset (1M rows)
│   │       └── final_data.csv           # Cleaned + transformed dataset
│   │
│   ├── logs/                           # Airflow execution logs (task monitoring)
│   │
│   ├── modules/
│   │   ├── transform.py                # Data transformation (normalization, feature engineering)
│   │   └── validator.py                # Data validation (nulls, duplicates, anomalies)
│   │
│   └── scripts/
│       ├── generate_data.py            # Generates synthetic ticket data
│       ├── merge_data.py               # Merges raw datasets
│       ├── process.py                  # Cleans + validates + transforms data
│       ├── load_to_db.py               # Loads processed data into DB (PostgreSQL)
│       └── performance_analysis.py     # Memory + performance benchmarking
│
├── api/
│   └── app.py                          # API layer 
│
├── data/
│   ├── raw/                            # Local raw dataset storage
│   ├── processed/                      # Local processed dataset
│   └── star/                           # Star schema data (warehouse-ready)
│
├── kafka/
│   ├── producer.py                     # Simulates real-time ticket data streaming
│   └── consumer.py                     # Consumes and processes streaming data
│
├── modules/
│   ├── transform.py                    # Reusable transformation functions
│   └── validator.py                    # Reusable validation logic
│
├── pipeline_deploy/                    # Cloud deployment (EC2 version of pipeline)
│   ├── data/
│   │   ├── raw/                        # Data used on EC2 instance
│   │   └── processed/
│   │
│   ├── modules/
│   │   ├── transform.py                # Same transformations for cloud execution
│   │   └── validator.py
│   │
│   └── scripts/
│       ├── generate_data.py            # Pipeline execution on EC2
│       ├── merge_data.py
│       ├── process.py
│       ├── load_to_db.py               # Loads into PostgreSQL (cloud DB)
│       └── performance_analysis.py
│
├── scripts/
│   ├── dashboard.py                    # Dashboard (Streamlit/visualization)
│   ├── star_schema.py                  # Creates star schema (data warehouse design)
│   ├── generate_data.py                # Standalone data generation
│   ├── merge_data.py                   # Standalone merging
│   ├── process.py                      # Standalone processing
│   ├── load_to_db.py                   # Standalone DB load
│   └── performance_analysis.py         # Performance metrics
│
├── spark/
│   ├── spark_job.ipynb                 # Spark batch + SQL + streaming analysis
│  
│
├── sql/
│   └── queries.sql                     # SQL queries (aggregation, ranking, analytics)
│
├── requirements.txt                   # Python dependencies
├── README.md                          # Project documentation
├── report.pdf                         # Final submission report
└── test.csv                           # S3 upload/download test file
```

##  Features

### 🔹 1. Data Ingestion

- Reads multiple CSV files (`data1.csv`, `data2.csv`)
- Merges datasets using `merge_data.py`


---

### 🔹 2. Data Validation & Cleaning

Implemented in `validator.py`:

- Null value detection  
- Duplicate detection  
- Anomaly detection  


---

### 🔹 3. Data Transformation

Implemented in `transform.py`:

- Price normalization  
- Feature engineering  
- Aggregation  

---

### 🔹 4. Workflow Orchestration (Airflow)

Automated DAG (`ticketing_pipeline_dag.py`) handles:

- Data generation  
- Data merging  
- Data processing  
- Database loading  
- Performance analysis  

---

### 🔹 5. Database Integration

- **MySQL** → Used for writing and testing SQL queries  
- **PostgreSQL** → Used for Airflow execution and EC2 deployment  

**Reason:**  
MySQL was suitable for local queries, but PostgreSQL was used for better compatibility with **Airflow and cloud deployment**.


---

### 🔹 6. Performance Optimization

- Dataset size: **1 Million Rows**
- Memory optimization applied
- Metrics tracked:
  - Load time  
  - Processing time  
  - Memory usage  

---

### 🔹 7. Big Data Processing (PySpark)

Implemented in `spark_job.ipynb`:

- Filtering  
- Aggregation  
- Spark SQL  
- Partitioning  
- Caching  

Also includes structured streaming simulation.


---

### 🔹 8. Streaming (Kafka Simulation)

- Producer-consumer architecture implemented  
- Simulates real-time data pipeline  

Files:
- `producer.py`
- `consumer.py`

---

### 🔹 9. Cloud Integration

####  AWS S3
- Upload & download dataset (`final_data.csv`)

####  AWS EC2
- Pipeline deployed and executed
- Virtual environment configured

---

##  Dashboard (Streamlit)

Interactive dashboard provides:

- Revenue by route  
- Revenue by city  
- Vehicle-wise revenue  
- Price category distribution  

Features:
- Filters  
- Interactive charts  
- Clean UI  

---

##  Tech Stack

| Category | Tools |
|--------|------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Orchestration | Apache Airflow |
| Big Data | Apache Spark |
| Streaming | Kafka (Simulation) |
| Database | MySQL (for SQL queries), PostgreSQL (for cloud deployment) |
| Cloud | AWS S3, EC2 |
| Visualization | Streamlit |

---

##  Unique Points

-  End-to-end pipeline (Ingestion → Processing → Storage → Visualization)  
-  Handles **1M+ rows efficiently**  
-  Combines **Batch + Streaming + Cloud + Big Data**  
-  Modular and reusable architecture  
-  Real-world deployment on EC2  
-  Data validation system implemented  

---

##  Future Improvements

- Real-time Spark Streaming with Kafka  
- Integration with AWS Redshift / BigQuery  
- Public dashboard deployment  
- ML-based demand prediction  
- Alert system for anomalies  

---

##  Conclusion

This project demonstrates a **complete data engineering pipeline** capable of handling large-scale data, ensuring data quality, and generating actionable insights.

It integrates modern tools and reflects real-world industry practices.

---

## Note
The necessary screenshots of the project are pasted in the project report document(report.pdf)

---

##  How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run pipeline
python scripts/generate_data.py
python scripts/merge_data.py
python scripts/process.py
python scripts/load_to_db.py
python scripts/properformance_analysis.py

# Run dashboard
streamlit run scripts/dashboard.py
