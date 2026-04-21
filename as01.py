marks=[]

grades=[12,13]

classes=['grade 12A1','grade 12A2','grade12A3',
         'grade 13A1','grade 13A2','grade13A3'
        ]

grade=int(input('what is your grade ? '))
print(grade)

if grade in grades:
    print("you are in our data system,let's continue")
    clas=str(input("what is your class ? ")) 
    
    if clas in classes:
        print("valid class")
        
        number_of_students=int(input("enter the number of students"))
        print(number_of_students)
      
        
        
        for i in range(number_of_students):
            mark=int(input("enter the marks "))
            if 0 < mark <= 100 :
                 marks.append(mark)
                 if mark < 40:
                     print("Fail")
                 else:
                     print("Pass")                                     
            else:
                print("invalid mark")
                
        total=sum(marks)
        print("total is ",total)
        average= total / len(marks)
        print('Average is ',average)
        highest_marks=max(marks)
        print("Highest mark is ",highest_marks)
        lowest_marks=min(marks)
        print("lowest mark is ",lowest_marks)                              
                
    else:
        print('invalid class')
else:
    print("sorry you are not in our data system")
    

        