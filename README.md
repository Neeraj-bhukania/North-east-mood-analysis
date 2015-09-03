# North-east-mood-analysis

A tool to extract data  from online newspapers / magazines that focuses on north east India ! 

A python script has been written 

-> Article-scraper.py - It scraps the data from thenortheasttoday.com of all the 8 states (northeast states along with arunachal                         pradesh). It currently loops over the first 4 pages and in all total 287 articles have been extracted .

A tool to auto parse the content into major and minor issues over time 

->LDA.py - It implements the Latent Dirichlet Allocation (LDA) algorithm over the extracted articles and gives us the major and            minor issues over time

A tool to extract the tweets based on the topics found with the help of LDA.py and perform sentiment analysis

->Twitter.py - Twitter data extraction is done with the help of tweepy module and Sentiment analysis is done with the help of                  textblob module .


