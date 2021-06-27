
import pandas as pd
def main1(name1,name2,name3):
    data_m = pd.read_excel(name2)
    data_s = pd.read_excel(name1)

    data_s['physical count'] = None
    data_s['recount'] = None
    data_s["Location"]=None
    data_s["Locations"]=None


    for x in range(len(data_s['Item'])):
        for y in range(len(data_m['SKU Number'])):
            if data_s['Item'][x]==data_m['SKU Number'][y]:
                data_s['Location'][x]=data_m['Location 1'][y]

                for i in range(4,23):
                    if type(data_m.loc[y][i])==str and i==4:
                        data_s['Locations'][x]=data_m.loc[y][i]
                    elif type(data_m.loc[y][i])==str and i>=5:
                        data_s['Locations'][x]=data_s['Locations'][x]+'/'+data_m.loc[y][i]

    data_s["diff."]=None
    data_s['physical count']=data_s['physical count'].where(data_s['physical count'].notnull(), 0.00)

    for x in range(len(data_s['Quantity On Hand'])):
        data_s["diff."][x]='('+str(data_s['Quantity On Hand'][x]-data_s['physical count'][x])+')'

    data_s["Location Qty"]=None

    for x in range(len(data_s['Item'])):
        for y in range(len(data_m['SKU Number'])):
            if data_s['Item'][x]==data_m['SKU Number'][y]:
                data_s['Location Qty'][x]=data_m['Location Count'][y]

    data_s.to_excel(name3)
    return None
