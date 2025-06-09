
# book-recommendation-system
A scalable book recommendation system built using Apache Spark, Hadoop, and Flask. Combines collaborative and content-based filtering with interactive Plotly dashboards for real-time, personalized suggestions. Features robust preprocessing, distributed processing, and an intuitive web interface.


# Overview
This project was developed as part of an academic initiative at San Jose State University. It focuses on applying big data technologies and machine learning to solve the challenge of book recommendation at scale.

# Features
This book recommendation system is designed to handle large-scale data efficiently through distributed data storage using HDFS and preprocessing workflows built with Python, Pandas, and MapReduce. It incorporates machine learning models developed using Apache Spark’s MLlib, enabling both collaborative filtering through the ALS algorithm and content-based filtering using MinHashLSH for accurate similarity detection.

To enhance the user experience, the system includes dynamic and interactive visualizations built with Plotly Dash, offering deep insights into user behavior, trends, and book popularity. The recommendations are deployed through a lightweight Flask web application, which serves real-time suggestions by loading pre-trained .pkl models—ensuring speed and scalability. With its modular architecture, the project integrates big data, machine learning, and visualization into a single, intuitive platform that provides personalized and engaging book recommendations.

# Technologies Used
  Apache Hadoop (HDFS, MapReduce)
  Apache Spark (PySpark, MLlib)
  Python (Pandas, NumPy, Scikit-learn)
  Plotly, Dash
  Flask
  HTML/CSS
  Jupyter Notebooks

# Dataset
Kaggle Dataset: https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews
