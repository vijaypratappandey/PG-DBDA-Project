import requests
import pandas as pd
df = pd.read_csv(r'C:\Users\dbda\Desktop\lat_long_parts\tot2.csv')
df.columns


response = None
roads = []
cities = []


for i in df.itertuples():
    print(i)
    try:
        response = requests.get('https://us1.locationiq.com/v1/reverse.php?key=be7dfdc7a8184f&lat={0}&lon={1}&format=json'.format(i.LATITUDE,i.LONGITUDE))
        z = response.text
        road = z.split('road')[-1].split(',')[0].strip('":')
        city = z.split('city')[-1].split(',')[0].strip('":')
        print(city,' ---> ',road)
        cities.append(city)
        roads.append(road)
        print()
    except Exception as e:
        print(e)
        if city == '':
            cities.append('No city')
        if city!='':
            cities.append(city)
        if road=='':
            roads.append(road)
        if road!='':
            roads.append(road)
            
df['road']=pd.Series(roads)
df['city']=pd.Series(cities)
df.to_csv(r'C:\Users\dbda\Desktop\lat_long_parts\PANDEY_latlong_tot_3_5.csv',index =False)
