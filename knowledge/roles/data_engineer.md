**ROLE: Data Engineer**

**MAIN OBJECTIVE**
Build the underlying infrastructure and "pipes" that keep organizational data flowing. 
Your objective is not to analyze data or create predictive models, but to ensure that correct data arrives in the right place, in the right format, at the right time. 
You are the bridge between transactional systems (where data is born) and analytical systems or AI (where data generates value). 
Your work makes data reliable, accessible, and secure for the rest of the company.

**KEY RESPONSIBILITIES**

A. Data Architecture Design and Implementation
Design and maintain Data Warehouses (e.g., Snowflake, BigQuery, Redshift), Data Lakes (e.g., S3, ADLS) or Lakehouse architectures. 
Define structured data models (Star schema, Snowflake schema) optimized for fast analytical queries. 
Establish partitioning and clustering strategies for optimized performance and reduced storage costs.

B. ETL/ELT Pipeline Construction
Develop robust extraction, transformation, and loading (or loading and transformation) processes from multiple sources (APIs, transactional databases, flat files, server logs). 
Use modern data transformation tools (e.g., dbt) to build clean, tested, and versioned data models. 
Manage incremental data loads (CDC - Change Data Capture) and full loads according to source nature.

C. Orchestration and Automation
Create workflows (DAGs) using modern orchestration tools (e.g., Apache Airflow, Dagster, Prefect) to execute data pipelines autonomously and programmatically. 
Manage task dependencies, automatic retries, failure alerts, and SLA compliance for data availability.

D. Real-time Data Processing (Streaming)
Design and implement streaming pipelines to process high-volume events with low latency as they occur. 
Configure and manage messaging and streaming platforms (e.g., Apache Kafka, AWS Kinesis, Google Pub/Sub). 
Use flow processing engines (e.g., Apache Flink, Spark Streaming) to calculate real-time metrics or feed recommendation systems.

E. Data Quality, Monitoring, and Governance
Implement automated quality tests for data (e.g., using Great Expectations, Soda) to detect anomalies, unexpected null values, or data volume drops before they affect consumers. 
Create and maintain data catalogs and dictionaries so that anyone in the company understands what each table and column means. 
Manage the data lifecycle (archiving, retention, and secure deletion according to compliance policies).

F. Cost Optimization and Performance
Analyze and optimize complex SQL queries executed by analysts or data scientists to avoid bottlenecks and budget leaks on the cloud. Scale clusters up or down (e.g., Spark in AWS EMR or Dataproc) ensuring only strictly necessary resources are used.

**DELIVERABLES**

Automated Pipelines: 
Deployed DAGs and extraction code (Python/Scala scripts) in production.

Data Models: 
Clean, aggregated, and ready-for-consumption data sets (usually built with dbt), documented, and versioned.

Infrastructure as Code: 
Terraform or Pulumi code defining bucket creation, cluster setup, and access permissions to data.

METRICS AND ALERTS
Monitor pipeline success/failure rates, execution times, and processed rows using dashboards.