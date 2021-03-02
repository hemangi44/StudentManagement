from manipulation import Data_manipulation
import matplotlib.pyplot as plt
m  = Data_manipulation()     #creation of object m for class Data_manipulation
#To ensure marks should be in the range 0-100  
def validate_field(num , field_name):
    if num < 0 or num > 100:
        print("Enter ", field_name ," marks in range of 0 to 100")
        return False
    return True
while True:
    op = int(input("1.Insert 2.View Details 3.View Chart 4.Update Details 5.Remove Data 6. Exit\n"))
    if op == 1:
        rno=int(input("Enter Roll no. "))       #input from user
        name=input("Enter Name: ")
        address=input("Enter Address: ")
        print("Enter marks subject-wise ")
        physics=int(input("Enter marks of Physics: "))
        if not validate_field(physics, "Physics"):
            break;
        
        chemistry=int(input("Enter marks of Chemistry: "))
        if not validate_field(chemistry, "Chemistry"):
            break;
        maths=int(input("Enter marks of Mathematics: "))
        if not validate_field(maths, "Maths"):
            break;
        english=int(input("Enter marks of English: "))
        if not validate_field(english, "English"):
            break;
        comp=int(input("Enter marks of Computer Science: "))
        if not validate_field(comp, "Computer Science"):
            break;
        m.add_student(rno,name,address,physics,chemistry,maths,english,comp)

    elif op==2:         #view student data
        data = m.view_students()        #invoking view_student() method of class Data_manipulation
        info = ""
        for d in data:
            per = (d[3]+d[4]+d[5]+d[6]+d[7])/5      #to find out percentage of marks
            info=info+"rno: "+str(d[0])+"  name: "+str(d[1])+"  address :"+str(d[2])+"  Physics :"+str(d[3])+"  Chemistry :"+str(d[4])+" Maths :"+str(d[5])+"  English :"+str(d[6])+"  Comp Science :"+str(d[7])
            info = info + " Percentage: "+str(per)+"%\n"

        print(info)
    elif op==3:                 #to view charts
        data = m.view_students()
        names=[]
        per=[]
        for d in data: 
            names.append(d[1])
            per.append((d[3]+d[4]+d[5]+d[6]+d[7])/5)
        plt.bar(names,per,color='r')
        plt.xlabel("Names")
        plt.ylabel("Percentages")
        plt.title("Percentage Graph")
        plt.grid()
        plt.show()
    elif op==4:             #to update data
        data = m.view_students()
        #fetching all student records in order to check the roll no. exists or not
        r_rno=int(input("Enter roll no. to update: "))
        found=False
        for d in data:    
            if  d[0]==r_rno:
                found=True         
        if not found:
            print("Roll No does not exist")
            break
        else:
            name=input("Enter Name: ")
            address=input("Enter Address: ")
            physics=int(input("Enter Physics marks: "))
            chemistry=int(input("Enter Chemistry marks: "))
            maths=int(input("Enter Mathematics marks: "))
            english=int(input("Enter English marks: "))
            comp=int(input("Enter Computer Science marks: "))
            m.update_student(r_rno,name,address,physics,chemistry,maths,english,comp)
    
    elif op==5:         #to remove student data  
        data = m.view_students()
        r_rno=int(input("Enter roll no. to delete: "))
        found=False
        for d in data:    
            if  d[0]==r_rno:
                found=True         
        if not found:
            print("Roll No does not exist")
            break
        else:
            m.delete_student(r_rno)    #invoking delete method 

    elif op==6:             
        break