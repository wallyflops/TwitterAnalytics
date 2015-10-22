import analyticsexport


USERNAME = ""
PASSWORD = ""
ANALYTICS_ACCOUNT = ""
NUM_DAYS = 7
OUTPUT_DIRECTORY = "C:\Projects\TwitterAnalyticsExport\Output"

analyticsexport.twitter_flow(USERNAME, PASSWORD, ANALYTICS_ACCOUNT, NUM_DAYS, OUTPUT_DIRECTORY)
