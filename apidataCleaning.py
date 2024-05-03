import pandas as pd
from dateutil import parser
import isodate


df=pd.read_csv('Data\\apiData.csv')

df.isnull().any()
df.dtypes

numeric_cols = ['viewCount', 'likeCount', 'favouriteCount', 'commentCount']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors = 'coerce', axis = 1)

df.dtypes


df['publishedAt'] =df['publishedAt'].apply(lambda x: parser.parse(x)) 
df['pushblishDayName'] = df['publishedAt'].apply(lambda x: x.strftime("%A")) 


df['durationSecs'] = df['duration'].apply(lambda x: isodate.parse_duration(x))
df['durationSecs'] = df['durationSecs'].astype('timedelta64[s]')
df['durationSecs'] = pd.to_timedelta(df['duration']).dt.total_seconds()



df[['durationSecs', 'duration']] 


df.dtypes


# Replace NaN values with an empty list
df['tags'] = df['tags'].fillna('')

# Apply lambda function to calculate tag count
df['tagCount'] = df['tags'].apply(lambda x: 0 if pd.isna(x) else len(x) if isinstance(x, list) else 0)

df.head()


df.to_csv('Data\\apiData.csv', index=False)
