import re
AllNodes = [i for i in range(50)]
s='10.1.1.'
c=[]
p=[]
b=[]
transmit=[]
receive=[]
Delay_Max = 0
Delay_Total = 0
matchl=[]
matchrec=[]
count=0

for i in range(1,51):
    b.append(s+str(i))

d=dict(zip(b,AllNodes))
print(d)
with open("IP_Trace.tr","r") as f:
	f1=f.read()
	s1=f1.strip()
	#print(s1)
	s2=s1.split("\n")


for k in s2:
	if k.find("Payload")!=-1:
		p.append(k)
#print("PAYLOAD************",p)


for item in p:
	if item.startswith("t"):
		transmit.append(item)
	elif item.startswith("r"):
		receive.append(item)
#print("TRANSMIT***********************",transmit)
#print("RECEIVE*************************",receive)
#print(len(transmit))
#print(len(receive))

for a in transmit:
	if ("/Tx(1)" in a):
		match=re.search(r'10.1.1.\d{1,2} > 10.1.1.\d{1,2}',a)
		#match1=re.search(r'SequenceNumber: \d{1,2}',a)
		match2=re.search(r'id \d{1,}', a)
		#match3=re.search(r'/\w*?\((\d)\)',a)
		'''if "/Tx(0)" in a:	
		print(a)'''	
		#print(match3.group(0))
        	#print(match1,match,match2)
		#print(a.find("/Tx(0)"))

		if match and match2:		
			matchl.append(a)
		#print(ct)
		#print(matchl)	
			Transmission_Time = re.findall(r't(.*?)/',a)
			
			#print(ct)
			#print(Transmission_Time[0])
        		IP = match.group(0).split('>')
        		sourceIP = IP[0].strip()
			'''if sourceIP:
				ct+=1	
			print(sourceIP)'''
			#print(ct)
        		string = "/NodeList/" + str(d[sourceIP])
			'''if string:
				ct+=1	'''
			#print(string)
                	#print(IP,sourceIP)
			#print(ct)
        		if string in a: 
            			destinationIP = IP[1].strip()
            			#seqNumber = match1.group(0).split(': ')
            			#seqNumber = seqNumber[1]
            			src_id = match2.group(0).split(' ')
            			src_id = src_id[1]
                        	#print(IP,sourceIP,destinationIP,src_id)

            			for recv in receive:
					#print(len(recv))
					if ("/Rx(1)" in recv):
               					string = "/NodeList/" + str(d[destinationIP])
                				if string in recv:
                    					match = re.search(r'10.1.1.\d{1,2} > 10.1.1.\d{1,2}', recv)
                    					#match1 = re.search(r'SeqNumber=\d{1,2}',recv)
                    					match2 = re.search(r'id \d{1,}',recv)
                                        		#print(match,match2)
					
                    					if match and match2:
								'''matchrec.append(recv)
								ct+=1
							print(matchrec)
							print(ct)'''
                        					Receiving_Time = re.findall(r'r(.*?)/',recv)
								#print(Receiving_Time[0])
                        					IP = match.group(0).split('>')
                        					rcv_sourceIP = IP[0].strip()
                        					rcv_destIP = IP[1].strip()
                        					#rcv_seqnum = match1.group(0).split('=')
                        					#rcv_seqnum = rcv_seqnum[1]
                        					des_id = match2.group(0).split(' ')
                        					des_id = des_id[1]
                                                		#print(IP,rcv_sourceIP,rcv_destIP,des_id)
					
                        					if sourceIP == rcv_sourceIP and destinationIP == rcv_destIP and src_id == des_id:
									count+=1
									print(count)
                            						if float(Transmission_Time[0]) < float(Receiving_Time[0]):
										
										#print(count)
                                                        			#print(Transmission_Time[0],Receiving_Time[0])
                                						delay = float(Receiving_Time[0]) - float(Transmission_Time[0])
										c.append(delay)
         									#print(c)
                                						Delay_Total = Delay_Total + delay
										#print("TOTAL DELAY",Delay_Total)
									
                                						#PacketsTransmitted_Total +=1
										
 										#print(PacketsTransmitted_Total)
                               	 						if Delay_Max < delay:
											#count+=1
                                    							Delay_Max = delay
                                						
										receive.remove(recv)
										#print(recv)
                                						break
										#print(Delay_Max)
										#print(count) 
        			
		else: break   					

#print(PacketsTransmitted_Total)
Delay_Average = Delay_Total / count
print(Delay_Average)
#printing the values of average and maximum delay
print('The average delay is {}'.format(Delay_Average))
print('The maximum delay is {}'.format(Delay_Max))
print('The Total delay is {}'.format(Delay_Total))

'''
new=[]
new1=[]
for i in transmit:
	new.append(i.split(" "))
print("*************************NEW**********",new)

for j in receive:
	new1.append(j.split(" "))
print("************************NEW1**********",new1)

for i in (new):
	for j in range(len(i)):
		print(new([j][1]))

f=[item[1] for item in new]

f1=[item[1] for item in new1 if (len(item)!=0)]

print("SUM of TRANSMISSION TIMES",sum(map(float,f)))
print("SUM of RECEIVING TIMES",sum(map(float,f1)))
print("DIFFERENCE BETWEEN RECEIVING TIMES AND TRANSMITTING TIMES",sum(map(float,f1))-sum(map(float,f)))'''
