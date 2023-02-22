import streamlit as st
import pandas as pd
import pymongo 
import snscrape.modules.twitter as sn
import datetime


# To create Front end user interface
st.title(":earth_africa: Twitter Scraping Project")
st.subheader(':page_with_curl: Enter Details')

col1, col2, col3= st.columns(3)

col1, col2, col3 = st.columns([4, 4, 4])

with col1:
    text=st.text_input("Search text",value="Type here")
    number = st.number_input("Limit the tweet count",1)
    

with col2:   
    start_date=st.date_input('From Date',value=datetime.date(2023,1,1))
    end_date=st.date_input('To Date',value=None)

#To Scrape the twitter data using Snscrape
Twitter_data=[]
for i,tweet in enumerate(sn.TwitterSearchScraper('{} since:{} until:{}'.format(text,start_date,end_date)).get_items()):
    if i >= int(number):
        break
    #To append data in the dataframe
    Twitter_data.append([tweet.date,tweet.id,
                         tweet.url,tweet.content,
                         tweet.user.username,
                         tweet.replyCount, tweet.retweetCount,
                         tweet.lang,tweet.hashtags,tweet.likeCount, 
                         tweet.sourceLabel]
                        )
    #to give column names
    tweets_df = pd.DataFrame(Twitter_data, columns=[ "Date Tweeted", 
                                                  "Twitter ID", "URL",
                                                  "Tweet Content","Username",
                                                  "Reply Count","Retweet Count",
                                                  "Language","Hastags","Like Count",
                                                  "Source"])
   

#To display Dataframe
st.subheader(":chart_with_upwards_trend: Scraped Dataframe")
if st.button("Show Table"):
    st.dataframe(Twitter_data)
    

co1,co2=st.columns(2)
co1, co2 = st.columns([5,5])

#To upload Data in Mongo
with co1:
    st.subheader(':arrow_double_up: MongoDB')
    if st.button('Upload to My Twitter Database'):
            client = pymongo.MongoClient("mongodb://Localhost:27017/")
            db=client['tweet']
            collection=db['Twitter_data']
            tweets_df.reset_index(inplace=True)
            My_dict=tweets_df.to_dict("records")
            collection.insert_many(My_dict)
        
#Function for Csv FIle Convert    
def convert_df_to_csv(df):
    return df.to_csv().encode('utf-8')
    
with co2 :   
    st.subheader(':arrow_double_down: Download data ')
    st.download_button(
        label="CSV Format",
        data=convert_df_to_csv(tweets_df),
        file_name='Twitter_data.csv',
        mime='text/csv',
        )

#Function for Json FIle Convert               
def convert_df_to_json(df):
    return df.to_json().encode('utf-8')
    
with co2 :    
    st.download_button(
        label="JSON Format",
        data=convert_df_to_json(tweets_df),
        file_name='Twitter_data.json',
    
           )