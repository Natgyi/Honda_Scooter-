print("\033[1;32m \n")
print('*'*50,'\n')
print(''' /$$   /$$  /$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$ 
| $$  | $$ /$$__  $$| $$$ | $$| $$__  $$ /$$__  $$
| $$  | $$| $$  \ $$| $$$$| $$| $$  \ $$| $$  \ $$
| $$$$$$$$| $$  | $$| $$ $$ $$| $$  | $$| $$$$$$$$
| $$__  $$| $$  | $$| $$  $$$$| $$  | $$| $$__  $$
| $$  | $$| $$  | $$| $$\  $$$| $$  | $$| $$  | $$
| $$  | $$|  $$$$$$/| $$ \  $$| $$$$$$$/| $$  | $$
|__/  |__/ \______/ |__/  \__/|_______/ |__/  |__/
                                                  ''')
print('*'*50,'\n')
print("\033[96m"+'            [-]For Scooter Only[-]\n '+"\033[0m")
print("\033[1m"+'         [++]Created by Mr Khaing[++]'+"\033[0m")
print("\033[1;33;40m ")
cuntry='Made in region:'
asi='Asia'
use='Type for use:'
tylevel='Type level:'
def convrt(string):
   list1=[]
   list1[:0]=string
   return list1
#iput='MLHJF011-B5000001'
iput=str(input('Enter frame numbers..:'))
cap=iput.upper()

obj=convrt(cap)
def num_element(list):
   count=0 
   for i in list:
      count+=1 
   return count 
ne=num_element(obj)
      
#print('\n')
#print('Your frame numbers are:',cap)
if ne>17:
   print("\033[91m"+'!!! You code numbers are too long..'+"\033[0m")
elif ne<17:
   print("\033[91m"+'!!! Please fill code numbers until to complete\n 17 letters ..'+"\033[0m")
else:
   if obj[0]=='J':
      print(cuntry,asi)
   elif obj[0]=='K':
      print(cuntry,asi)
   elif obj[0]=='L':
      print(cuntry,asi)
   elif obj[0]=='M':
      print(cuntry,asi)
   elif obj[0]=='N':
      print(cuntry,asi)
   elif obj[0]=='P':
      print(cuntry,asi)
   elif obj[0]=='R':
      print(cuntry,asi)
   else:
      print(cuntry+ obj[0] +'is wrong code.')
   if obj[1]=='L':
      print('Type: Motorcycle ')
   else:
       print('Type: Wrong code! ')
   if obj[2]=='H':
      print('Company: Honda')
   else:
      print('Company: '+obj[2]+' is wrong code!')
   
   
   if obj[4]=='A':
      print(use,'Business Type')
   
   elif obj[4]=='B':
      print(use,'Family or leisure type.')
   elif obj[4]=='C':
      print(use,'On road type.')
   elif obj[4]=='D':
      print(use,'On off road type.')
   elif obj[4]=='E':
      print(use,'Off road type.')
   elif obj[4]=='F':
      print(use,'Scooter type.')
   elif obj[4]=='G':
      print(use,'Purpose type.')
   elif obj[4]=='H':
      print(use,'Special type.')
   elif obj[4]=='I':
      print(use,'Special type.')
   else:
      print('Power: '+obj[4]+' is wrong code!')
      
   if obj[6]=='1':
      print('DVL: Develop level 1')
   elif obj[6]=='2':
      print('DVL: Develop level 2')
   elif obj[6]=='3':
      print('DVL: Develop level 3')
   else:
      print('DVL:' +obj[6]+ 'is wrong code!')
      
   if obj[7]=='0':
      print('Type for country: Thailand ')
   elif obj[7]=='1':
      
      print(tylevel+' 1')
   elif obj[7]=='2':
      print(tylevel+' 2')
   elif obj[7]=='3':
      
      print(tylevel+' 3')
   elif obj[7]=='4':
      print(tylevel+' 4 ')
   elif obj[7]=='8':
      print(tylevel+' 8')
   elif obj[7]=='S':
      
      print(tylevel+' Test')
   else:
      print(tylevel+' Not found..')
   
   if obj[9]=='1':
      print('Model year: 2001')
   
   elif obj[9]=='2':
      print('Model year: 2002')
   elif obj[9]=='3':
      print('Model year: 2003')
   elif obj[9]=='4':
      print('Model year: 2004')
   elif obj[9]=='5':
      print('Model year: 2005')
   elif obj[9]=='6':
      print('Model year: 2006')
   elif obj[9]=='7':
      print('Model year: 2007')
   elif obj[9]=='8':
      print('Model year: 2008')
   elif obj[9]=='9':
      print('Model year: 2009')
   elif obj[9]=='A':
      print('Model year: 2010')
   elif obj[9]=='B':
      print('Model year: 2011')
   elif obj[9]=='C':
      print('Model year: 2012')
   elif obj[9]=='D':
      print('Model year: 2013')
   elif obj[9]=='E':
      print('Model year: 2014')
   elif obj[9]=='F':
      print('Model year: 2015')
   elif obj[9]=='G':
      print('Model year: 2016')
   elif obj[9]=='H':
      print('Model year: 2017')
   elif obj[9]=='J':
      print('Model year: 2018')
   elif obj[9]=='K':
      print('Model year: 2019')
   elif obj[9]=='L':
      print('Model year: 2020')
   elif obj[9]=='M':
      print('Model year: 2021')
   elif obj[9]=='N':
      print('Model year: 2022')
   elif obj[9]=='P':
      print('Model year: 2023')
   elif obj[9]=='R':
      print('Model year: 2024')
   elif obj[9]=='S':
      print('Model year: 2025')
   elif obj[9]=='T':
      print('Model year: 2026')
   elif obj[9]=='V':
      print('Model year: 2027')
   elif obj[9]=='W':
      print('Model year: 2028')
   elif obj[9]=='X':
      print('Model year: 2029')
   elif obj[9]=='Y':
      print('Model year: 2030')
   
   else:
      print('Model year:' +obj[9]+ 'is wrong code!')
   
   if obj[10]==5:
      print('Factory number: 5')
      
   ls=obj[11:17]
   def lstring(ls):
      str1=''
      for ele in ls:
         str1+=ele
      return str1
   
   print('Serial numbers are: '+lstring(ls))
   #Created date (24.3.2022)