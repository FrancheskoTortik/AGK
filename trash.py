import report
import datetime

def body_mail():
    region = []
    number_agk = []
    voltage = []
    data_time = []
    datetime.datetime.now()
    for x in report.number_bb_get():
        region.append(report.find_region(x))
        number_agk.append(str(report.number_agk_get(x)[0]))
        voltage.append(report.voltage_get(x))
        data_time.append(datetime.datetime.now())

    titles = ['Район', 'Номер АГК', 'Напряжение АКБ', 'Время измерения']
    data = [titles] + list(zip(region, number_agk, voltage, data_time))
    result  = '\n'

    print(type(data), data)
    for i, d in enumerate(data):
        print(i, d)

        line = '|'.join(str(x).ljust(22) for x in d)
        result += str(line) + '\n'

        #print(line)
        if i == 0:
            result = '-' * len(line) + '\n'

            print('-' * len(line) + '\n')

    return result
print(body_mail())