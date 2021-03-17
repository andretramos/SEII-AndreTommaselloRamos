import datetime
import pytz

d = datetime.date(2016,7,24)
tday = datetime.date.today()

print(d)
print(tday)
print(tday.weekday())
print(tday.isoweekday())

#weekday -> 0 à 6  segunda à domingo 
#isoweekday -> 1 à 7 segunda à domingo

tdelta = datetime.timedelta(days=7)

print(tday + tdelta)
print(tday - tdelta)

#date2 = date1 + timedelta
#timedelta = date1 + date2

bday = datetime.date(2022, 3, 8)
till_bday = bday - tday

print(till_bday.days)
print(till_bday.total_seconds())

t = datetime.time(9, 30, 35, 100000)
print(t.hour)

dt = datetime.datetime(2016,7,26,12,30,45,100000)
print(dt)
print(dt.date())
print(dt.time())

tdelta = datetime.timedelta(days=7)
print(dt + tdelta)

tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo = pytz.UTC)
print(dt_utcnow)

dt_utcnow = dt_now

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

# for tz in pytz.all_timezones:
# 	print(tz)

#dt_mtm = datetime.datetime.now()
#mtn_tz = pytz.timezone('US/Mountain')
#dt_mtn = mtn_tz.localize(dt_mtn)

print(dt_mtn.isoformat())
print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'March 17, 2021'

dt = datetime.datetime.strptime(dt_str,'%B %d, %Y')
print(dt) 

#strftime -> Datetime para string
#strptime -> String para datetime




