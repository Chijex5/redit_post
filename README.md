# Reddit Data Scrapper

## Overview
The Reddit Data Fetching and Storage System is designed to retrieve top posts from specified subreddits using the PRAW library. This system efficiently organizes the data into a Pandas DataFrame and facilitates the export of top-rated posts to a CSV file. Furthermore, it establishes a secure connection to a Snowflake database to store the top-rated posts, utilizing environment variables for sensitive information, such as API keys and database credentials. This approach ensures secure and efficient handling of data while maintaining data integrity.

## Features
- **Data Retrieval**: Fetches top posts from multiple specified subreddits, allowing for flexibility in user preferences.
- **Data Organization**: Utilizes Pandas for effective data manipulation and organization, enabling easy analysis and visualization.
- **CSV Export**: Provides functionality to export the collected data into CSV format for external use and reporting.
- **Secure Storage**: Connects to a Snowflake database for reliable and scalable data storage, ensuring long-term accessibility of the dataset.

## Technical Details
- **Libraries Used**: 
  - **PRAW**: Python Reddit API Wrapper for seamless interaction with the Reddit API.
  - **Pandas**: For data manipulation and organization.
  - **Snowflake Connector**: For secure data storage and retrieval.
- **Environment Variables**: Implements environment variables to manage sensitive information, enhancing security best practices.

## Installation
To install the necessary libraries, use the following command:
```bash
pip install praw pandas snowflake-connector-python
