import datetime
from datetime import date
d1 = datetime.datetime(2014, 7, 16, 23)
d2 = datetime.datetime.now()

petdtnascto = datetime.date(2024, 1, 1)
today = date.today()
petidade = today.month - petdtnascto.month - (today.day < petdtnascto.day)
print(petidade)
diff = d2 - d1

days = diff.days
years, days = divmod(days, 365)
months, days = divmod(days, 30)

seconds = diff.seconds
hours, seconds = divmod(seconds, 3600)
minutes, seconds = divmod(seconds, 60)

print(
    f"Desde {d1} passaram {years} anos, {months} meses, {days} dias, {hours} horas, {minutes} minutos e {seconds} segundos")