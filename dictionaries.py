import re
'''
choice_1='0'
players = {}
print("Привет!!! Желаешье сохранить память о своем кумире баскетбола?\n\nТогда набери 1, если нет - нажми любую клавишу")
choice_1=input("Сделай свой выбор: ")
while True:
    
    if choice_1.isdigit() and choice_1=='1':
     while True:
        id = input("Введите в цифровом формате уникальный ID баскетболиста: ")
        if id.isdigit() and id[0]!='0':
            break
        else:
            print("Ошибка ввода. Введите пожалуйста в ID цифровое значение начиная с 1.")
            
    while True:
        valid=True
        surname= input("Введи фамилию: ")
        for i in surname:
            if i.isdigit():
                print("Вы вписали в фамилию цифру. Будьте внимательны и повторите ввод.")
                valid=False
                break
        if valid:
            break   

    while True:
        valid=True
        name= input("Введи имя: ")
        for i in name:
            if i.isdigit():
                print("Вы вписали в имя цифру. Будьте внимательны и повторите ввод.")
                valid=False
                break
        if valid:
            break   

    while True:
        valid=True
        patronymic=input("Введи отчество: ")
        for i in patronymic :
            if i.isdigit():
                print("В отчество игрока вы вписали цифру. Будьте внимательны и повторите ввод.")
                valid=False
                break
        if valid:
            break       

    while True:
        height=input("Введи рост: ")
        
        if re.match("^\d+,\d+$", height) or re.match("^\d+$", height):
                height = height.replace(',', '.')
                height=float(height)   
                break
        else:
            print("Ошибка!!! Проверьте правильность ввода роста игрока!!!")
         
     
    players[id] = {"Surname": surname,"Name": name,"Patronymic": patronymic, "height": height}

    print("Ваш кумир успешно сохранен. Если желаете еще кого-то сохранить нажмите 1,\n если нет, тогда любую другую клавишу.")
    choice_1=input("Сделай свой выбор: ")
    if choice_1 !='1':
        break
     
    
       
choice_2= input("Если хотите поработать со списком нажмите 1, если нет- любую другую клавишу и Вы покините програму: ")

if choice_2.isdigit() and choice_2=='1':

  if choice_2.isdigit() and choice_2 == '1':
    while True:
        print("Ниже приведены действия, которые можно совершать со списком:")
        print("1. Удалить баскетболиста")
        print("2. Найти баскетболиста")
        print("3. Заменить данные баскетболиста")
        print("4. Показать всех баскетболистов")

        choice = input("Выберите опцию (1-4): ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 4:
                
                if choice == 1:
                    id = input("Введите ID баскетболиста для удаления: ")
                    if id in players:
                        del players[id]
                        print(f"Баскетболист с ID {id} удалён.")
                    else:
                        print(f"Баскетболист с таким ID не найден.")
                elif choice == 2:
                    id = input("Введите ID баскетболиста для поиска: ")
                    if id in players:
                        player = players[id]
                        print(f"Баскетболист: {player['Surname']},{player['Name']},{player['Patronymic']}, рост - {player['height']} см.")
                    else:
                        print(f"Баскетболист с таким ID не найден.")
                elif choice == 3:
                    
                    while True:
                     id = input("Введите  ID баскетболиста для замены данных: ")
                     if id.isdigit() and id[0]!='0':
                        break
                     else:
                        print("Ошибка ввода. Введите пожалуйста в ID цифровое значение начиная с 1.")
                    if id in players:
                         while True:
                            valid=True
                            newSurname=input("Введите новую фамилию баскетболиста: ")
                            for i in newSurname:
                                if i.isdigit():
                                    print("Вы вписали в фамилию цифру. Будьте внимательны и повторите ввод.")
                                    valid=False
                                    break
                            if valid:
                                break   

                         while True:
                            valid=True
                            newName=input("Введите новое имя баскетболиста: ")
                            for i in newName:
                                if i.isdigit():
                                    print("Вы вписали в имя цифру. Будьте внимательны и повторите ввод.")
                                    valid=False
                                    break
                            if valid:
                                break   

                         while True:
                            valid=True
                            newPatronymic=input("Введите новое отчество баскетболиста: ")
                            for i in newPatronymic:
                                if i.isdigit():
                                    print("В отчество игрока вы вписали цифру. Будьте внимательны и повторите ввод.")
                                    valid=False
                                    break
                            if valid:
                                break       

                         while True:
                            newHeight = float(input("Введите новый рост баскетболиста в сантиметрах: "))
                            if re.match("^\d+,\d+$", height) or re.match("^\d+$", height):
                                    newHeight = newHeight.replace(',', '.')
                                    height=float(newHeight)   
                                    break
                            else:
                                print("Ошибка!!! Проверьте правильность ввода роста игрока!!!")

                            players[id]["Surname"] = newSurname
                            players[id]["Name"] = newName
                            players[id]["Patronymic"] = newPatronymic
                            players[id]["height"] = newHeight

                            print(f"\nДанные баскетболиста с ID {id} обновлены.")
                            print(f"\n Теперь по ID {id} зарегистрирован баскетболист {players[id]['Surname']},{players[id]['Name']},{players[id]['Patronymic']}, рост - {players[id]['height']} см.")
                    else:
                        print(f"Баскетболист с таким ID не найден.")
                elif choice == 4:
                    if players:
                        print("\nСписок всех баскетболистов:")
                        for id, player in players.items():
                            print(f"ID: {id}, ФИО: {player['Surname']},{player['Name']},{player['Patronymic']}, рост - {player['height']} см. ")
                    else:
                        print("Список баскетболистов пуст.")

                continue_choice = input("\nХотите продолжить работать со списком? Если да нажмите 1, если нет- любую другую клавишу: ")
                if continue_choice != '1':
                 print("Спасибо за использование программы. До свидания!!!")
                 break    
            else:
                print("Ошибка: выберите число от 1 до 4 и повторите ввод.\n")
                 
        else:
             print("Ошибка: введено не число. Пожалуйста, выберите число от 1 до 4 и повторите ввод.\n")
      
else:
   print("Спасибо за использование программы. До свидания!!!")
   '''
'''
englishRussianDictionary= {}
russianEnglishDictionary= {}
length= len(englishRussianDictionary)
english_pattern = r'^[a-zA-Z-]+$'  
russian_pattern = r'^[а-яА-ЯёЁ-]+$'
print("\nЗадание №2")
print("Реализуем англо-русски словарь")
choiceDictionary= input("Если хочешь поработать со словарем нажми 1, если нет - нажми любую другую клавишу ")
if choiceDictionary=='1':
    while True:
        print("Выбери операцию, какую хочешь провести:")
        print("1. Добавить новое слово.")
        print("2. Искать слово")
        print("3. Удалить слово")
        print("4. Заменить слово")
        print("5. Показать словарь")
        while True:
            choiceDictionary_1= input("Сделай свой выбор ")
            if choiceDictionary_1.isdigit():
                choiceDictionary_1= int(choiceDictionary_1)
                if 1<=choiceDictionary_1 and choiceDictionary_1<=5:
                    print("Отлично. Вы сделали свой выбор.\n")
                    break
                else:
                    print("Ошибка!!! Для выбора операции необходимо использовать цифры от 1 до 5. Повторите ввод")
            else:
                print("Ошибка!!! Для выбора операции необходимо использовать цифры от 1 до 5. Повторите ввод")

        if  choiceDictionary_1 ==1 :
            while True:
                englishWord= input("Введите слово на английском языке : ")
                if re.match(english_pattern, englishWord):
                    if englishWord in englishRussianDictionary:
                        print("Такое слово уже имеется в словаре. Может Вы имели ввиду другое слово?")
                    else:
                        break
                else:
                    print("Ошибка!!! При вводе слова на английском языке можно использовать только литиницу и тире.\nПовторите ввод.")
        if choiceDictionary_1 !=5 and choiceDictionary_1 !=1 and length !=0 :
            while True:
                englishWord= input("Введите слово на английском языке : ")
                if re.match(english_pattern, englishWord):
                    break
                else:
                    print("Ошибка!!! При вводе слова на английском языке можно использовать только литиницу и тире.\nПовторите ввод.")
        if choiceDictionary_1 ==1:
            while True:
                russianWord=input("Введите его перевод на русском: ")
                if re.match(russian_pattern,russianWord):
                    break
                else:
                    print("Ошибка!!! При  вводе слова на руском языке можно использовать только кириллицу и тире.\nПовторите ввод.")

        if choiceDictionary_1 ==1:
                englishRussianDictionary[englishWord]= [russianWord]
                russianEnglishDictionary[russianWord]= englishWord
                length=len(englishRussianDictionary)
                if englishWord in englishRussianDictionary:
                    print(f"Поздравляю слово {englishWord} успешно добавлено в ловарь.")

        elif choiceDictionary_1 ==2:
            if length !=0:
                if englishWord in englishRussianDictionary:
                    print(f"Слово {englishWord} имеет на русском языке такие значения как: {englishRussianDictionary[englishWord]}")
                else:
                    print("В словаре такое слово как {englishWord} пока отсутствует.")
                    choiceDictionary_2= input("Если хотите его добавить в словарь то нажмите 1, если нет, тогда любую другую клавишу")
                    if choiceDictionary_2=='1':
                        englishRussianDictionary[englishWord]= [russianWord]
                        russianEnglishDictionary[russianWord]= englishWord
            else:
                print("Список пуст, поэтому поиск невозможен.")


        elif choiceDictionary_1 ==3:
             if length !=0:
                if englishWord in englishRussianDictionary:
                    del englishRussianDictionary[englishWord]
                    length=len(englishRussianDictionary)
                    print(f"Слово {englishWord} успешно удалено из списка")
                else:
                    print("В словаре такое слово как {englishWord} отсутствует.")
             else:
                 print("Список пуст, поэтому любое удаление невозможно.")
            

        elif choiceDictionary_1 ==4: 
             if length !=0:
                while True:
                    while True:
                     choice_4= input("Если хотите заменить слово тогда нажмите 1, если хотите добавить перевод тогда 2") 
                     if choice_4.isdigit() and (choice_4=='1' or choice_4=='2'):
                            break
                     else:
                            print("Ошибка!!! При выборе необходимо использовать цифровые значени или 1 или 2. Повторите ввод.")
                        
                    if choice_4=='1':
                            while True:
                                englishWord_1= input(f"Введите слово, на которое хотите заменить слово {englishWord}  : ")
                                if re.match(english_pattern, englishWord_1):
                                    if englishWord==englishWord_1:
                                      print("ОШибка!!! Вы хотите заменить слово на само себя. Будте внимательны")
                                    else:
                                        break
                                else:
                                    print("Ошибка!!!! Для ввода английского слова допустимо использовать только латиницу и тире.")
                            
                            englishRussianDictionary[englishWord_1]= englishRussianDictionary.pop(englishWord)  
                                  
                    else:
                        while True:
                            russianWord_1= input("Введите слово, которое хотите добавить в перевод.")
                            if re.match(russian_pattern,russianWord_1):
                                englishRussianDictionary[englishWord].append(russianWord_1)
                                break
                            else:
                                print("Ошибка!!! Слово на русском языке может содержать  только кирилицу и тире. Повторите ввод")
                    break
             else:
                 print("Список пуст, поэтому замена невозможна.")

                               
        elif choiceDictionary_1 ==5:  
            
            if length !=0:
                print("Русско-английский словарь\n")
                for key  in englishRussianDictionary:
                    print(f"{key} перевод: {englishRussianDictionary[key]}")
            else:
                print("Словарь пока не заполнен.")
         
        choiceAction=input("Если хочешь продолжить работу со словарем нажми 1, если нет - тогда любую другую клавишу.")
        if choiceAction !='1':
            print("Работа приложения окончена!!! Хорошего дня!!!!")
            break
            

else:
    print("Работа приложения окончена!!! Хорошего дня!!!!")
'''

print("Задание №3\n")
employees={}
employeeKey=()
namePattern = r'^[а-яА-ЯёЁ-]+$'
phonePattern = r'^\+\d{12}$'
emailPattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
skypePattern = r'^[a-zA-Z][a-zA-Z0-9._-]{5,31}$'
dateBirthPattern= r'^\d{2}.\d{2}.\d{4}$'

companyChoice=input("Хочешь поработать с данными о работниках своей компании нажми 1,\n если нет - тогда нажми любую другую склавишу ")
print("Отлично!!!! Вы сделали свой выбор.\n")
if  companyChoice=='1':
    while True:
        print("Возможные операции со списком сотрудников:")
        print("1. Добавить нового сотрудника.")
        print("2. Искать сотрудника")
        print("3. Удалить сотрудника")
        print("4. Заменить данные сотрудника")
        print("5. Показать всех сотрудников")
        while True:   
            chooseEmployee= input("Выбери желаемую операцию ")
            if chooseEmployee.isdigit():
                chooseEmployee=int(chooseEmployee)
                if 1<=chooseEmployee and chooseEmployee<=5:
                    break
                else:
                    print("Ошибка ввода!!! Выбор операции осуществляется путем нажатия одной из клавиш со значением от 1 до 5, включительно. Повторите ввод. ")
            else:
                print("Ошибка ввода!!! Вы ввели некорректное значение. Повторите ввод. ")

        if  chooseEmployee==1:
            while True:
                employeeSurname = input("Введите фамилию работника ")
                if re.match(namePattern,employeeSurname):
                    break
                else:
                    print("Ошибка ввода!!! Фамилия должна содержать только буквенные значения кирилицы.\nПовторите ввод")

            while True:
                employeeName= input("Введите имя работника ")
                if re.match(namePattern,employeeName):
                    break
                else:
                    print("Ошибка ввода!!! Имя должно содержать только буквенные значения кирилицы.\nПовторите ввод")

            while True:
                employeeMiddleName= input("Введите отчество работника ")
                if re.match(namePattern,employeeMiddleName):
                    break
                else:
                    print("Ошибка ввода!!! Отчество должно содержать только буквенные значения кирилицы.\nПовторите ввод")

            while True:
                    dateBirth= input("Введите дату рождения работника как показано в скобках (05.05.1980) ")
                    if re.match(dateBirthPattern,dateBirth):
                        break
                    else:
                        print("Ошибка ввода!!! Отчество должно содержать только буквенные значения кирилицы.\nПовторите ввод")   

            employeeKey = (employeeSurname, employeeName, employeeMiddleName,  dateBirth) 
            if employeeName in employees:
                chooseEmployee_1="Такой сотрудник уже есть в базе данных. Вы уверены, что хотите продолжить?\nЕсли да, то нажмите 1, если нет- любую другую клавишу "
                if chooseEmployee_1!='1':
                    break

            while True:
                jobTitle=input("Введите должность работника ")
                if re.match(namePattern,jobTitle):
                    break
                else:
                    print("Ошибка ввода!!! Имя должно содержать только буквенные значения кирилицы.\nПовторите ввод")


            while True:
                telefonNumber=input("Введите номер телефона работника в международном формате например: +380971234567.\nВведите номер: ")
                if re.match(phonePattern,telefonNumber):
                    break
                else:
                    print("Ошибка ввода!!! Номер содержит некорректные символы или недостаточноцифр.\nПовторите ввод")

            while True:
                email=input("Введите Email-адрес работника ")
                if re.match(emailPattern,email):
                    break
                else:
                    print("Ошибка ввода!!! Email-адрес содержит недопустимые символы.\nПовторите ввод")

            while True:
                skype = input("Введите Skype работника ")
                if re.match(skypePattern,skype):
                    break
                else:
                    print("Ошибка ввода!!! Skype-адрес содержит недопустимые символы.\nПовторите ввод")
            
            employees[employeeKey]={
            'Должность': jobTitle,
            'Телефон': telefonNumber,
            'Email': email,
            'Skype': skype}

        elif  chooseEmployee==2:
            counter=0
            while True:
                print("Выберите по какому критерию хотите произести поиск")
                print("1- если по фамилии")
                print("2- если по имени")
                print("3- если по отчеству")
                print("4- если по дате рождения")  
                searchValue= input("Введите критерий поиска ")
                if searchValue.isdigit():
                    searchValue=int(searchValue)
                    if 1<=searchValue and searchValue<=4:
                        if searchValue==1:
                            
                            while True:
                                searchSurname = input("Введите фамилию работника ")
                                if re.match(namePattern,searchSurname):
                                    break
                                else:
                                    print("Ошибка ввода!!! Фамилия должна содержать только буквенные значения кирилицы.\nПовторите ввод")
                            for search in employees.keys():
                                if search[0]==searchSurname:  
                                    counter+=1
                                print(employees[search])
                            if counter==0:
                                print("Работник с такой фамилией не найден")

                        if searchValue==2:
                            
                            while True:
                                searchName = input("Введите отчество работника ")
                                if re.match(namePattern,searchName):
                                    break
                                else:
                                    print("Ошибка ввода!!! Имя должно содержать только буквенные значения кирилицы.\nПовторите ввод")
                            for search in employees.keys():
                                if search[1]==searchName:  
                                    counter+=1
                                print(employees[search])
                            if counter==0:
                                print("Работник с таким именем не найден")

                        if searchValue==3:
                            
                            while True:
                                searchMiddleName = input("Введите отчество работника ")
                                if re.match(namePattern,searchMiddleName):
                                    break
                                else:
                                    print("Ошибка ввода!!! Отчество должно содержать только буквенные значения кирилицы.\nПовторите ввод")
                            for search in employees.keys():
                                if search[2]==searchMiddleName:  
                                    counter+=1
                                print(employees[search])
                            if counter==0:
                                print("Работник с таким отчеством не найден")

                        if searchValue==4:
                            
                            while True:
                                searchDateBirth = input("Введите дату рождения работника ")
                                if re.match(dateBirthPattern,searchDateBirth):
                                    break
                                else:
                                    print("Ошибка ввода!!! Дата рождения содержит недопустимые символы.\nПовторите ввод")
                            for search in employees.keys():
                                if search[3]==searchSurname:  
                                    counter+=1
                                print(employees[search])
                            if counter==0:
                                print("Работник с такой датой рождения не найден")

                choiceAction_11=input("Если хочешь продолжить поиск нажми 1, если нет - тогда любую другую клавишу.")
                if choiceAction_11 !='1':
                    print("Поиск закончен")
                    break   
                        
        elif  chooseEmployee==3:
            counter_1==0
            while True:
             searchSurname = input("Введите фамилию работника ")
             if re.match(namePattern,searchSurname):
                break
             else:
              print("Ошибка ввода!!! Фамилия должна содержать только буквенные значения кирилицы.\nПовторите ввод")

            while True:
                searchName= input("Введите имя работника ")
                if re.match(namePattern,searchName):
                    break
                else:
                    print("Ошибка ввода!!! Имя должно содержать только буквенные значения кирилицы.\nПовторите ввод")

            while True:
                searchMiddleName= input("Введите отчество работника ")
                if re.match(namePattern,searchMiddleName):
                    break
                else:
                    print("Ошибка ввода!!! Отчество должно содержать только буквенные значения кирилицы.\nПовторите ввод")

            while True:
                searchdateBirth= input("Введите дату рождения работника как показано в скобках (05.05.1980) ")
                if re.match(dateBirthPattern,searchdateBirth):
                    break
                else:
                    print("Ошибка ввода!!! Отчество должно содержать только буквенные значения кирилицы.\nПовторите ввод")  
            
            delitKey=(searchSurname, searchName, searchMiddleName, searchdateBirth)
            for delKey in employees.keys():
                if delKey==delitKey:
                    del employees[delitKey]
                    counter_1+=1
            if counter_1==0:
                print("Работник с таким данными не найден")

        elif  chooseEmployee==4:
            counter_2=0
            while True:
             searchSurname = input("Введите фамилию работника данные которого хотите заменить ")
             if re.match(namePattern,searchSurname):
                break
             else:
              print("Ошибка ввода!!! Фамилия должна содержать только буквенные значения кирилицы.\nПовторите ввод")

            while True:
                searchName= input("Введите имя работника ")
                if re.match(namePattern,searchName):
                    break
                else:
                    print("Ошибка ввода!!! Имя должно содержать только буквенные значения кирилицы.\nПовторите ввод")

            while True:
                searchMiddleName= input("Введите отчество работника ")
                if re.match(namePattern,searchMiddleName):
                    break
                else:
                    print("Ошибка ввода!!! Отчество должно содержать только буквенные значения кирилицы.\nПовторите ввод")

            while True:
                searchdateBirth= input("Введите дату рождения работника как показано в скобках (05.05.1980) ")
                if re.match(dateBirthPattern,searchdateBirth):
                    break
                else:
                    print("Ошибка ввода!!! Отчество должно содержать только буквенные значения кирилицы.\nПовторите ввод")  
            
            exchangeKey=(searchSurname, searchName, searchMiddleName, searchdateBirth)
            for key in employees.keys():
                if key==exchangeKey:
                    counter_2+=1
                    while True:
                        newjobTitle=input("Введите новую должность работника ")
                        if re.match(namePattern,newjobTitle):
                            break
                        else:
                            print("Ошибка ввода!!! Имя должно содержать только буквенные значения кирилицы.\nПовторите ввод")


                    while True:
                        newtelefonNumber=input("Введите номер телефона работника в международном формате например: +380971234567.\nВведите номер: ")
                        if re.match(phonePattern,newtelefonNumber):
                         break
                        else:
                            print("Ошибка ввода!!! Номер содержит некорректные символы или недостаточноцифр.\nПовторите ввод")

                    while True:
                        newEmail=input("Введите Email-адрес работника ")
                        if re.match(emailPattern,newEmail):
                            break
                        else:
                            print("Ошибка ввода!!! Email-адрес содержит недопустимые символы.\nПовторите ввод")

                    while True:
                        newSkype = input("Введите Skype работника ")
                        if re.match(skypePattern,newSkype):
                            break
                        else:
                            print("Ошибка ввода!!! Skype-адрес содержит недопустимые символы.\nПовторите ввод")
                        
                    employees[exchangeKey]['Должность']=newjobTitle
                    employees[exchangeKey]['Телефон']=newtelefonNumber
                    employees[exchangeKey]['Email']=newEmail
                    employees[exchangeKey]['Skype']=newSkype
            if counter_2==0:
              print("Работник с таким данными не найден")

        elif  chooseEmployee==5:
            print("Список сотрудников")
            for emp, role in employees:
                print(emp, role)

        choiceAction_1=input("Если хочешь продолжить работу со словарем нажми 1, если нет - тогда любую другую клавишу.")
        if choiceAction_1 !='1':
          print("Работа приложения окончена!!! Хорошего дня!!!!")
          break                                   
else:
 print("Програма завершила свою работу")
 