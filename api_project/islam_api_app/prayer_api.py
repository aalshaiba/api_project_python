from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime, timedelta
from rest_framework import serializers
import base64


class Prayer:
    def __init__(self, englishname, time, arabicname):
        self.englishname = englishname
        self.time = time
        self.arabicname = arabicname


class PrayerSerializer(serializers.Serializer):
    englishname = serializers.CharField(max_length=100)
    time = serializers.CharField(max_length=100)
    arabicname = serializers.CharField(max_length=100)


def get_prayer():
    url = 'http://m.awqaf.ae/prayertimes.aspx'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    englishnames = ['Al Fajr', 'Al Shurooq', 'Al Dhuhr', 'Al Asr', 'Al Maghreb', 'Al Esha']
    nn = ['الفجر', 'الشروق', 'الظهر', 'العصر', 'المغرب', 'العشاء']
    arabicnames = []
    for n in nn:
        n = base64.b64encode(n.encode('utf-8'))
        n = base64.b64decode(n)
        arabicnames.append(n)

    prayers = []
    ul = soup.find('ul', {'data-role': 'listview'})

    for item, name1, name2 in zip(ul.find_all('li'), englishnames, arabicnames):
        t = re.findall('\d+:\d+', item.text)
        tim = datetime.strptime(t[0], '%I:%M')
        p = Prayer(englishname=name1, time=tim, arabicname=name2)

        prayers.append(p)

    for index, prayer in enumerate(prayers):
        if index == 2 or index == 3 or index == 4 or index == 5:
            prayer.time = prayer.time + timedelta(hours=12)

    for x in prayers:
        x.time = x.time.strftime('%I:%M %p')

    serializer = PrayerSerializer(prayers, many=True)

    return serializer.data


def month_def(months, m):
    for i, mon in enumerate(months):
        if i == (int(m.text) - 1):
            return months[i]


def get_date():
    url = 'http://m.awqaf.ae/prayertimes.aspx'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    day = soup.find('span', {'id': 'ContentPlaceHolder1_DataList1_HDayLabel_0'})
    month = soup.find('span', {'id': 'ContentPlaceHolder1_DataList1_HMonthLabel_0'})
    year = soup.find('span', {'id': 'ContentPlaceHolder1_DataList1_HYearLabel_0'})

    months = ['محرم', 'صفر', 'ربيع الأول', 'ربيع الثاني', 'جمادى الأولى', 'جمادى الآخرة', 'رجب', 'شعبان', 'رمضان',
              'شوال', 'ذو القعدة', 'ذو الحجة']

    months_english = ['Muharram', 'Safar', 'Rabee - 1', 'Rabee - 2', 'Jumada Al Ola ', 'Jumada Al Akhera', 'Rajab', 'Shaaban',
                      'Ramadan', 'Shawwal', 'Dhu Al Qida', 'Dhu Al Hija']

    m = month_def(months, month)
    english_mont = month_def(months_english, month)

    return [day.text.strip(), m,year.text.strip(), english_mont]
