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


    tag = re.search(r'_[a-z]*', word)

    cur.execute('SELECT * FROM NP WHERE Tag LIKE ' + '"' +tag.group(0)+ '"')
    data = cur.fetchall()
    if len(data) > 0:

        candidate_to_NP += ' ' +word
    else:

        if candidate_to_NP != '':
            candidate_list = candidate_to_NP[1:].split()
            

            first_tag = re.search(r'_[a-z]*', candidate_list[0])

            cur.execute('SELECT * FROM Function WHERE Tag LIKE ' + '"' +first_tag.group(0)+ '"')
            data = cur.fetchall()
            while len(data) > 0 and len(candidate_list) > 1:
                candidate_list.pop(0)
                first_tag = re.search(r'_[a-z]*', candidate_list[0])

                cur.execute('SELECT * FROM Function WHERE Tag LIKE ' + '"' +first_tag.group(0)+ '"')
                data = cur.fetchall()
                

            last_tag = re.search(r'_[a-z]*', candidate_list[-1])

            cur.execute('SELECT * FROM Function WHERE Tag LIKE ' + '"' +last_tag.group(0)+ '"')
            data = cur.fetchall()
            while len(data) > 0 and len(candidate_list) > 1:
                candidate_list.pop(-1)
                last_tag = re.search(r'_[a-z]*', candidate_list[-1])

                cur.execute('SELECT * FROM Function WHERE Tag LIKE ' + '"' +last_tag.group(0)+ '"')
                data = cur.fetchall()
                

            if len(candidate_list) == 1:
                one_tag = re.search(r'_[a-z]*', candidate_list[0])
                if one_tag.group(0) == '_ns':

                    candidate_without_tag = candidate_list[0][:one_tag.span(0)[0]]

                    if candidate_without_tag not in nominal_groups:
                        nominal_groups.append(candidate_without_tag)
                        
                    candidate_to_NP = ''
            else:
                candidate_without_tags = ''
                for candidate in candidate_list:

                    del_tag = re.search(r'_[a-z]*', candidate)
                    candidate_without_tag = candidate[:del_tag.span(0)[0]]
                    candidate_without_tags += candidate_without_tag
                
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
