
import datetime, locale
locale.setlocale(locale.LC_ALL, "es-Es ")
fecha  = datetime.datetime(1999, 10, 10)

print(fecha.strftime("%M"))