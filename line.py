#coding=utf-8

import requests
import json
import warnings
import time

def getLineList(src, dest):
    query_url='https://kyfw.12306.cn/otn/leftTicket/query'
    train_date='2017-06-29'
    from_station=src
    to_station=dest
    purpose_codes='ADULT'
    r=requests.get(query_url, params={'leftTicketDTO.train_date': train_date, 'leftTicketDTO.from_station': from_station, 'leftTicketDTO.to_station': to_station, 'purpose_codes': purpose_codes}, verify=False)
    obj=json.loads(r.text)
    lst=obj['data']['result']
    return lst

def getLine(src, dest):
    result=[[],[]]
    lst=getLineList(src, dest)
    for each in lst:
        tmp=each.split('|')
        s=tmp[3]+' '+src+' '+dest+' '+tmp[8]+' '+tmp[9]+' '+tmp[10]+' '
        price_url='https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice'
        train_no=tmp[2]
        from_station_no=tmp[16]
        to_station_no=tmp[17]
        seat_types=tmp[35]
        train_date='2017-06-29'

        try:
            for i in range(6):
                if i>=5:
                    raise IOError
                r=requests.get(price_url, params={'train_no': train_no, 'from_station_no': from_station_no, 'to_station_no': to_station_no, 'seat_types': seat_types, 'train_date': train_date}, verify=False)
                if(r.text.find('validateMessagesShowId')>=0):
                    break
                time.sleep(3)

            obj=json.loads(r.text)
            if 'WZ' in obj['data']:
                s=s+obj['data']['WZ'][1:]
            elif 'O' in obj['data']:
                s=s+obj['data']['O'][1:]
            else:
                raise IOError
            result[0].append(s)

        except:
            s=s+'0.0'
            result[1].append(s)

        finally:
            print(s)

        time.sleep(2)

    return result

warnings.filterwarnings("ignore")

line_require=[]
fp=open("./line_require.txt", "r", encoding="utf-8")
for line in fp:
    line=line.strip()
    if line=="": continue
    line_require.append(line.split(' '))
fp.close()

fp=open("./line.txt", "w", encoding="utf-8")
fp_bad=open("./line_bad.txt", "w", encoding="utf-8")
for each in line_require:
    result=getLine(each[0], each[1])
    for line in result[0]:
        fp.write(line+'\n')
    for line in result[1]:
        fp_bad.write(line+'\n')
    fp.flush()
    fp_bad.flush()

fp.close()
fp_bad.close()
