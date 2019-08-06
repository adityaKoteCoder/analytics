import re

data = "1001 dbms 20   1002 jd 23 1003 sql 15"
data1 = "Aditya is in 560070 works at Bangalore and krish is in 522612 and works at Guntur"
data2 = "House number 198 and pincode 560070"
data3 = "blue shape red toy green"
data3 = re.sub('(blue|green|red|yellow)','color',data3)
lst = re.split(r"\s+",data)  #\s space
dst = re.findall(r"\d{4}",data) #\d digits
sst = re.findall(r"[A-z]+",data) #character
cst = re.findall(r"at+\s([A-z]+)",data1) #at followed by caps characters (+) 
ip = "192.169.1.255"
#ist =  re.search(r"\s+",data)
kst = re.findall(r'(\d{4})\s([A-z]*)\s+(\d{2})',data)
pst = re.findall(r'\bA[a-z]{5}\s',data1)
print(pst)


import re
data4="ADITYA12@gmail.com kote67@yahoo.com lehan@spaneous.com"
gst = re.findall(r'@([A-z]+).',data4)
print(gst)

gst = re.findall(r'\b([A-z]*[0-9]+)@',data4)
print(gst)

data5 =  "learning_python is fun. python is ,easy"
data5 =re.sub(r"-|,|_"," ",data5)
data5 = re.sub(r"\s+"," ",data5)
print(data5)



