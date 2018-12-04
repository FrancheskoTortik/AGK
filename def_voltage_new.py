#Вычисление напряжения комплекса по номеру биглбона
import re
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

test_bb = '2812BB001395'
def number_agk_get():
    # получаем файл с данными
    agk_list = requests.get('http://tech.emercit.com/state.html')
    agk_number = []
    # берем только строку, содержащуюю ББ
    for i in agk_list.text.split('<'):
        if re.findall('АГК', i):
            #print('AGK-' + i.split('>')[1].split('-')[1])
            agk_number.append('AGK-' + i.split('>')[1].split('-')[1])
        elif re.findall('ЭМЕРСИТ', i):
            #print('AGK-'+ i.split('>')[1].split('-')[1])
            agk_number.append('EMERCIT-'+ i.split('>')[1].split('-')[1])
    return agk_number

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

def info_voltage():
    info_agk = []
    no_data_from_agk = []
    agk_allert = ''
    for i in range(len(number_bb_get())):
        try:
            if float(voltage_get(number_bb_get()[i])) < 12.0:

                agk_tmp = []
                agk_tmp.append(number_bb_get()[i])
                agk_tmp.append(number_agk_get()[i])
                agk_tmp.append(voltage_get(number_bb_get()[i]))
                info_agk.append(agk_tmp)

        except:
            agk_tmp = []
            agk_tmp.append(number_bb_get()[i])
            agk_tmp.append(number_agk_get()[i])
            agk_tmp.append(voltage_get(number_bb_get()[i]))
            no_data_from_agk.append(agk_tmp)

            continue
    info_agk.sort(key=lambda i : i[2])
    #ata = open('data.txt', 'a', encoding='UTF-8')

    for x in no_data_from_agk:
        agk_allert = agk_allert + '\t' + str(x[0]) +'-------->' + str(x[1]) +'-------->' +  str(x[2]) + '\n'
        #data.write(str(x[0]) + ' ' + str(x[1])+ ' ' + str(x[2]) + '\n')
    for y in info_agk:
        agk_allert = agk_allert +'\t' + str(y[0]) +'-------->' + str(y[1]) + '-------->' +str(y[2]) + '\n'
        #data.write(str(y[0]) + ' ' + str(y[1]) + ' ' + str(y[2]) + '\n')
    #data.close()
    return agk_allert #info_agk, no_data_from_agk
msg = MIMEMultipart()
addr_from = '8600999@gmail.com'
addr_to = '4008@emercit.ru'
password = 'qwerty8600999'
msg['From'] = addr_from
msg['To'] = addr_to
msg['Subject'] = 'Report_voltage'
body =''' \tДобрый день! Высылаю напряжение АКБ:\n
''' + info_voltage()
msg.attach(MIMEText(body,'plain'))
smpt_obj = smtplib.SMTP('smtp.gmail.com', 587)
#smpt_obj.set_debuglevel(True)
smpt_obj.ehlo()
smpt_obj.starttls()
smpt_obj.login('8600999@gmail.com', password)
smpt_obj.send_message(msg)
smpt_obj.quit()