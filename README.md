# XMbDi
Xiaomi Mi Band Data Import


Insert in "Input_data_divided" the un-zipped file exported from your xiaomi account. You should have 6 folder:
* ACTIVITY
* DOBY
* HEARTRATE
* SLEEP
* SPORT 
* USER 

each folder should contain only one csv file. 

This first **Alpha** should simply create a sqlite database wqith 6 tables corresponding to the aforementioned categories. 

Urgent to do: 
- Time conversion based on a precise time-zone 

To do: 
- Work with just the zip provided by Xiaomi. 

In the next versions: 
- UI. Still to decide what I'll use. I'll probably give "pywebview" a try, but i might convert the script in Kotlin or other languages in order to build an application able to run on mobile devices. 
- Export your data to Google Fit (maybe Apple Health) 
