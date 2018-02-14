with open("Project2_25Nodes_5Pause.tr","r") as f:
	f1=f.read()
	s1=f1.strip()
	#print(s1)
	s2=s1.split("()")
l=[]
for item in s2:
	l.append(item.strip())
#print("l",l)
p=[]
for k in l:
	if k.find("Payload")!=-1:
		p.append(k)
#print("PAYLOAD************",p)

transmit=[]
receive=[]
for item in p:
	if item.startswith("t"):
		transmit.append(item)
	elif item.startswith("r"):
		receive.append(item)
#print("TRANSMIT***********************",transmit)
#print("RECEIVE*************************",receive)
new=[]
new1=[]
for i in transmit:
	new.append(i.split(" "))
print("*************************NEW**********",new)

for j in receive:
	new1.append(j.split(" "))
print("************************NEW1**********",new1)

'''for i in (new):
	for j in range(len(i)):
		print(new([j][1]))'''

f=[item[1] for item in new]

f1=[item[1] for item in new1 if (len(item)!=0)]

print("SUM of TRANSMISSION TIMES",sum(map(float,f)))
print("SUM of RECEIVING TIMES",sum(map(float,f1)))
print("DIFFERENCE BETWEEN RECEIVING TIMES AND TRANSMITTING TIMES",sum(map(float,f1))-sum(map(float,f)))
