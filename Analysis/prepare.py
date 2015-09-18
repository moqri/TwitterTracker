import pandas as pd
tweets_raw=pd.DataFrame.from_csv("tweets.csv")
print tweets_raw.head()
raw_input("Press Enter to continue...")