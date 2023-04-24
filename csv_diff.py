import pandas as pd
dfA = pd.read_csv("purge_event_qa.csv")
dfB = pd.read_csv("purge_event_qa_backup.csv")


dfDiff = pd.concat([dfA, dfB]).drop_duplicates(subset='event_start_date',keep=False)
dfDiff.to_csv('dfDiff.csv')
print(dfDiff)