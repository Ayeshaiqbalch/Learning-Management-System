def len(para):
	countw=0
	for e in para:
		countw+=1
	return countw	
def password(psw,stdNamesList):
	list =[]
	Counter =0
	while Counter != len(stdNamesList):
		if stdNamesList[Counter]!=0:
			list = list+[str(stdNamesList[Counter][-3])+str(stdNamesList[Counter][-2])+str(stdNamesList[Counter][-1])]
			Counter+=1
		else:
			Counter+=1
	if psw in list:
		return True;
	else:
		return False;
def theCoursesofaStudent(stdNamesList,stdRegNoList,CourseList,Course_Code,Course_Name,Credit_Hours,Semester,rgn):
	inx=stdRegNoList.index(rgn)
	cont=0
	print('Course Code	Credit Hours	Semester	Course Name')
	while cont< len(CourseList[inx]):
		if CourseList[inx][cont] == 0:
			cont+=1
		else:
			if CourseList[inx][cont] in Course_Code:
				xedni=Course_Code.index(CourseList[inx][cont])
				print(CourseList[inx][cont],'		',Credit_Hours[xedni],'		',Semester[xedni],'		',Course_Name[xedni])
			cont+=1
def registerCourse(stdNamesList,stdRegNoList,CourseList,Course_Code,reg_no,courseCode):
	if reg_no in stdRegNoList:
		Ind = stdRegNoList.index(reg_no)
		if courseCode in Course_Code:
			CounterA = 0
			while CounterA < len(CourseList[Ind]):
				if CourseList[Ind][CounterA]!=0:
					CounterA+=1
				else:
					CourseList[Ind][CounterA]=courseCode
					break
				print("Course has been registered successfully.")
		else:
			print('Invalid Course Code.')	
	else:
		print("Invalid Registration Number.")
def deleteStd(stdNamesList,stdRegNoList,CourseList,Regi_no):
	if Regi_no in stdRegNoList:
		ind1 = stdRegNoList.index(Regi_no)
		stdNamesList[ind1]=0
		stdRegNoList[ind1]=0
		CounterC=0
		while CounterC < len(CourseList[ind1]):
			if CourseList[ind1][CounterC] != 0:
				CourseList[ind1][CounterC] = 0
			CounterC+=1
		print('Student has been deleted successfully.')
	else:
		print('Invalid Registration number.')
def viewallStudent(stdNamesList,stdRegNoList):
	 print('Registration Number	Name')
	 print('#############################################')
	 a1 = 0
	 while a1 < len(stdNamesList):
			 if	 ((stdNamesList[a1] != 0) and (stdRegNoList[a1] != 0)): 
				 print(stdRegNoList[a1],'		',stdNamesList[a1])
			 a1 = a1 + 1
def unregisterCourse(stdRegNoList,CourseList,Reg_no,CourseCode):
	if Reg_no in stdRegNoList:
		IND = stdRegNoList.index(Reg_no)
		if CourseCode in  CourseList[IND]:
			INDX = CourseList[IND].index(CourseCode)
			CourseList[IND][INDX]=0
			print('Course has been unregistered Successfully.')
		else:
			print("Invalid Course code.")
	else:
		print("Invalid Registration Number.")
def saveStd(stdNamesList,stdRegNoList,CourseList):
	import os	
	global line
	filePath = 'Students.txt'
	if os.path.exists(filePath):
		file  = open(filePath, "w")
		a2 = 0
		while a2 < len(stdNamesList):
			if stdNamesList[a2] != 0:
				line = str(stdRegNoList[a2])+','+str(stdNamesList[a2])
				file.write(line)
				file.write('\n')
				a4 = 0
				while a4 < len(CourseList[a2]):
					if CourseList[a2][a4] != 0:
						file.write(str(CourseList[a2][a4]))
						file.write(',')
					a4+=1
				file.write('\n')
			a2 = a2 + 1		
		file.close()
	else:
		print("The file does not exist")
def LoadStd(stdNamesList,stdRegNoList,CourseList):
	import os
	if os.path.exists('C:\\Users\\Aneeq ch\\Documents\\python\\Students.txt') :		
		file = open('Students.txt')
		count = 0
		count1=0
		for line in file:
			if count%2==0:
				templist=splitlist(line.replace("\n",""))
				ncounter = 0
				while ncounter < len(stdNamesList):
					if stdNamesList[ncounter] != 0:
						ncounter+=1
					else:
						stdRegNoList[ncounter]=templist[0]
						stdNamesList[ncounter]=templist[1]
						break
			count+=1
			if count1%2==1:
				templist=splitlist(line.replace("\n",""))
				if templist != []:
					bcounter=0
					while bcounter< len(templist):
						scounter=0
						while scounter < len(CourseList):
							acounter = 0
							while acounter<len(CourseList[scounter+1]):
								if CourseList[scounter+1][acounter] !=0:
									acounter+=1
								else:
									CourseList[scounter+1][acounter]=templist[bcounter]									
									break
							break
						bcounter+=1
			count1 += 1
		file.close()
	else:
		print("The file does not exist or it empty")
def updateStudent(stdNamesList,stdRegNoList,nd1,nd2,rg):
	if rg in stdRegNoList:
		ind = stdRegNoList.index(rg)
		if RegNo(nd1) == True:
			stdRegNoList[ind]=nd1
			if studentname(nd2) == True:
				stdNamesList[ind] = nd2
				print('Student has been added successfully')
			else:
				print('New Name is invalid.')
		else:
			print('New registration num is invalid.')
	else:
		print('This is not present in registration list')
def addStudent(stdNamesList,stdRegNoList,sr,sn):
	if RegNo(sr) == True:
		if studentname(sn) == True:
			scounter=0
			while scounter < len(stdNamesList):
				if stdNamesList[scounter] != 0:
					scounter+=1
				else:
					stdNamesList[scounter]=sn
					stdRegNoList[scounter]=sr
					break
				print('Student has been added successfully.')
		else:
			print("Student Name is invalid.")
	else:
		print("Registration number is invalid.")
def RegNo(reg):
	if len(reg) == 11:
		if (reg[0]=='2') and (reg[1]=='0') and (reg[2]=='1') and (reg[3]>='0' and reg[3]<='9') and (reg[4] == '-') and (reg[5]>='C') and (reg[6]=='E' or reg[6]=='S') and (reg[7] == '-' )and (reg[8]>='0' and reg[8]<='9') and (reg[9]>='0' and reg[9]<='9') and (reg[10]>='0' and reg[10]<='9'):
			return True;
		else:
			return False;
	else:
		print('Please enter a valid registration number.')
def studentname(name):
		 j = 0
		 booleanResult = True
		 while	 j < len(name):
				 if ((name[j]>='A' and name[j]<='Z') or (name[j]>='a' and name[j]<='z') or (name[j] == ' ')):					 
					 booleanResult = booleanResult and True					 
					 j = j + 1
				 else:					 
					 booleanResult = booleanResult and False					
					 j = j + 1
		 return booleanResult;
def splitlist(sentence):
	list5 = []
	tmp = ''
	for c in sentence:
		if c == ',' :
		#list1.append(tmp)
			list5 = list5 + [tmp]
			tmp = ''
		
		else:
			#if c == '\n':
			tmp += c
	if tmp:
		list5 = list5 + [tmp]
	

	return list5;
def	 coursecode(c):
	 if len(c) == 5:
		 if( (c[0]>='A' and c[0]<='Z') and	(c[1]>='A' and c[1]<='Z') and (c[2]>='0' and c[2]<='9') and (c[3]>='0' and c[3]<='9') and (c[4]>='0' and c[4]<='9')):
			 return True;
	
		 else:
			 return False;
	 else:
		 print('Please enter only five characters.')
def	 coursename(d):
	 if	 len(d) <= 50:
		 j = 0
		 booleanResult = True
		 while	 j < len(d):
				 if ((d[j]>='A' and d[j]<='Z') or (d[j]>='a' and d[j]<='z') or (d[j] == ' ')):					 
					 booleanResult = booleanResult and True					 
					 j = j + 1
				 else:					 
					 booleanResult = booleanResult and False					
					 j = j + 1			   
	 else:
		 print("Please write only 50 character")
	 return booleanResult;	 
def	 credithours(e):
	 if	 (e >= '1' and e <= '3'):
		 return True;
	 else:
		 return False;
def	 semester(f):
	 if	 (f >= '1' and f <= '8'):
		 return True;
	 else:
		 return False;
def	 addcourse(Course_Code,Course_Name,Credit_Hours,Semester,cc,cn,ch,cs):			 
			 if	 coursecode(cc) == True:
				 if	 coursename(cn) == True:				
					 if	credithours(ch)== True:			  
						 if	semester(cs) == True:
							 counter = 0
							 while counter < len(Course_Code):
								 if Course_Code[counter] != 0:
									 counter+=1
								 else:
									 Course_Code[counter]=cc
									 Course_Name[counter]=cn
									 Credit_Hours[counter]=ch
									 Semester[counter]=cs
									 break 
							 print(Course_Code)
							 print('Course has been added successfully.')
						 else:
							 print('This Semester is invalid')
							 print('\n')
					 else:
						 print('Credit Hours are invalid')
						 print('\n')
				 else:
					 print('Course name is invalid')
					 print('\n')
			 else:
				  print('Course code is invalid');
				  print('Please enter a valid course')
				  print('\n')			 
def	 deletethecorse(Course_Code,Course_Name,Credit_Hours,Semester,dc): 
	 if	 dc in Course_Code:
		 w = Course_Code.index(dc)
		 Course_Code[w] = 0
		 Course_Name[w] = 0
		 Credit_Hours[w] = 0
		 Semester[w] = 0
		 print(Course_Code)
		 print('Course has been deleted successfully')	
	 else:			
		 print('Please enter a valid course.')
		 print('\n')		 
def	 viewallthecourses(Course_Code,Course_Name,Credit_Hours,Semester):
	 print('We are in  View all course for	option 4')
	 print('Course Code	Semester	Credit Hours	Course Name')
	 a1 = 0
	 while a1 < len(Course_Code):
			 if	 ((Course_Code[a1] != 0) and (Course_Name[a1] != 0) and (Credit_Hours[a1] != 0)	and (Semester[a1] != 0)): 
				 print(Course_Code[a1],'		',Semester[a1],'		',Credit_Hours[a1],'		',Course_Name[a1])
			 a1 = a1 + 1
def	 viewthecoursesofasemester(Course_Code,Course_Name,Credit_Hours,Semester,b1):
	 a3 = 0
	 print('Course Code	 Credit Hours	Course Name')					 
	 while a3 < len(Course_Code):
		 if	 ((Course_Code[a3] != 0) and (Course_Name[a3] != 0) and (Credit_Hours[a3] != 0)	and (Semester[a3] != 0)):
			 if int(Semester[a3]) == b1:
				 print('-----------------------------------------------------')
				 print(Course_Code[a3],'		',Credit_Hours[a3],'		',Course_Name[a3])
		 a3 = a3 + 1
def	 updatethecourse(Course_Code,Course_Name,Credit_Hours,Semester,s1,s,v,p,n):
			 if n in Course_Code:
				 o = Course_Code.index(n)
				 if coursecode(s1) == True:
					 Course_Code[o] = s1
					 if credithours(s) == True:
						 Credit_Hours[o] = s
						 if semester(v) == True:
							 Semester[o]=v
							 if coursename(p) == True:
								 Course_Name[o]=p
								 print('Course has been edited successfully')
							 else:
								 print('Invalid Course Name')
						 else:
							 print('Invalid Semester')
					 else:
						 print('invalid Credit Hours')
				 else:
					 print('Invalid Course Code ')
			 else:
				 print('Invalid Course Code which is not present in list')
def loadCourse(Course_Code,Course_Name,Credit_Hours,Semester):
	import os
	if os.path.exists('C:\\Users\\Aneeq ch\\Documents\\python\\Courses.txt') and os.path.getsize('C:\\Users\\Aneeq ch\\Documents\\python\\Courses.txt') > 0:		
		file = open('Courses.txt')
		for line in file:			
			templist = splitlist(line.replace("\n",""))
			ncounter = 0
			while ncounter < len(Course_Code):
				 if Course_Code[ncounter] != 0:
					 ncounter+=1
				 else:
					 Course_Code[ncounter]=templist[0]
					 Course_Name[ncounter]=templist[1]
					 Credit_Hours[ncounter]=templist[2]
					 Semester[ncounter]=templist[3]
					 break			
		file.close()
	else:
		print("The file does not exist or it empty")
def SaveCourse(Course_Code,Course_Name,Credit_Hours,Semester):
	import os	
	global line
	filePath = 'Courses.txt'
	if os.path.exists(filePath):
		file  = open(filePath, "w")
		a2 = 0
		while a2 < len(Course_Code):
			if Course_Code[a2] != 0:
				line = str(Course_Code[a2])+','+str(Course_Name[a2])+','+str(Credit_Hours[a2])+','+str(Semester[a2])
				file.write(line)
				file.write('\n')
			a2 = a2 + 1		
		file.close()
	else:
		print("The file does not exist")
def loaduser(userlist,passwordsList):
	import os
	
	B = input("Username = ")
	C = input("Password = ")
	#if os.path.exists('C:\\Users\\Aneeq ch\\Documents\\python\\test.txt'):
	if os.path.exists('ze.txt'): 
	#print("The file exist")
		file = open('ze.txt')
		booleanResult = True
		for line in file:
			templist = splitlist(line.replace("\n",""))
			userlist = userlist + [templist[0]]
			passwordsList = passwordsList + [templist[1]]
			
		if (B in userlist ) and (C in passwordsList ):
			booleanResult = booleanResult and  True
		else :
			booleanResult = booleanResult and False
		return booleanResult;
		file.close()
	else:
		print("Sorry, we are unable to run the program, as user data does not exist.")
def main():
	Course_Code = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
	Course_Name = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
	Semester = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
	Credit_Hours = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
	stdNamesList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	stdRegNoList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	CourseList=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
	LoadStd(stdNamesList,stdRegNoList,CourseList)
	loadCourse(Course_Code,Course_Name,Credit_Hours,Semester)
	i = 0
	while	 i!=13:
		 print('Choose the following option')
		 print('1	  Add Course')
		 print('2	  Update Course')
		 print('3	  Delete Course')
		 print('4	  View all Courses')
		 print('5	  View Courses of a Smester')
		 print('6	  Add New Students')
		 print('7	  Edit Student')
		 print('8	  Delete Student ')
		 print('9	  View all student')
		 print('10	  Register the course for student')
		 print('11	  Unregister the course for student')
		 print('12	  logout')
		 print('13	  Exit Program')
		 print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		 
		 i =int(input('please Choose only the above option :'))
		 print('------------------------------------------------------------------------------------------------------------------------')
		 if	 i == 1:
			 print('				Code Hours Smester Name')
			 A = input('Enter the details of the course:')
			 input1 = A[0:5]
			 input2 = A[10:60]
			 input3 = A[6]
			 input4 = A[8]
			 addcourse(Course_Code,Course_Name,Credit_Hours,Semester,input1,input2,input3,input4)
			 print('Test = ');
			 print(Course_Code)
			 print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		 if	 i == 2:
			 n = input("Enter the Course code  which you want to edit	:")
			 print('			Code Hours Smester Name')
			 B = input("Enter the New details	:")
			 updatethecourse(Course_Code,Course_Name,Credit_Hours,Semester,B[0:5],B[6],B[8],B[10:60],n)
			 print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		 if	 i == 3:
			 inputdel = input("Enter the course code to delete:")
			 deletethecorse(Course_Code,Course_Name,Credit_Hours,Semester,inputdel)
			 print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		 if	 i == 4:
			 viewallthecourses(Course_Code,Course_Name,Credit_Hours,Semester)
			 print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++') 
		 if	 i == 5:
			 b1 = int(input("Enter the Semester for which you want to view the courses :"))
			 viewthecoursesofasemester(Course_Code,Course_Name,Credit_Hours,Semester,b1)
			 print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		 if	 i == 6:
			 print('				Reg.No	Name')
			 AS=input("Enter the details of student :")
			 addStudent(stdNamesList,stdRegNoList,AS[0:11],AS[12:60])
			 print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		 if	 i == 7:
			 rg = input('Enter the Registration number of the student to edit : ')
			 print('				Reg.no Name')
			 UP = input('Enter the New details of student : ')
			 updateStudent(stdNamesList,stdRegNoList,UP[0:11],UP[12:60],rg)
			 print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		 if	 i == 8:
			 Regi_no = input("Enter Registration number")
			 deleteStd(stdNamesList,stdRegNoList,CourseList,Regi_no)
			 print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		 if	 i == 9:
			 viewallStudent(stdNamesList,stdRegNoList)
			 print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		 if	 i == 10:
			 reg_no = input("Enter registration Number of the student for course registration:")
			 courseCode = input('Enter the Course Code to Register:')
			 registerCourse(stdNamesList,stdRegNoList,CourseList,Course_Code,reg_no,courseCode)
			 print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		 if	 i == 11:
			 Reg_no = input("Enter registeration number : ")
			 CourseCode = input("Enter Course code to unregister:")
			 unregisterCourse(stdRegNoList,CourseList,Reg_no,CourseCode)
			 print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		 if	 i == 12:
			 admin()
		 if	 i == 13:
			 SaveCourse(Course_Code,Course_Name,Credit_Hours,Semester)
			 saveStd(stdNamesList,stdRegNoList,CourseList)
		 print('Thank You!')
def admin():
	print('**	 Welcome to University Learning Management System	 **')
	print('Dear User, current software is intended for authorized users only. Login to the system to get access.')
	print('\n')
	userlist = []
	passwordsList = []
	if loaduser(userlist,passwordsList) == True :
		main()
	else :
		print('Dear User, Username/password is incorrect.','\n','Enter the username/password again to get access to the system')
		admin()
def std():
	rgn=input('Enter Registration number:')
	psw=input("Enter password:")
	Course_Code = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
	Course_Name = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
	Semester = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
	Credit_Hours = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
	stdNamesList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	stdRegNoList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	CourseList=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
	LoadStd(stdNamesList,stdRegNoList,CourseList)
	loadCourse(Course_Code,Course_Name,Credit_Hours,Semester)
	if rgn in stdRegNoList and  password(psw,stdNamesList) == True:
		wq = 0
		while wq !=3:
			print('Enter 1 to view registered course')
			print('Enter 2 to logout of the system')
			print('Enter 3 to exit')
			wq = int(input('Choose option'))
			if wq == 1:
				
				theCoursesofaStudent(stdNamesList,stdRegNoList,CourseList,Course_Code,Course_Name,Credit_Hours,Semester,rgn)
			if wq == 2:
				final()
def final():
	j = 0
	while j < 3:
		print('Choose the option for Login')
		print("1 for Admin")
		print('2 for student')
		j = int(input("Enter option:"))
		if j==1:
			admin()
		if j==2:
			std()
final()

