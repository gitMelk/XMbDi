# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 13:51:41 2020
@author: melk
# Xiaomi Health data Import 
"""
import glob
import numpy as np
import pandas as pd
import math

import sqlite3

DATABASE_NAME = "HealthData.db"

all_health_data = sqlite3.connect('database/'+DATABASE_NAME)


categories = ["ACTIVITY","BODY",
              "HEARTRATE","SLEEP",
              "SPORT","USER"]
#%%
# init dataset
init_database_table = True
if(init_database_table):

    c = all_health_data.cursor()
    
    # Create tables
    
    c.execute('''CREATE TABLE IF NOT EXISTS "activity"("date" text, "lastSyncTime" int, "steps" int, 
                 "distance" int, "runDistance" int, "calories" int)''') 
    
    c.execute('''CREATE TABLE IF NOT EXISTS "body"("timestamp" int, "weight" int, "height" int, 
                 "bmi" real, "fatRate" int, "bodyWaterRate" int, "boneMass" int,
                 "metabolism" int, "muscleRate" int, "visceralFat" int,
                 "impedance" int)''') 
    
    c.execute('''CREATE TABLE IF NOT EXISTS "heartrate"("date" int, "lastSyncTime" int, "heartRate" text, 
                 "timestamp" text)''') 
    
    c.execute('''CREATE TABLE IF NOT EXISTS "sleep"("date" text, "lastSyncTime" int, "deepSleepTime_min" int, 
                 "shallowSleepTime_min" int, "wakeTime" int, "start_s" int, "stop_s" int)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS "sport"("type" int, "startTime" int, "sportTime" int, 
                 "distance" real, "maxPace" real, "minPace" int, "avgPace" real,
                 "calories" int)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS "user"("userId" int, "gender" int, "height" int, 
                 "weight" real, "nickName" text, "avatar" blob, "birthday" text)''')
    
    
    # Insert a row of data
    
    # Save (commit) the changes
    all_health_data.commit()
    
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    all_health_data.close()


#%% ACTIVITY
all_health_data = sqlite3.connect('database/'+DATABASE_NAME)

input_data_path = 'Input_data_divided/' + categories[0] + '/'

data_name = glob.glob(input_data_path+'*.csv')

data_raw = pd.read_csv(data_name[0], sep=',',dtype='str',encoding="utf-8")
c = all_health_data.cursor()

for x in range(data_raw.shape[0]):
    params = (data_raw.iloc[x,0],
              data_raw.iloc[x,1],
              data_raw.iloc[x,2],
              data_raw.iloc[x,3],
              data_raw.iloc[x,4],
              data_raw.iloc[x,5])
    c.execute("INSERT INTO activity VALUES (?, ?, ?, ?, ?, ?)", params)

all_health_data.commit()
all_health_data.close()
#%% BODY
all_health_data = sqlite3.connect('database/'+DATABASE_NAME)

input_data_path = 'Input_data_divided/' + categories[1] + '/'

data_name = glob.glob(input_data_path+'*.csv')

data_raw = pd.read_csv(data_name[0], sep=',',dtype='str',encoding="utf-8")
c = all_health_data.cursor()

for x in range(data_raw.shape[0]):
    params = (data_raw.iloc[x,0],
              data_raw.iloc[x,1],
              data_raw.iloc[x,2],
              data_raw.iloc[x,3],
              data_raw.iloc[x,4],
              data_raw.iloc[x,5],
              data_raw.iloc[x,6],
              data_raw.iloc[x,7],
              data_raw.iloc[x,8],
              data_raw.iloc[x,9],
              data_raw.iloc[x,10])
    c.execute("INSERT INTO body VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)
    

all_health_data.commit()
all_health_data.close()
#%% HEARTRATE
all_health_data = sqlite3.connect('database/'+DATABASE_NAME)

input_data_path = 'Input_data_divided/' + categories[2] + '/'

data_name = glob.glob(input_data_path+'*.csv')

data_raw = pd.read_csv(data_name[0], sep=',',dtype='str',encoding="utf-8")
c = all_health_data.cursor()

for x in range(data_raw.shape[0]):
    params = (data_raw.iloc[x,0],
              data_raw.iloc[x,1],
              data_raw.iloc[x,2],
              data_raw.iloc[x,3])
    c.execute("INSERT INTO heartrate VALUES (?, ?, ?, ?)", params)
    

all_health_data.commit()
all_health_data.close()



#%% SLEEP
all_health_data = sqlite3.connect('database/'+DATABASE_NAME)

input_data_path = 'Input_data_divided/' + categories[3] + '/'

data_name = glob.glob(input_data_path+'*.csv')

data_raw = pd.read_csv(data_name[0], sep=',',dtype='str',encoding="utf-8")
c = all_health_data.cursor()

for x in range(data_raw.shape[0]):
    params= (data_raw.iloc[x,0], 
                data_raw.iloc[x,1], 
                data_raw.iloc[x,2],
                data_raw.iloc[x,3], 
                data_raw.iloc[x,4], 
                data_raw.iloc[x,5],
                data_raw.iloc[x,6])
              
    c.execute("INSERT INTO sleep VALUES (?, ?, ?, ?, ?, ?, ?)", params)    

all_health_data.commit()
all_health_data.close()
#%% SPORT
all_health_data = sqlite3.connect('database/'+DATABASE_NAME)

input_data_path = 'Input_data_divided/' + categories[4] + '/'

data_name = glob.glob(input_data_path+'*.csv')

data_raw = pd.read_csv(data_name[0], sep=',',dtype='str',encoding="utf-8")
c = all_health_data.cursor()

for x in range(data_raw.shape[0]):
    params = (data_raw.iloc[x,0],
              data_raw.iloc[x,1],
              data_raw.iloc[x,2],
              data_raw.iloc[x,3],
              data_raw.iloc[x,4],
              data_raw.iloc[x,5],
              data_raw.iloc[x,6],
              data_raw.iloc[x,7])
    c.execute("INSERT INTO sport VALUES (?, ?, ?, ?, ?, ?, ?, ?)", params)

all_health_data.commit()
all_health_data.close()

#%% USER
all_health_data = sqlite3.connect('database/'+DATABASE_NAME)

input_data_path = 'Input_data_divided/' + categories[5] + '/'

data_name = glob.glob(input_data_path+'*.csv')

data_raw = pd.read_csv(data_name[0], sep=',',dtype='str',encoding="utf-8")
c = all_health_data.cursor()

for x in range(data_raw.shape[0]):
  params = (data_raw.iloc[x,0],
              data_raw.iloc[x,1],
              data_raw.iloc[x,2],
              data_raw.iloc[x,3],
              data_raw.iloc[x,4],
              data_raw.iloc[x,5],
              data_raw.iloc[x,6])
    
  c.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?)", params)


all_health_data.commit()
all_health_data.close()
#%%
all_health_data = sqlite3.connect('database/'+DATABASE_NAME)
c = all_health_data.cursor()


counter = 0
for row in c.execute('SELECT * FROM user'):
        counter += 1 
        print(row)
        if(counter== 10): break

all_health_data.commit()
all_health_data.close()



