import pandas as pd
import psycopg2

#read csv
df=pd.read_csv('Data\\CleanData.csv')

# Define connection parameters
conn_params = {
    "host": "127.0.0.2",
    "port": "5432",
    "user": "postgres",
    "password": input("Enter your database password: "),
    "database": "YT_Data"
}

# Establish connection
conn = psycopg2.connect(**conn_params)

# Create cursor
cur = conn.cursor()

# Define the table creation query
create_table_query = '''
CREATE TABLE IF NOT EXISTS yt (
    video_id VARCHAR PRIMARY KEY,
    channelTitle VARCHAR,
    title VARCHAR,
    description TEXT,
    tags TEXT,
    publishedAt TIMESTAMP,
    viewCount FLOAT,
    likeCount FLOAT,
    favouriteCount FLOAT,
    commentCount FLOAT,
    duration VARCHAR,
    definition VARCHAR,
    caption BOOLEAN,
    pushblishDayName VARCHAR,
    durationSecs FLOAT,
    tagCount INT
);
'''

# Execute the create table query
cur.execute(create_table_query)
conn.commit()

# Iterate through DataFrame rows and insert data into the table
for index, row in df.iterrows():
    insert_query = """
    INSERT INTO yt (
        video_id, channelTitle, title, description, tags, publishedAt,
        viewCount, likeCount, favouriteCount, commentCount, duration,
        definition, caption, pushblishDayName, durationSecs, tagCount
    )
    VALUES (%s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s);
    """
    cur.execute(insert_query, tuple(row))
    conn.commit()

# Close cursor and connection
cur.close()
conn.close()





