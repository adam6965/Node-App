from hashlib import new
import pandas as pd  
import math
import glob


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Max und Avrage jede Site
all_df = []
for x in glob.glob("LicenseUsageReport*.xlsx"):
    new_df = pd.read_excel(x)
    all_df.append(new_df)

comparedDf = pd.concat(all_df)
comparedDf.shape

df_new = comparedDf.rename(columns={'Total Lic hours': 'maxim'})

maxim_list=[]
for x in df_new.maxim:
  maxim_list.append(int(x))

user_list=[]
for x in df_new.Site:
  user_list.append(x.upper())

user_dic={} #Alle user mit alle Anzahl von ein user
list_end=[] #alle user sind in list ende
#max_dic={} #Maximal anzahl mit User
#durchschnitt_dic={} #avrage Anzahl mit User
max_list=[]
Avrage_list=[]
frame1={}
for x in user_list:
  maxim_list_dic=[] # list för Anzahl von jede User, die einelögin haben.
  max=0
  a=0
  for y in user_list:
    if x==y:
      f=maxim_list[a] # for andis jede user
      maxim_list_dic.append(f) # mit andis anzahl von Userlogin stellen wir maxim_list_dic
    a+=1 # for andis diesele user . weil wir manchmal mehr ein User haben, deswegen macht Python falsh andis finden, deshalb mit das konnen wir richtige andis erhalten.

  list_end.append(x) #alle user sind in list ende
  user_dic[x]=maxim_list_dic # user mit ofen jeden mal
  [int(x) for x in maxim_list_dic]
  #max_dic[x]=max(maxim_list_dic)# user mit max in dic
  #durchschnitt_dic[x]=math.ceil(sum(maxim_list_dic)/len(maxim_list_dic)) # user mit avrage in dic 
  for z in maxim_list_dic:
    if z > max:
      max=z
  max_list.append(max) #user mit max in list
  Avrage_list.append(math.ceil(sum(maxim_list_dic)/len(maxim_list_dic))) # user mit avrage in list


list_last=[] # för entfernt von widerhulunguser
max_list_last=[] # för entfernt von widerhulunguser
Avrage_list_last=[] # för entfernt von widerhulunguser
index=0
for x in list_end:
  if x in list_last:
    continue
  else:
    index = list_end.index(x,index)
    max=max_list[index]
    avrage=Avrage_list[index]
    list_last.append(x)
    max_list_last.append(max) 
    Avrage_list_last.append(avrage) 

frame1["Site"]=list_last
frame1["max"]=max_list_last
frame1["Avrage"]=Avrage_list_last

df1 = pd.DataFrame(frame1) 
print(df1)
df1.to_excel('file_name2.xlsx', index=False)