#Вычисление напряжения комплекса по номеру биглбона
import os
import re
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders                                # Импортируем энкодер
from email.mime.base import MIMEBase
import region_dict
from email.mime.image import MIMEImage
import mimetypes


test_bb = '2018BBBB0BAC'
def number_agk_get(bb):
    # получаем файл с данными

    agk_list = requests.get('http://tech.emercit.com/state.html')

    # берем только строку, содержащуюю ББ
    for i in agk_list.text.split('onclick'):

        if re.findall(str(bb), i) != []:
            if re.findall('АГК',i):
                agk_number = re.findall(r'АГК-\d+', i)
            elif re.findall('ЭМЕРСИТ', i):
                agk_number = re.findall(r'ЭМЕРСИТ-\d+\w*', i)



    return agk_number #возвращает номер АГК


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
    voltage = '--.--'
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
    #data = open('data.txt', 'a', encoding='UTF-8')

    for x in no_data_from_agk:
        try:
            agk_allert = agk_allert + '\t' + str(x[2]) + '-------->' + str(x[1]) + '-------->' + region_dict.region_dick[str(x[1][-4:])] + '\n'
        except:
            agk_allert = agk_allert + '\t' + str(x[2]) + '-------->' + str(x[1]) + '-------->' + "Район Неизвестен" + '\n'

    for y in info_agk:
        agk_allert = agk_allert +'\t' + str(y[2]) +'-------->' + str(y[1]) + '-------->' +str(y[0]) + '\n'
        #data.write(str(y[0]) + ' ' + str(y[1]) + ' ' + str(y[2]) + '\n')
    #data.close()
    return agk_allert #info_agk, no_data_from_agk
email_list = ['4008@emercit.ru']# 'm.ovsienko@emercit.ru', ]

def find_region(bb):
    agk = number_agk_get(bb)[0].split('-')[1]
    region = "Неизвестно"

    try:
        if int(agk) in region_dict.region_dick.keys():

            region = region_dict.region_dick[int(agk)]
    except:
        try:
            region = region_dict.region_dick[agk[1:]]
        except:
            region = 'Неизвестно'
    return region
    #print(number_agk_get())


hhh = 0
a = open('2.txt', 'a', encoding='UTF-8')
def voltage_report():
    report_temp = []
    report_no_data = []
    report_str = ''
    for x in number_bb_get():
        try:
            if float(voltage_get(x)) < 12.0:

                report = []
                report.append(voltage_get(x))
                report.append(number_agk_get(x))
                report.append(find_region(x))
                report_temp.append(report)
        except:
            report = []
            report.append(voltage_get(x))
            report.append(number_agk_get(x))
            report.append(find_region(x))
            report_temp.append(report)
    report_temp.sort(key=lambda i : i[2])
    report_no_data.sort(key=lambda i: i[2])


    for y in report_no_data:

        a.write('|'.join(str(x).ljust(17) for x in [str(y[0]), str(y[1][0]), str(y[2])]) + '\n')

    for z in report_temp:
        a.write('|'.join(str(x).ljust(17) for x in [str(z[0]), str(z[1][0]), str(z[2])]) + '\n')

    return report_str

voltage_report()
a.close()
report = ''
msg = MIMEMultipart()
filepath = '2.txt'
filename = os.path.basename(filepath)
if os.path.isfile(filepath):                              # Если файл существует
  ctype, encoding = mimetypes.guess_type(filepath)        # Определяем тип файла на основе его расширения
  if ctype is None or encoding is not None:               # Если тип файла не определяется
      ctype = 'application/octet-stream'                  # Будем использовать общий тип
  maintype, subtype = ctype.split('/', 1)                 # Получаем тип и подтип
  if maintype == 'text':                                  # Если текстовый файл
      with open(filepath, encoding='utf-8') as fp:                          # Открываем файл для чтения
          file = MIMEText(fp.read(), _subtype=subtype)
          # Используем тип MIMEText
          fp.close()                                      # После использования файл обязательно нужно закрыть
  elif maintype == 'image':                               # Если изображение
      with open(filepath, 'rb') as fp:
          file = MIMEImage(fp.read(), _subtype=subtype)
          fp.close()
  elif maintype == 'audio':                               # Если аудио
      with open(filepath, 'rb') as fp:
          file = MIMEAudio(fp.read(), _subtype=subtype)
          fp.close()
  else:                                                   # Неизвестный тип файла
      with open(filepath, 'rb') as fp:
          file = MIMEBase(maintype, subtype)              # Используем общий MIME-тип
          file.set_payload(fp.read())                     # Добавляем содержимое общего типа (полезную нагрузку)
          fp.close()
      encoders.encode_base64(file)                        # Содержимое должно кодироваться как Base64
  file.add_header('Content-Disposition', 'attachment', filename=filename) # Добавляем заголовки
  msg.attach(file)                                        # Присоединяем файл к сообщению


if hhh ==0:
    for x in email_list:

        addr_from = '8600999@gmail.com'
        addr_to = x
        password = 'qwerty8600999'
        msg['From'] = addr_from
        msg['To'] = addr_to
        msg['Subject'] = 'Report_voltage'
        body =''' \tДобрый день! Высылаю напряжение АКБ:\n
        '''
        msg.attach(MIMEText(body,'plain'))
        smpt_obj = smtplib.SMTP('smtp.gmail.com', 587)
        #smpt_obj.set_debuglevel(True)
        smpt_obj.ehlo()
        smpt_obj.starttls()
        smpt_obj.login('8600999@gmail.com', password)
        smpt_obj.send_message(msg)
        smpt_obj.quit()