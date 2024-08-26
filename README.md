
# YT_ETL Data Analytics

## Project Link
Power BI Dash Board: [Link](https://app.powerbi.com/links/qLs5SvBDqt?ctid=d6011d6b-35d1-495c-a859-c8b56d77536b&pbi_source=linkShare&bookmarkGuid=e16ab9b5-1e70-4e2b-8d00-2fece18ab6ac)<br>
For more details, visit the [project repository](https://github.com/Shyam414/YT_Data).

# Introduction

Hi Shyam Sundar! The project's objective is to utilize YouTube APIs to extract data from various YouTube channels with different channel IDs. Following data extraction, the data will be cleaned and loaded into a PostgreSQL database. Subsequently, Power BI will be employed to visualize the data. The primary aim is to establish a seamless pipeline from API extraction to visualization.

## Data_Architecture
<img src="img.png">


## Technology Used
- Programming Language - Python
- Storage - PostgreSQL
- Data Visualization - PowerBI
- deployment - Github
- source-You Tube API

  Data Pipeine : Api-->Python-->Postgresql--> Python-->Postgresql-->PowerBI

## Dataset source
==>To create an API key for accessing the YouTube Data API, you can follow these steps:

1)Go to the Google Cloud Console: https://console.cloud.google.com/apis/credentials  
2)If prompted, sign in with your Google account.<br>
3)Once logged in, select the project where you want to create the API key, or create a new project if needed. You can do this by clicking on the project dropdown menu at the top of the page.<br>
4)Once you've selected or created the project, click on the "Create credentials" button and select "API key" from the dropdown menu.<br>
5)Your API key will be generated. Make sure to copy and securely store the API key, as you'll need it to authenticate your requests to the YouTube Data API.<br>
==>For data extraction from YouTube, you can follow the steps outlined in the guide provided at the following link: https://developers.google.com/youtube/v3/docs <br>
1)This resource explains how to use the YouTube Data API to extract, preprocess, and analyze data from YouTube channels using Python. <br>2)The guide covers web scraping techniques, data preprocessing, and analysis methods to retrieve information such as video titles, views, durations, and more. <br>3)By following the instructions in the guide, you can effectively extract and analyze YouTube data for various purposes.

## Data Model
video_id,
    channelTitle,<br>
    title,<br>
    description,<br>
    tags,<br>
    publishedAt,<br>
    viewCount,<br>
    likeCount,<br>
    favouriteCount,<br>
    duration,<br>
    commentCount,<br>
    definition,<br>
    caption,<br>
    pushblishDayName,<br>
    durationSecs,<br>
    tagCount 

## Data Visualization
<img src="YT DB.gif">
