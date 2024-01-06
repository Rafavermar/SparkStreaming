# Real-Time Sentiment Analysis with TCP Socket, Apache Spark, OpenAI, Kafka and Elasticsearch | Data Enginering pipeline project


## Introduction
This project builds an end-to-end data engineering pipeline for real-time sentiment analysis using Yelp's Customer Reviews Dataset. It integrates TCP/IP Socket, Apache Spark, OpenAI LLM, Kafka, and Elasticsearch.


## System Architecture
This section describes any modifications to the original system architecture, focusing on the integration and flow of data across various components.
![Architecture.png](assets%2FArchitecture.png)

## Content
- Setting up data pipeline with TCP/IP
- Real-time data streaming with Apache Kafka
- Data processing techniques with Apache Spark
- Realtime sentiment analysis with OpenAI ChatGPT
- Synchronising data from kafka to elasticsearch
- Indexing and Querying data on elasticsearch

## Technologies
- Python
- TCP/IP
- Confluent Kafka
- Apache Spark
-  Docker
- Elasticsearch
-  OpenAI GPT-3.5 Turbo

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/Rafavermar/SparkStreaming.git
   ```

3. Navigate to the project directory:
    ```bash
   cd SparkStreaming
   ```

4. Run Docker Compose to set up the environment:
   ```bash
    docker-compose up
   ```
   
## CMD Commands needed ( Windows )
 [cmd_comands](assets/cmd_comands.txt)

 ## Resources
   - Customer Reviews Dataset: https://www.yelp.com/dataset/
   - Confluent Cloud Docs: https://docs.confluent.io/cloud
   - Elasticsearch Documentation: https://www.elastic.co/guide
   - Docker Compose Documentation: https://docs.docker.com/compose/
   - Apache Kafka Official Site: https://kafka.apache.org/
   - Apache Spark Official Site: https://spark.apache.org/

## Disclaimer
This project not only replicates but also builds upon Yusuf's foundational work, providing an up-to-date, real-world application of data engineering techniques.
Inspired by [airscholar's RealtimeStreamingEngineering](https://github.com/airscholar/RealtimeStreamingEngineering#)
