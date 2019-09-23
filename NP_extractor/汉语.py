import sqlite3 as SQLite
import re

file_name = input('Input file: ')

if file_name[-4:] != '.txt':
    file_name += '.txt'

file = open(file_name, 'r', encoding = 'utf-8')
text = file.read()

nominal_groups = []

candidate_to_NP = ''
for word in text.split():
    
    con = SQLite.connect('汉语 data.db')
    cur = con.cursor()

    #Поиск тегов именных групп.
    tag = re.search(r'_[a-z]*', word)
    #Запрос о наличие тега.
    cur.execute('SELECT * FROM NP WHERE Tag LIKE ' + '"' +tag.group(0)+ '"')
    data = cur.fetchall()
    if len(data) > 0:
        #Формирование кандидата в именную группу.
        candidate_to_NP += ' ' +word
    else:
        #Исключение пустых строк.
        if candidate_to_NP != '':
            candidate_list = candidate_to_NP[1:].split()
            
            #Удаление союзов, предлогов и вспомогательных частиц из начала кандидата.
            first_tag = re.search(r'_[a-z]*', candidate_list[0])
            #Запрос о наличие тега.
            cur.execute('SELECT * FROM Function WHERE Tag LIKE ' + '"' +first_tag.group(0)+ '"')
            data = cur.fetchall()
            while len(data) > 0 and len(candidate_list) > 1:
                candidate_list.pop(0)
                first_tag = re.search(r'_[a-z]*', candidate_list[0])
                #Запрос о наличие тега.
                cur.execute('SELECT * FROM Function WHERE Tag LIKE ' + '"' +first_tag.group(0)+ '"')
                data = cur.fetchall()
                
            #Удаление союзов, предлогов и вспомогательных частиц из конца кандидата.
            last_tag = re.search(r'_[a-z]*', candidate_list[-1])
            #Запрос о наличие тега.
            cur.execute('SELECT * FROM Function WHERE Tag LIKE ' + '"' +last_tag.group(0)+ '"')
            data = cur.fetchall()
            while len(data) > 0 and len(candidate_list) > 1:
                candidate_list.pop(-1)
                last_tag = re.search(r'_[a-z]*', candidate_list[-1])
                #Запрос о наличие тега.
                cur.execute('SELECT * FROM Function WHERE Tag LIKE ' + '"' +last_tag.group(0)+ '"')
                data = cur.fetchall()
                
            #Удаление кандидата, состоящего из одного иероглифа и не обозначающего географический объект.
            if len(candidate_list) == 1:
                one_tag = re.search(r'_[a-z]*', candidate_list[0])
                if one_tag.group(0) == '_ns':
                    #Удаление тега части речи.
                    candidate_without_tag = candidate_list[0][:one_tag.span(0)[0]]
                    #Запись именной группы в список именных групп.
                    if candidate_without_tag not in nominal_groups:
                        nominal_groups.append(candidate_without_tag)
                        
                    candidate_to_NP = ''
            else:
                candidate_without_tags = ''
                for candidate in candidate_list:
                    #Удаление тегов частей речи.
                    del_tag = re.search(r'_[a-z]*', candidate)
                    candidate_without_tag = candidate[:del_tag.span(0)[0]]
                    candidate_without_tags += candidate_without_tag
                #Запись именной группы в список именных групп.
                if candidate_without_tags not in nominal_groups:
                    nominal_groups.append(candidate_without_tags)

                    candidate_without_tags = ''
                candidate_to_NP = ''

save = open('中文字典.txt', 'w', encoding = 'utf-8')

No = 1
for NP in nominal_groups:
    save.write(str(No)+ '. ' +NP+ '\n')
    No += 1
    
file.close()
con.close()
save.close()

print('\nChinese dictionary of nominative phrases was created successfully.')
