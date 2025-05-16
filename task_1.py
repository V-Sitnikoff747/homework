
import random

size_1 = int(input("Введите размер первого массива: "))
size_2 = int(input("Введите размер второго массива: "))
arr1 = [random.randint(0,100) for _ in range(size_1)]
arr2 = [random.randint(0,100) for _ in range(size_2)]
arr3=[]
arr_11=[]
arr_12=[]
counter=0
min_value_1 = arr1[0]  
max_value_1 = arr1[0] 
min_value_2 = arr2[0] 
max_value_2 = arr2[0] 


for i in range(size_1):
    print(arr1[i], end=" ")
print(" ")
print("Второй массив")
print(" ")
for i in arr2:
    print(i, end=" ")
for i in arr1:
    arr3.append(i)    
for i in arr2:
    arr3.append(i)
print(" ")
print("Результирующий массив")
print(" ")
for i in arr3:
    print(i, end=" ")
arr3.clear()
print(" ")
print("Результирующий массив, который не содержит повторяющиеся элементы")
print(" ")
for i in arr1:
    if i not in arr3:
        arr3.append(i)
for i in arr2:
    if i not in arr3:
        arr3.append(i)

for i in arr3:
    print(i, end=' ')

arr3.clear()
print(" ")
print("Результирующий массив, который содержит общие элементы двух массивов")
print(" ")

for i in range(size_1):
    for j in range(size_2):
        if arr1[i]==arr2[j]:
            arr3.append(i)
            counter+=1
if counter !=0:
   for i in arr3:
       print(i, end=' ')
else:
    print("Списки не имеют одинаковых элементов")
arr3.clear()
print(" ")
print("Результирующий массив, который содержит общие элементы двух массивов")
print(" ")
for i in arr1:
    if arr1.count(i)==1:
        arr3.append(i)
for i in arr2:
    if arr2.count(i)==1:
        arr3.append(i)
for i in arr3:
    print(i, end=' ')
arr3.clear()
print(" ")
print("Результирующий массив, который содержит максимальный и минимальный элементы двух массивов")
print(" ")
for num in arr1:
    if num < min_value_1 :
        min_value_1= num
    if num > max_value_1:
        max_value_1= num
for num in arr2:
    if num < min_value_2 :
        min_value_2= num
    if num > max_value_2:
        max_value_2= num
arr3=[min_value_1,max_value_1,min_value_2,max_value_2]

for i in arr3:
    print(i, end=' ')
    

print(" ")
print("Задание №2")
print(" ")
size_3 = int(input("Введите размер  массива: "))
randomArray=[random.randint(-100,100) for _ in range(size_3)]
negativSumm=0
evenSumm=0
summOdd=0
negativArr=[]
positivArr=[]
evenArr=[]
oddArr=[]
summBetween=0
production=1
production_1=1
minValue= min(randomArray)
maxValue=max(randomArray)
minIndex=randomArray.index(minValue)
maxIndex=randomArray.index(maxValue)
firstPositiveIndex = -1
lastPositiveIndex = -1
if minIndex> maxIndex:
    maxIndex, minIndex = minIndex, maxIndex

for num in randomArray:
    print(num, end=' ')
print(' ')
for i in range(size_3):
    if randomArray[i] %2==0:
        evenSumm+= randomArray[i]
        evenArr.append(randomArray[i])
    else:
        summOdd+=randomArray[i]
        oddArr.append(randomArray[i])
    if randomArray[i]<0:
        negativSumm+=randomArray[i]
        negativArr.append(randomArray[i])
    else:
        positivArr.append(randomArray[i])
    if i%3==0:
        production*=randomArray[i]

for i in range(minIndex, maxIndex+1):
    production_1*=randomArray[i]

print(f"Сумма  четных чисел равна - {evenSumm}")
print(f"Сумма не четных чисел равна - {summOdd}")
print(f"Сумма отрицтельных чисел равна - {negativSumm}")
print(f"Произведение чисел с индексом кратным 3 равно - {production}")
print(f"Произведение чисел, находящихся между минимальным и максимальным значениями равно - {production_1}")

for i in range(size_3):
    if randomArray[i]>0:
        firstPositiveIndex=i
        break

for i in range(size_3-1,-1,-1):
    if randomArray[i]>0:
        lastPositiveIndex=i
        break

if firstPositiveIndex != -1 and lastPositiveIndex != -1 and firstPositiveIndex < lastPositiveIndex:  
    for i in range(firstPositiveIndex, lastPositiveIndex+1):
        summBetween+= randomArray[i]
else:
    print("В массиве нет двух положительных элементов")

print(f"Сумма чисел, находящихся между первым и последним положительными элементами равна - {summBetween}")
print("Массив, содержищий только положительные числа.")
print(" ")
for i in positivArr:
    print(i, end =' ')
print(' ')
print("Массив, содержищий только отрицательные числа.")
print(" ")
for i in negativArr:
    print(i, end =' ')
print(' ')
print("Массив, содержищий только четные числа.")
print(" ")
for i in evenArr:
    print(i, end =' ')
print(' ')
print("Массив, содержищий только не четные числа.")
print(" ")
for i in oddArr:
    print(i, end =' ')
print(' ')