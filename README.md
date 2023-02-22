# Twitter-Scraping
To Scrape the data I used Snscrape Package.

Built User Interface Using Streamlit.

Used Mongopy Connected with local host to Store the Data in database.

Used Padas for Data Collection

A)StreamLit

I have developed the page containing user to give details to Scrape the data such as Name, Number of Tweets Required and Date Range. It has buttons to Show Database, Upload Database to store in Mongo and Downlod To Dowload the file in Required Format such as CSV and JSON.

B)Pandas

I Have used the Pandas to add data using Append function to the dataframe so that it can collect the data with iteration using For loop. And Collected  date, id, url, tweet content, user,reply count, retweet count,language, source, like count.

C)Mongo

Stored each collection of data into a document into Mongodb along with the hashtag or key word we use to  Scrape from twitter. 

D)Covert and Download Csv and JSON file
   
Converted the dataframe to CSV and JSON and Give user download button to dowload the file.
  
