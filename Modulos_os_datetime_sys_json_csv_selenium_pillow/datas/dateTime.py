from datetime import datetime, timedelta

# data = datetime(2019, 4, 20, 10, 53, 20)
# print(data)  #americano

# data = datetime(2019, 4, 20, 10, 53, 20)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

# data = datetime.strptime('20/04/2019', '%d/%m/%Y')
# print(data.timestamp())

# data = datetime.fromtimestamp(1555729200.0)
# print(data)

# strtime(str, fmt)
# .strftime(fmt)
# fromtimestamp()

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('20/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')

print(d2 > d1)  #comparação se é verdadeiro ou false

# print(d1.time())

# dif = d2 - d1
# print(dif.seconds)
# print(dif.total_seconds())
# print(dif.days)


# data = data + timedelta(days=5, seconds=59)
# data = data + timedelta(seconds=2*60*60)
# data = data + timedelta(seconds=59*60)  # segundos
# print(data.strftime('%d/%m/%Y %H:%M:%S'))