import threading
import csv
import os
import re

class Spravochnik:
   
    fileName=""
    def __init__(self, fileName="Spravochnic.csv"):

        self.fileName= fileName
        self.lock=threading.Lock()

        try:
           if not os.path.exists(self.fileName):
              with open(self.fileName,'w',newline='', encoding='utf-8' ) as f:
                 writer= csv.writer(f)
                 writer.writerow(['Название компании', 'Фамилия директора','Адрес','Номер телефона','Вид деятельности'])
              

        except IOError as e :
          print(f"Ошибка при создании файла: {e}")

    def addRecord(self, companyName, ownerName, address, telefonNumber, activity):
       try:
          with self.lock:
             with open(self.fileName, 'a', newline='', encoding='utf-8') as f:
                writer= csv.writer(f)
                writer.writerow([companyName, ownerName, address, telefonNumber, activity])
       except IOError as e:
            print(f"Ошибка при добавлении записи: {e}")

    def showAll(self):
       try:
          with self.lock:
             with open(self.fileName, 'r', newline='', encoding='utf-8') as f:
                reader=csv.reader(f)
                records=list(reader)
             return records
       
       except IOError as e:
          print(f"Ошибка при чтении файла: {e}")
          return []
       
    def search(self, query):
       query=query.lower()
       results=[]
       try:
          with self.lock:
             with open(self.fileName,'r',newline='', encoding='utf-8') as f:
                reader= csv.DictReader(f)
                for row in reader:
                   if (query in row['Название компании'].lower() or
                       query in row['Фамилия директора'].lower() or
                       query in row['Адрес'].lower() or
                       query in row['Номер телефона'].lower() or
                       query in row['Вид деятельности'].lower()):
                      
                      results.append(row)
       except IOError as e:
            print(f"Ошибка при поиске: {e}")

       return results

       
def main():
   
       spravochnik = Spravochnik()
       choise_1=''
       companyPattern = r"^[A-Za-zА-Яа-яЁё0-9 .,]+(-\d+)?$"
       ownerPattern = r"^[A-Za-zА-Яа-яЁё]+(-[A-Za-zА-Яа-яЁё]+)?$"
       addressPattern = r"^[A-Za-zА-Яа-яЁё0-9 ,.\-]+$"
       phonePattern = r"^\+380\d{9}$"

       while True:
          print("Если хочеш посмотреть все записи набери 1," \
                "\nесли хочеш добавить запись набери 2," \
                "\nесли хочеш провести поиск нажми 3," \
                "\n если хочешь завершить работу нажми 4.")
          while True:
            choise_1= input("Сделай свой выбор ")
            try:
               choise_1= int(choise_1)
               if choise_1>=1 or choise_1<=3:
                break
               else:
                print("Ошибка!!! Число выбора может находится в интервале от 1 до 3, включительно.\nБудьте внимательны и повторите ввод.")
                
            except ValueError:
               print("Ошибка!!! Вы ввели не число. Будте внимательны и посторите ввод")
               
          if choise_1==1:
             print('Все записи:')
             for r in spravochnik.showAll():
               print(r)

          elif choise_1 == 2:
                while True: 
                 companyName= input("Введите название компании ")
                 if not re.match(companyPattern,companyName):
                    print("Ошибка!!! НАзвание содержит некорректные символы. Повторите ввод.")
                    continue
                 break
                
                while True:
                 ownerName=input("Введите фамилию собственника ")
                 if not re.match(ownerPattern, ownerName):
                    print("Ошибка ввода!!! Фамилия содержит некорректные символы. Повторите ввод.")
                    continue
                 break
                
                while True:   
                 address=input("Введите адрес компании как указано в скобках(Одесса, ул.Пушкинская, д.12) ")
                 if not re.match(addressPattern,address):
                    print("Ошибка ввода!!! Адрес содержит некорректные значения. Повторите ввод.")
                    continue
                 break
                while True:
                 telefonNumber= input("Введите номер телефона в (формате +380999219322) ")
                 if not re.match(phonePattern, telefonNumber):
                    print("Ошибка ввода!!! Вы ввели некорректный номер телефона. Повторите ввод.")
                    continue
                 break
                while True: 
                  activity= input("Введите вид деятельности ")
                  if not re.match(ownerPattern, activity):
                     continue
                  break
                spravochnik.addRecord(companyName, ownerName,address, telefonNumber, activity)
                print(f"Запись о компании {companyName} успешно внесена в список.")
  
          elif choise_1 == 3:
                keyWord= input("Введи ключевое слово для поиска ")
                spravochnik.search(keyWord)
   
                
          elif choise_1==4:
             print("Работа завершена.")
             break
            
if __name__ == '__main__':    
   main()    
             
          


          
    
    
    

    







    

   