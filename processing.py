import pandas as pd

l = pd.read_csv(r'F:\sai\uk-road-safety-accidents-and-vehicles\Accident_Information.csv',na_values=['None','Unclassified','Data missing or out of range','Unknown','Unallocated','Not known','Other/Not known (2005-10)'])
##??????????see model,age band columns has date

m = pd.read_csv(r'F:\sai\uk-road-safety-accidents-and-vehicles\Vehicle_Information.csv' , engine='python',na_values=['None','Unclassified','Data missing or out of range','Unknown','Unallocated','Not known','Other/Not known (2005-10)'])

combined = pd.merge(left=l,right=m, left_on='Accident_Index', right_on='Accident_Index')
print(combined.InScotland.value_counts())
combined.to_csv(r'F:\sai\combined_data.csv',index =False)

#removing redundant columns

redundant_removed = combined.drop(['Accident_Index','Location_Easting_OSGR','Location_Northing_OSGR','InScotland','Year_y','Local_Authority_(Highway)','2nd_Road_Number','1st_Road_Number'],axis=1)

redundant_removed.to_csv(r'F:\sai\redundant_removed.csv',index =False)

#removing coluns based on null or uninformative

redundant_removed.isna().sum()

thresh = redundant_removed.shape[0] * 0.4
na_removed = redundant_removed.dropna(thresh = thresh, axis = 1)
na_removed.to_csv(r'F:\sai\na_removed.csv',index =False)

#getting info about each column
print(na_removed.columns)
'''
Index(['1st_Road_Class', 'Accident_Severity', 'Date', 'Day_of_Week',
       'Did_Police_Officer_Attend_Scene_of_Accident', 'Junction_Control',
       'Junction_Detail', 'Latitude', 'Light_Conditions',
       'Local_Authority_(District)', 'Longitude', 'LSOA_of_Accident_Location',
       'Number_of_Casualties', 'Number_of_Vehicles',
       'Pedestrian_Crossing-Human_Control',
       'Pedestrian_Crossing-Physical_Facilities', 'Police_Force',
       'Road_Surface_Conditions', 'Road_Type', 'Speed_limit', 'Time',
       'Urban_or_Rural_Area', 'Weather_Conditions', 'Year_x',
       'Age_Band_of_Driver', 'Age_of_Vehicle', 'Driver_Home_Area_Type',
       'Driver_IMD_Decile', 'Engine_Capacity_.CC.', 'Junction_Location',
       'make', 'model', 'Propulsion_Code', 'Sex_of_Driver',
       'Towing_and_Articulation', 'Vehicle_Leaving_Carriageway',
       'Vehicle_Location.Restricted_Lane', 'Vehicle_Manoeuvre',
       'Vehicle_Reference', 'Vehicle_Type', 'Was_Vehicle_Left_Hand_Drive',
       'X1st_Point_of_Impact']
'''
print(na_removed.isna().sum()*100/na_removed.shape[0])
'''
1st_Road_Class                                 26.298576
Accident_Severity                               0.000000
Date                                            0.000000
Day_of_Week                                     0.000000
Did_Police_Officer_Attend_Scene_of_Accident     0.005538
Junction_Control                               36.307136
Junction_Detail                                 0.008842
Latitude                                        0.006024
Light_Conditions                                0.001215
Local_Authority_(District)                      0.000000
Longitude                                       0.006073
LSOA_of_Accident_Location                       6.762848
Number_of_Casualties                            0.000000
Number_of_Vehicles                              0.000000
Pedestrian_Crossing-Human_Control               0.031772
Pedestrian_Crossing-Physical_Facilities         0.066556
Police_Force                                    0.000000
Road_Surface_Conditions                         0.174212
Road_Type                                       0.523706
Speed_limit                                     0.003158
Time                                            0.007093
Urban_or_Rural_Area                             0.004372
Weather_Conditions                              1.801781
Year_x                                          0.000000
Age_Band_of_Driver                              7.907616
Age_of_Vehicle                                 16.418611
Driver_Home_Area_Type                          14.628490
Driver_IMD_Decile                              33.486559
Engine_Capacity_.CC.                           12.160709
Junction_Location                               0.185337
make                                            5.384987
model                                          14.543132
Propulsion_Code                                11.348479
Sex_of_Driver                                   3.543418
Towing_and_Articulation                         0.056451
Vehicle_Leaving_Carriageway                     0.058589
Vehicle_Location.Restricted_Lane                0.054605
Vehicle_Manoeuvre                               0.063010
Vehicle_Reference                               0.000000
Vehicle_Type                                    0.019432
Was_Vehicle_Left_Hand_Drive                     0.444324
X1st_Point_of_Impact                            0.076127
'''
## dropping rows of very less na columns
row_dropped = na_removed.dropna(subset=['Did_Police_Officer_Attend_Scene_of_Accident', 'Junction_Detail','Latitude', 'Light_Conditions', 'Longitude','Pedestrian_Crossing-Human_Control','Pedestrian_Crossing-Physical_Facilities', 'Road_Surface_Conditions', 'Road_Type', 'Speed_limit', 'Time','Urban_or_Rural_Area','Junction_Location','Towing_and_Articulation','Vehicle_Leaving_Carriageway', 'Vehicle_Location.Restricted_Lane','Vehicle_Manoeuvre', 'Vehicle_Reference', 'Vehicle_Type','Was_Vehicle_Left_Hand_Drive', 'X1st_Point_of_Impact'])

print(row_dropped.isna().sum()*100/row_dropped.shape[0])
'''
1st_Road_Class                                 26.127256
Accident_Severity                               0.000000
Date                                            0.000000
Day_of_Week                                     0.000000
Did_Police_Officer_Attend_Scene_of_Accident     0.000000
Junction_Control                               36.283059
Junction_Detail                                 0.000000
Latitude                                        0.000000
Light_Conditions                                0.000000
Local_Authority_(District)                      0.000000
Longitude                                       0.000000
LSOA_of_Accident_Location                       6.768060
Number_of_Casualties                            0.000000
Number_of_Vehicles                              0.000000
Pedestrian_Crossing-Human_Control               0.000000
Pedestrian_Crossing-Physical_Facilities         0.000000
Police_Force                                    0.000000
Road_Surface_Conditions                         0.000000
Road_Type                                       0.000000
Speed_limit                                     0.000000
Time                                            0.000000
Urban_or_Rural_Area                             0.000000
Weather_Conditions                              1.618095
Year_x                                          0.000000
Age_Band_of_Driver                              7.829278
Age_of_Vehicle                                 16.322470
Driver_Home_Area_Type                          14.535261
Driver_IMD_Decile                              33.396263
Engine_Capacity_.CC.                           12.054575
Junction_Location                               0.000000
make                                            5.306093
model                                          14.434176
Propulsion_Code                                11.247667
Sex_of_Driver                                   3.484500
Towing_and_Articulation                         0.000000
Vehicle_Leaving_Carriageway                     0.000000
Vehicle_Location.Restricted_Lane                0.000000
Vehicle_Manoeuvre                               0.000000
Vehicle_Reference                               0.000000
Vehicle_Type                                    0.000000
Was_Vehicle_Left_Hand_Drive                     0.000000
X1st_Point_of_Impact                            0.000000
'''
row_dropped.to_csv(r'F:\sai\row_dropped.csv',index =False)
#info about each column
for col in row_dropped.columns:
    print(row_dropped[col].value_counts())
'''
sub categorizing 1st road class

motorway and A(M) combine ---- motorway

remaining same

'''
##row_dropped = row_dropped.replace({'Day_of_Week': {'Motorway': 'motorway', 'A(M)':'motorway'}})
'''
sub categorizing junction control

stop sign and auto traffic signal--Auto traffic signal
'''
##row_dropped = row_dropped.replace({'Day_of_Week': {'Stop sign': 'Auto traffic signal'}})

'''
sub categorizing days of week

to remove skew in data we are adding friday to non weekdays 

monday to thurs-----week days(wk)
friday to sunday----non week days(nwk)

wk     0.599895
nwk    0.400105
'''
row_dropped = row_dropped.replace({'Day_of_Week': {'Friday': 'nwk', 'Saturday':'nwk','Sunday':'nwk','Monday':'wk','Tuesday':'wk','Wednesday':'wk','Thursday':'wk'}})

'''
sub categorizing junction details

not junction,slip--------------not junc-0.39
other,t or sta junction,Private drive or entrance-------junc-----0.37

cross,roundabt,more,mini-------cross----0.21
'''
row_dropped = row_dropped.replace({'Junction_Detail': {'Not at junction or within 20 metres': 'not junc', 'Slip road':'not junc','Other junction':'junc','T or staggered junction':'junc','Crossroads':'cross','Roundabout':'cross','More than 4 arms (not roundabout)':'cross','Mini-roundabout':'cross','Private drive or entrance':'junc'}})

'''
sub categorising  light conditions
because of very high skew

day light---day---0.75
remaining---night-0.25
'''
row_dropped = row_dropped.replace({'Light_Conditions': {'Daylight': 'day','Darkness - lights lit': 'night','Darkness - no lighting': 'night','Darkness - lighting unknown': 'night','Darkness - lights unlit': 'night'}})
'''
sub categorising road surface
dry---dry---70
wet,frost,snow,flood----wet----30
'''
row_dropped = row_dropped.replace({'Road_Surface_Conditions': {'Dry': 'dry', 'Wet or damp':'wet','Frost or ice':'wet','Snow':'wet','Flood over 3cm. deep':'wet'}})
'''
categorising road type

single-----0.72
dual,round,oneway,slip road---0.3
'''
row_dropped = row_dropped.replace({'Road_Type': {'Single carriageway': 'single', 'Dual carriageway':'dual','Roundabout':'dual','One way street':'dual','Slip road':'dual'}})
'''
binning time
21-4----1
4-12----2
12-16---3
16-21---4

'''

row_dropped['Time'] = pd.to_datetime(row_dropped['Time']).dt.hour


bins = [-1,4,12,16,21,24]
labels = [1,2,3,4,5]
row_dropped['Time'] = pd.cut(row_dropped['Time'], bins=bins, labels=labels)
row_dropped = row_dropped.replace({'Time': {5: 1}}) ##convert last bin to 1 i.e 21-24
'''
age band
'''
row_dropped = row_dropped.replace({'Age_Band_of_Driver': {'26 - 35': 5, '36 - 45':6,'46 - 55':7,'21 - 25':4,'56 - 65':8,'16 - 20':3,'66 - 75':9,'Over 75':10,'11 - 15':3,'6 - 10':2,'0 - 5':1}})
'''
make-----  many different categories
model----    "
Propulsion_Code---redundant column Vehicle	
Towing_and_Articulation	-----98% same value
Vehicle_Leaving_Carriageway---90% same value
Vehicle_Location.Restricted_Lane--98% same value


'''
'''
sub category manoeure

Going ahead other--------------------------stright---0.45

Turning right------------------------------turning---0.27
Going ahead right-hand bend
Going ahead left-hand bend
Turning left
Overtaking moving vehicle - offside
Reversing
Changing lane to left
Changing lane to right
U-turn
Overtaking - nearside


Waiting to go - held up-------------------static---0.27
Slowing or stopping
Parked
Overtaking static vehicle - offside
Waiting to turn right
Waiting to turn left
Moving off
'''

a1 = ['Going ahead right-hand bend','Going ahead left-hand bend','Turning left','Overtaking moving vehicle - offside','Reversing','Changing lane to left','Changing lane to right','U-turn','Overtaking - nearside','Turning right']

d1 = dict()
d1 = d1.fromkeys(a1,'turning')

a2 = ['Waiting to go - held up','Slowing or stopping','Parked','Overtaking static vehicle - offside','Waiting to turn right','Waiting to turn left','Moving off']

d2 = dict()
d2 = d2.fromkeys(a2,'static')

d1.update(d2)

d1['Going ahead other'] = 'stright'

row_dropped = row_dropped.replace({'Vehicle_Manoeuvre': d1})
'''
remove vehicle reference number no meaningful data
remove was vehicle left 99% same
'''
a1 = ['Motorcycle over 500cc','Motorcycle 125cc and under','Pedal cycle','Motorcycle over 125cc and up to 500cc','Motorcycle 50cc and under','Other vehicle','Motorcycle - unknown cc','Mobility scooter','Ridden horse','Electric motorcycle']

d1 = dict()
d1 = d1.fromkeys(a1,'light_weight')

a2 = ['Car','Taxi/Private hire car',]
d2 = dict()
d2 = d2.fromkeys(a2,'medium_weight')
a3 = ['Van / Goods 3.5 tonnes mgw or under','Bus or coach (17 or more pass seats)','Goods 7.5 tonnes mgw and over','Goods over 3.5t. and under 7.5t','Minibus (8 - 16 passenger seats)','Agricultural vehicle','Goods vehicle - unknown weight','Tram']
d3 = dict()
d3 = d3.fromkeys(a3,'high_weight')

d1.update(d2)
d1.update(d3)
row_dropped = row_dropped.replace({'Vehicle_Type': d1})
row_dropped.to_csv(r'F:\sai\sub_categorizing.csv',index =False)

row_dropped.skew(axis = 0, skipna = True) 
'''
Did_Police_Officer_Attend_Scene_of_Accident     1.850826
Latitude                                        1.023165
Longitude                                      -0.402554
Number_of_Casualties                           15.593432
Number_of_Vehicles                             11.556403
Pedestrian_Crossing-Human_Control              14.969962
Pedestrian_Crossing-Physical_Facilities         2.414783
Speed_limit                                     0.994292
Time                                           -0.055623
Year_x                                         -0.263147
Age_Band_of_Driver                              0.255781
Age_of_Vehicle                                  1.225093
Driver_IMD_Decile                               0.049044
Engine_Capacity_.CC.                            5.306806
Vehicle_Location.Restricted_Lane                8.937237
Vehicle_Reference                               7.256647
'''
print(row_dropped.isna().sum()*100/row_dropped.shape[0])
'''
1st_Road_Class                                 26.127256
Junction_Control                               36.283059
Driver_IMD_Decile                              33.396263
Driver_Home_Area_Type                          14.535261
Propulsion_Code                                11.247667

LSOA_of_Accident_Location                       6.768060  --> category data 
Weather_Conditions                              1.618095  ---> nikal becoz no previous dates

Age_Band_of_Driver                              7.829278  ---> droping row becoz of correlation
Age_of_Vehicle                                 16.322470  --->nikal column kyu ki no correlation

Engine_Capacity_.CC.                           12.054575   ---> droped column becoz of no correlation
make                                            5.306093  ---->remove rows

model                                          14.434176   ---> drop column becoz of redundent data more

Sex_of_Driver                                   3.484500  --->no corr

'''
row_dropped.to_csv(r'F:\sai\not_imputed.csv',index =False)
corr_row_dropped = row_dropped.corr()
corr_row_dropped.to_csv(r'F:\sai\corr_row_dropped.csv',index =True)
'''
imputing 1st road class through lat and log so we get total data

A           1
B           2
C       3
Motorway    4
A(M)        5
'''

import pandas as pd
row_dropped = pd.read_csv(r'F:\sai\row_dropped.csv')

row_dropped = row_dropped.replace({'1st_Road_Class': {'A': 1, 'B':2,'C':3,'Motorway':4,'A(M)':5}})
imp_df = row_dropped.loc[:,['1st_Road_Class','Latitude','Longitude']]

'''

'''
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=1)

dff = pd.DataFrame()

for i in range(81):
    imp_df = row_dropped.loc[i*25000:(i+1)*25000-1,['1st_Road_Class','Latitude','Longitude']]
    imp_df = pd.DataFrame(imputer.fit_transform(imp_df), columns = ['1st_Road_Class','Latitude','Longitude'])
    dff = pd.concat([dff,imp_df],ignore_index=True)
    print(dff.shape)

imp_df = row_dropped.loc[81*25000:,['1st_Road_Class','Latitude','Longitude']]
imp_df = pd.DataFrame(imputer.fit_transform(imp_df), columns = ['1st_Road_Class','Latitude','Longitude'])
dff = pd.concat([dff,imp_df],ignore_index=True)
print(dff.shape)

dff.dtypes

dff = dff.replace({'1st_Road_Class': {1:'A', 2:'B',3:'C',4:'Motorway',5:'A(M)'}})


#dff.to_csv(r'F:\sai\1st_Road_Class.csv',index=False)

row_dropped['1st_Road_Class'] = dff['1st_Road_Class']

row_dropped['Junction_Control'] = pd.read_csv(r'C:\Users\dbda\Desktop\junction_control.csv')['Junction_Control']
'''
sub categorizing 1st road class

motorway and A(M) combine ---- motorway

remaining same

'''
row_dropped = row_dropped.replace({'1st_Road_Class': {'Motorway': 'motorway', 'A(M)':'motorway'}})
'''
sub categorizing junction control

stop sign and auto traffic signal--Auto traffic signal
'''
row_dropped = row_dropped.replace({'Junction_Control': {'Stop sign': 'Auto traffic signal'}})


row_dropped['Driver_IMD_Decile'] = pd.read_csv(r'C:\Users\dbda\Desktop\driver_decile.csv')['Driver_IMD_Decile']



'''
imputing Driver_Home_Area_Type
'''

row_dropped = row_dropped.replace({'Driver_Home_Area_Type': {'Urban area': 1, 'Rural':2,'Small town':3}})
imp_df = row_dropped.loc[:,['Driver_Home_Area_Type','Latitude','Longitude']]


dff = pd.DataFrame()

for i in range(81):
    imp_df = row_dropped.loc[i*25000:(i+1)*25000-1,['Driver_Home_Area_Type','Latitude','Longitude']]
    imp_df = pd.DataFrame(imputer.fit_transform(imp_df), columns = ['Driver_Home_Area_Type','Latitude','Longitude'])
    dff = pd.concat([dff,imp_df],ignore_index=True)
    print(dff.shape)

imp_df = row_dropped.loc[81*25000:,['Driver_Home_Area_Type','Latitude','Longitude']]
imp_df = pd.DataFrame(imputer.fit_transform(imp_df), columns = ['Driver_Home_Area_Type','Latitude','Longitude'])
dff = pd.concat([dff,imp_df],ignore_index=True)
print(dff.shape)

dff.dtypes

dff = dff.replace({'Driver_Home_Area_Type': {1 : 'Urban area', 2:'Rural',3:'Small town'}})

row_dropped['Driver_Home_Area_Type'] = dff['Driver_Home_Area_Type'] 


row_dropped.to_csv(r'F:\sai\middle.csv',index =False)
#row_dropped  =pd.read_csv(r'F:\sai\middle.csv')
'''
imputing propulsion code based on vehicle type grouping and mode
'''
row_dropped['Propulsion_Code']=row_dropped[['Propulsion_Code']].fillna('mc')

Propulsion_Code = pd.DataFrame(row_dropped.loc[:,['Vehicle_Type','Propulsion_Code']])
def mcfunc(x):
    if x.value_counts().index[0]!='mc':
        return x.value_counts().index[0]
    elif x.value_counts().shape[0]==1:
        return 'no propulsion'
    else:
        return x.value_counts().index[1]
        
mc_df=pd.DataFrame(Propulsion_Code.groupby(['Vehicle_Type']).agg(lambda x:mcfunc(x)))
df1 = mc_df.to_dict()

dff11 = df1.values()

for i in dff11:
    dff = i

xxx1 = pd.DataFrame()
#based on vehicle type propulsion code filled
xxx1['Propulsion_Code']= row_dropped.apply(lambda row: dff[row['Vehicle_Type']] if row['Propulsion_Code'] == 'mc' else row['Propulsion_Code'],axis=1)


    
row_dropped['Propulsion_Code'] = xxx1['Propulsion_Code']



row_dropped = row_dropped.replace({'Sex_of_Driver': {1:'Male', 2:'Female'}})

row_dropped.to_csv(r'F:\sai\imputed_lsoa_present_.csv',index =False)



row_dropped.drop(['LSOA_of_Accident_Location','Age_of_Vehicle','Engine_Capacity_.CC.','model'],axis=1,inplace=True)

row_dropped.dropna(inplace=True)

row_dropped.shape # (1763197, 38)
print(row_dropped.isna().sum()*100/row_dropped.shape[0])
'''
1st_Road_Class                                 0.0
Accident_Severity                              0.0
Date                                           0.0
Day_of_Week                                    0.0
Did_Police_Officer_Attend_Scene_of_Accident    0.0
Junction_Control                               0.0
Junction_Detail                                0.0
Latitude                                       0.0
Light_Conditions                               0.0
Local_Authority_(District)                     0.0
Longitude                                      0.0
Number_of_Casualties                           0.0
Number_of_Vehicles                             0.0
Pedestrian_Crossing-Human_Control              0.0
Pedestrian_Crossing-Physical_Facilities        0.0
Police_Force                                   0.0
Road_Surface_Conditions                        0.0
Road_Type                                      0.0
Speed_limit                                    0.0
Time                                           0.0
Urban_or_Rural_Area                            0.0
Weather_Conditions                             0.0
Year_x                                         0.0
Age_Band_of_Driver                             0.0
Driver_Home_Area_Type                          0.0
Driver_IMD_Decile                              0.0
Junction_Location                              0.0
make                                           0.0
Propulsion_Code                                0.0
Sex_of_Driver                                  0.0
Towing_and_Articulation                        0.0
Vehicle_Leaving_Carriageway                    0.0
Vehicle_Location.Restricted_Lane               0.0
Vehicle_Manoeuvre                              0.0
Vehicle_Reference                              0.0
Vehicle_Type                                   0.0
Was_Vehicle_Left_Hand_Drive                    0.0
X1st_Point_of_Impact                           0.0
'''
row_dropped = pd.read_csv(r'F:\sai\final_zero_nulls.csv')
'''
Weather_Conditions preprocess

Fine no high winds       81.738569
Raining no high winds    12.114585
Other                     2.042767
Raining + high winds      1.417369
Fine + high winds         1.271837
Snowing no high winds     0.699298
Fog or mist               0.578154
Snowing + high winds      0.137421
Name: Weather_Conditions, dtype: float64'''

row_dropped = row_dropped.replace({'Weather_Conditions': {'Fine no high winds': 'fine', 'Fine + high winds':'fine','Raining no high winds':'rain','Other':'rain','Raining + high winds':'rain','Snowing no high winds':'rain','Fog or mist':'rain','Snowing + high winds':'rain'}})
row_dropped.to_csv(r'F:\sai\final_zero_nulls.csv',index =False)





