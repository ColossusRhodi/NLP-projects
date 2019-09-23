import sys, math

def Euclid(*arguments):

    ' --- Составляем матрицу предложения на слова --- '

    USSR = list(set(Text_to_M_1.split()).union(set(Text_to_M_2.split())))
    
    matrix_1 = {}
    
    for word in sentence_1.split():
        for No_element in range(len(USSR)):
            if word == USSR[No_element]:
                matrix_1[(0, No_element)] = matrix_1.get((0, No_element), 0) + 1
                
    matrix_2 = {}
    
    for word in sentence_2.split():
        for No_element in range(len(USSR)):
            if word == USSR[No_element]:
                matrix_2[(1, No_element)] = matrix_2.get((1, No_element), 0) + 1
    
    ' --- Составляем списки с координатами слов --- '
                
    #Coordinates list for a sentence from the 'File_1' - CL_Sentence_1
    CL_Sentence_1 = list(matrix_1.keys())
    
    #Coordinates list for a sentence from the 'File_2' - CL_Sentence_2
    CL_Sentence_2 = list(matrix_2.keys())

    ' --- Считаем "близость" предложений по евклидову расстоянию --- '
    
    #Degree of proximity between 'CL_Sentence_1' and 'CL_Sentence_2' - D_1_2
    D_1_2 = 0

    for x_y_1 in CL_Sentence_1:
        for x_y_2 in CL_Sentence_2:
            D_1_2 += math.sqrt(((x_y_1[0] - x_y_2[0])**2) + ((x_y_1[1] - x_y_2[1])**2))
    
    return D_1_2

def Pearson(*arguments):

    ' --- Составляем матрицу предложения на слова --- '

    USSR = list(set(Text_to_M_1.split()).union(set(Text_to_M_2.split())))

    matrix_1 = {}
    
    for word in sentence_1.split():
        for No_element in range(len(USSR)):
            if word == USSR[No_element]:
                matrix_1[(0, No_element)] = matrix_1.get((0, No_element), 0) + 1
    
    matrix_2 = {}
    
    for word in sentence_2.split():
        for No_element in range(len(USSR)):
            if word == USSR[No_element]:
                matrix_2[(1, No_element)] = matrix_2.get((1, No_element), 0) + 1
    
    ' --- Составляем списки с координатами слов --- '
    
    #Coordinates list for a sentence from the 'File_1' - CL_Sentence_1
    CL_Sentence_1 = list(matrix_1.values())
    
    #Coordinates list for a sentence from the 'File_2' - CL_Sentence_2
    CL_Sentence_2 = list(matrix_2.values())

    ' --- Считаем "близость" предложений по коэффициенту корреляции пирсона --- '
    
    Up = 0
    for x_y_1 in CL_Sentence_1:
        for x_y_2 in CL_Sentence_2:
            Up =+ (x_y_1 - (len(CL_Sentence_1)/len(USSR)))*(x_y_2 - (len(CL_Sentence_2)/len(USSR)))
    
    Down = 0
    for x_y_1 in CL_Sentence_1:
        for x_y_2 in CL_Sentence_2:
            Down =+ ((x_y_1 - (len(CL_Sentence_1)/len(USSR)))**2)*((x_y_2 - (len(CL_Sentence_2)/len(USSR)))**2)

    if Down != 0:
        r = Up / math.sqrt(Down)
        return r

try:
    #Путь к проге и аргументы: LR_8_3_Rozhin.py LR_8_3_Два_капитана.txt LR_8_3_Капитанская_дочь.txt LR_8_3_Save.txt
    File_1 = open(sys.argv[1], 'r', encoding = 'utf-8')
    Text_1 = File_1.read()
    
    File_2 = open(sys.argv[2], 'r', encoding = 'utf-8')
    Text_2 = File_2.read()

    File_3 = open('StopWords_EN_for_LR8.txt', 'r', encoding = 'utf-8')
    StopWords = File_3.read()

    #Signs of the end-of-sentence - EndSigns
    EndSigns = ('.', '!', '?')
    punctuation_marks = (".", ",", ":", ";", "'", '"', "-")

    #File_1
    ' --- Ищем границы заголовков в тексте --- '
    
    string_1 = ''
    for each in Text_1:
        if each != '\n':
            string_1 += each
        else:
            if string_1[-1] not in EndSigns:
                string_1 += '. '
            else:
                string_1 + ' '

    for each in EndSigns:
        string_1 = string_1.replace(each, '$')
        
    #Text to extract sentences - T_extract
    T_extract_1 = string_1.split('$')
    
    ' --- Удаляем знаки препинания --- '
    
    string_2 = ''
    for symbol in string_1:
        if symbol not in punctuation_marks:
            string_2 += symbol

    ' --- Удаляем стоп-слова --- '
    
    string_3 = ''
    for symbol in string_2.split():
        if symbol.lower() not in StopWords.split():
            string_3 += symbol
            string_3 += ' '

    #Text to create matrix - Text_to_M_1
    Text_to_M_1 = string_3
    Text_to_M_1 = Text_to_M_1.replace('$', '').lower()
    
    ' --- Разбиваем текст на предложения --- '
        
    text_1 = string_3.lower().split('$')
    if text_1[-1] == ' ':
        text_1.pop()
    
    #File_2
    ' --- Ищем границы заголовков в тексте --- '

    string_1 = ''
    for each in Text_2:
        if each != '\n':
            string_1 += each
        else:
            if string_1[-1] not in EndSigns:
                string_1 += '. '
            else:
                string_1 + ' '

    for each in EndSigns:
        string_1 = string_1.replace(each, '$')
        
    #Text to extract sentences - T_extract
    T_extract_2 = string_1.split('$')
    
    ' --- Удаляем знаки препинания --- '
    
    string_2 = ''
    for symbol in string_1:
        if symbol not in punctuation_marks:
            string_2 += symbol
    
    ' --- Удаляем стоп-слова --- '
    
    string_3 = ''
    for symbol in string_2.split():
        if symbol.lower() not in StopWords.split():
            string_3 += symbol
            string_3 += ' '

    #Text to create matrix - Text_to_M_2
    Text_to_M_2 = string_3
    Text_to_M_2 = Text_to_M_2.replace('$', '').lower()
    
    ' --- Разбиваем текст на предложения --- '

    text_2 = string_3.lower().split('$')
    if text_2[-1] == ' ':
        text_2.pop()
    
    ' --- Обращаемся к функции Euclid --- '
    
    Euclid_dict = {}

    No_sentence_1 = 0
    for sentence_1 in text_1:
        if len(sentence_1) != 0:
            No_sentence_1 += 1
            No_sentence_2 = 0
            for sentence_2 in text_2:
                if len(sentence_2) != 0:
                    No_sentence_2 += 1
                    E = Euclid(sentence_1, sentence_2)
                    if (No_sentence_2, No_sentence_1) not in Euclid_dict.values():
                        Euclid_dict[E] = No_sentence_1, No_sentence_2
    
    ' --- Обращаемся к функции Pearson --- '
    
    Pearson_dict = {}

    No_sentence_1 = 0
    for sentence_1 in text_1:
        if len(sentence_1) != 0:
            No_sentence_1 += 1
            No_sentence_2 = 0
            for sentence_2 in text_2:
                if len(sentence_2) != 0:
                    No_sentence_2 += 1
                    P = Pearson(sentence_1, sentence_2)
                    if (No_sentence_2, No_sentence_1) not in Pearson_dict.keys():
                        Pearson_dict[No_sentence_1, No_sentence_2] = P

    ' --- Сохраняем результаты --- '
    
    Save = open(sys.argv[3], 'w', encoding = 'utf-8')
    
    Save.write('\tЛексически \"близкие\" предложения\n\n')#?
    Save.write('-Евклидово расстояние-\n\n')
    
    No = 1
    if str(max(Euclid_dict.keys()))[0] != 1:
        for each in Euclid_dict.keys():
            if each >= float(str(int(str(max(Euclid_dict.keys()))[0]) - 1) + str(max(Euclid_dict.keys()))[1:]):
                Save.write("Совпадение №" + str(No) + '\n')
                if len(T_extract_1[Euclid_dict[each][0]]) != 0 and len(T_extract_2[Euclid_dict[each][1]]) != 0:
                    Save.write("Предложение из первого текста - " + '\"' + T_extract_1[Euclid_dict[each][0]] + '\"' + '\n')
                    Save.write("Предложение из второго текста - " + '\"' + T_extract_2[Euclid_dict[each][1]] + '\"' + '\n' + '\n')
                    No += 1
    
    Save.write('-Коэффициента корреляции Пирсона-\n\n')

    #Pearson list without identic items - PL_without_i
    PL_without_i = []
    
    for each in Pearson_dict.items():
        if each[1] and float(each[1]) > 1:
            write_1 = "Предложение из первого текста - " + '\"' + T_extract_1[each[0][0]] + '\"' + '\n'
            write_2 = "Предложение из второго текста - " + '\"' + T_extract_2[each[0][1 - 1]] + '\"' + '\n' + '\n'
            if (write_1, write_2) not in PL_without_i:
                PL_without_i.append((write_1, write_2))
   
    No = 1
    for each in PL_without_i:
        Save.write("Совпадение №" + str(No) + '\n')
        Save.write(str(each[0]))
        Save.write(str(each[1]))
        No += 1
                
    File_1.close()
    File_2.close()
    File_3.close()
    Save.close()
    
except FileNotFoundError:
    print("!Вы ввели имя файла неверно или не указали его расширение!")
    print("\tПример ввода -> LR_8_3_Два_капитана.txt LR_8_3_Капитанская_дочь.txt LR_8_3_Save.txt")
except IndexError:
    print("!Вы не указали один из файлов!")
    print("\tПример ввода -> LR_8_3_Два_капитана.txt LR_8_3_Капитанская_дочь.txt LR_8_3_Save.txt")
    

