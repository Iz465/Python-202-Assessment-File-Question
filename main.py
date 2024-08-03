import os 

def student_info(student):
  removed_newline = [newline.strip() for newline in student] # Removed newline is a new list which will hold the student lists without the spaces or new lines. This is required for the email to prevent spaces after index 1 and 2.
  with open('student_record_v2.txt','a') as file: # 'a' means you can append the file.
    if os.stat('student_record_v2.txt').st_size < 511: # 511 is how much space the reformatted student data takes in the file. This stops the info repeating in the file.
      file.write(f"ID: {removed_newline[0]}First Name: {student[1]}Last Name: {student[2]}Campus: {student[3]}Study: {student[4]}Email:{removed_newline[1]}_{removed_newline[2]}@yoobeecolleges.com \n\n")
  
 
with open('student_record_v1.txt','r') as file: # 'r' means it will only read the files and not modify them
  lines = file.readlines()

student1 = [] # Each list will hold the info of each student
student2 = []
student3 = []
student4 = []
student5 = []
line_count = 0
for line in lines: 
  line_count += 1
  match line_count: # Works like switch statement
    case 1: student1.append(line) # Will add the info from the text file to the specific list
    case 2: student2.append(line)
    case 3: student3.append(line)
    case 4: student4.append(line)
    case 5: student5.append(line)
  if line_count >= 5:
    line_count = 0
print()
student_info(student1)
student_info(student2)
student_info(student3)
student_info(student4)
student_info(student5)



  
  
   
   
   
   
   
   
