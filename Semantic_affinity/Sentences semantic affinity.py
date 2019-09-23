import math

print("Введите любые три предложения для определения их лексической близости.")

sentence_1 = input("Предложение №1: ").split()
sentence_2 = input("Предложение №2: ").split()
sentence_3 = input("Предложение №3: ").split()
print("")

#set of words for "sentence_1" - set_1
set_1 = set(sentence_1)
set_2 = set(sentence_2)
set_3 = set(sentence_3)

USSR = set_1.union(set_2.union(set_3))
USSR = list(USSR)

" --- Создаём матрицу --- "

#первое предложение "sentence_1"
matrix_for_sentence_1 = {}

for word in sentence_1:
    for element_number in range(len(USSR)):
        if word == USSR[element_number]:
            matrix_for_sentence_1[(0, element_number)] = matrix_for_sentence_1.get((0, element_number), 0) + 1            

#второе предложение "sentence_2"
matrix_for_sentence_2 = {}

for word in sentence_2:
    for element_number in range(len(USSR)):
        if word == USSR[element_number]:
            matrix_for_sentence_2[(0, element_number)] = matrix_for_sentence_2.get((0, element_number), 0) + 1            

#третье предложение "sentence_3"
matrix_for_sentence_3 = {}

for word in sentence_3:
    for element_number in range(len(USSR)):
        if word == USSR[element_number]:
            matrix_for_sentence_3[(0, element_number)] = matrix_for_sentence_3.get((0, element_number), 0) + 1            

" --- Считаем степень близости для каждого из предложений --- "

#degree of proximity between "sentence_1" and "sentence_2" - D_1_2
D_1_2 = 0
for X_Y_1 in matrix_for_sentence_1:
    for X_Y_2 in matrix_for_sentence_2:
        D_1_2 += math.sqrt(((X_Y_1[0] - X_Y_2[0])**2) + ((X_Y_1[1] - X_Y_2[1])**2))
        
print("Степень близости первого и второго предложений - ", str(int(D_1_2)) + "%")

#degree of proximity between "sentence_1" and "sentence_3" - D_1_3
D_1_3 = 0
for X_Y_1 in matrix_for_sentence_1:
    for X_Y_2 in matrix_for_sentence_3:
        D_1_3 += math.sqrt(((X_Y_1[0] - X_Y_2[0])**2) + ((X_Y_1[1] - X_Y_2[1])**2))
        
print("Степень близости первого и третьего предложений - ", str(int(D_1_3)) + "%")

#degree of proximity between "sentence_2" and "sentence_3" - D_2_3
D_2_3 = 0
for X_Y_1 in matrix_for_sentence_2:
    for X_Y_2 in matrix_for_sentence_3:
        D_2_3 += math.sqrt(((X_Y_1[0] - X_Y_2[0])**2) + ((X_Y_1[1] - X_Y_2[1])**2))
        
print("Степень близости второго и третьего предложений - ", str(int(D_2_3)) + "%")
print("")

if D_1_2 < D_1_3 < D_2_3:
    print("Второе и третье предложения имеют минимальное расстояние между собой.")

elif D_1_2 > D_1_3 > D_2_3:
    print("Первое и второе предложения имеют минимальное расстояние между собой.")

else:
    print("Первое и третье предложения имеют минимальное расстояние между собой.")
