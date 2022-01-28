import requests
import json
import pandas as pd
import time
import datetime

def main():
    tables = []
    
    for i in range(373801, 378500, 1000): #цикл по longitude
         for j in range(556101, 559001, 1000): #цикл по latitude
            time.sleep(1)
            lng = i/10000
            lat = j/10000
            params = {'lng': lng, 'lat': lat}
            response_new = requests.get('https://carsharing-search.ru/cars',
            params=params)
            # print(response.url)
            data_new = json.loads(response_new.text)
            Table_new = pd.DataFrame.from_records(data_new['data'])
            tables.append(Table_new) 
        
    
    mod_Table = pd.concat(tables)
    mod_Table.drop_duplicates(subset=['latitude', 'longitude'])    #Называем файл по дате
    file_name="Day_"+datetime.datetime.today().strftime("%Y-%m-%d")+".csv"
    # df = pd.read_csv('.csv', usecols=['model', 'price'])
    mod_Table.to_csv(file_name,index = False)

# добавьте время
if __name__ == '__main__':
    main()