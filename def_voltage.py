#Вычисление напряжения комплекса по номеру биглбона
import re
import requests

test_bb = '2812BB001395'

def number_bb_get():
    #получаем файл с данными
    bb_list = requests.get('http://tech.emercit.com/state.html')
    bb_number = []
    #берем только строку, содержащуюю ББ
    for i in bb_list.text.split():
        if re.findall(r'loadCharts', i):
            bb_number.append(i[-20:-8])
    return bb_number

def voltage_get (bb):
    #делаем запрос лога
    agk = requests.get('http://emercit.com/tech3/log.php?bb=' + str(bb))
    #проходим циклом по всем строкам полученного лога
    for i in agk.text.split():
        #выбираем только строки, содержащие значение напряжения
        voltage_level_str = re.findall(r'volt', i)
        if voltage_level_str != []:
            voltage = i[10:15]
            return voltage
#функция пробегает по списку ББ и находит их напряжение
def bb_to_voltage():
    for i in number_bb_get():
        print(i, ' ', voltage_get(i), '\n')
bb_to_voltage()
