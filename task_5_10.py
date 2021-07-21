from datetime import datetime
train = [{'train_num': '123', 'station_arrive': 'Grodno', 'time_arrive': '10:00', 'station_otprav': 'Minsk', 'time_otprav': '7:00'},
         {'train_num': '56', 'station_arrive': 'Moskow', 'time_arrive': '11:30', 'station_otprav': 'Mogilev', 'time_otprav': '8:00'},
         {'train_num': '1036', 'station_arrive': 'Kyiv', 'time_arrive': '15:00', 'station_otprav': 'Minsk', 'time_otprav': '7:30'},
         {'train_num': '123', 'station_arrive': 'Brest', 'time_arrive': '12:10','station_otprav': 'Minsk', 'time_otprav': '8:15'}]
FMT = '%H:%M'
d = '7:20'
for i in range(len(train)):
    delta = datetime.strptime(train[i].get('time_arrive'), FMT) - datetime.strptime(train[i].get('time_otprav'), FMT)
    print(delta)
    if str(delta) > d:
        print(train[i])








