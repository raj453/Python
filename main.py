import os

class record:
    def __init__(self,id,book_name,author,student_name,date):
        self.id=id
        self.book_name=book_name
        self.author=author
        self.student_name=student_name
        self.date=date

    def Add_record(self):
        list=[self.book_name,self.author,self.student_name,self.date]
        dic={self.id:list}

        f=open("StdentDB.txt","a+")
        f.write("\n")
        f.write(str(dic))
        f.close()

    def Search(self,r):
        f=open("StdentDB.txt","r+")
        for line in f:
            if r in line:
                print("\nResult: \n"+line)


                if line[0:1]=="{" and line[-2:-1]=="}":
                    print("ID of Book: ",r)
                    if "[" in line:


                        start=line.index("[")
                        end = line.index("}")
                        co=0
                        for i in range(start,end+1):
                            if line[i:i+1] ==",":
                                st = line[start + 1:i]
                                co=co+1
                                if co==1:
                                    print("Book Name: "+st)
                                elif co==2:
                                    print("Book Author: "+st)
                                elif co==3:
                                    print("Student Name: "+st)
                                elif co==4:
                                    print("Date"+st)
                                start=i

                            if line[i:i+1]=="}":
                                st=line[start:-3]
                                print("Date: "+ st)

        f.close()

    def Delete(self,r):
        if(os.path.exists("./temp.txt")):
            f=open("temp.txt","w+")
            f.truncate()

        f = open("StdentDB.txt", "r+")
        for line in f:
            if r in line:
                print(line+" \n line Deleted sucessfully.......")
                ele=line
        f.close()

        f = open("StdentDB.txt", "r+")
        lines=f.readlines()
        f.close()

        f=open("temp.txt","w+")
        for line in lines:
            if ele.strip() !=line.strip():
                f.write(line)
        f.close()

        f=open("temp.txt","r+")
        lines=f.readlines()
        f.close()

        f2 = open("StdentDB.txt", "r+")
        f2.truncate()
        f2.close()

        f2=open("StdentDB.txt", "a+")

        for line in lines:
            f2.write(line)

        f2.close()
        f.close()

    def view_recored(self):
        f=open("StdentDB.txt","r+")
        lines=f.readlines()
        for line in lines:
            if line[0:1] == "{" and line[-2:-1] == "}":
                id=line[1:2]
                print("ID of Book: ",id)
                if "[" in line:

                    start = line.index("[")
                    end = line.index("}")
                    co = 0
                    for i in range(start, end + 1):
                        if line[i:i + 1] == ",":
                            st = line[start + 1:i]
                            co = co + 1
                            if co == 1:
                                print("Book Name: " + st)
                            elif co == 2:
                                print("Book Author: " + st)
                            elif co == 3:
                                print("Student Name: " + st)
                            elif co == 4:
                                print("Date" + st)
                            start = i
                        if line[i:i + 1] == "}":
                            st = line[start:-3]
                            print("Date: " + st)
        f.close()


class lib(record):

    def __init__(self,s):
        self.s=s

    def Choice(self):

        if(self.s==1):
            a=input("Enter a string to serche: ")

            if a.isnumeric():
                if "/" in a:
                    super(lib, self).Search(a)
                else:
                    super(lib, self).Search(a + ":")

            else:
                super(lib, self).Search(a)


        elif (self.s == 2):

            id=int(input("Enter Id of Book: "))
            b_name=input("Enter name of Book: ")
            author=input("Enter author name of Book: ")
            student_name=input("Enter Student name: ")
            date=input("Enter date of borrow: ")

            super(lib, self).__init__(id,b_name,author,student_name,date)
            super(lib, self).Add_record()

        elif (self.s == 3):
            a = input("Enter a string to delete: ")

            if a.isnumeric():
                if "/" in a:
                    super(lib, self).Delete(a)
                else:
                    super(lib, self).Delete(a + ":")

            else:
                super(lib, self).Delete(a)


        elif (self.s == 4):
            super(lib, self).view_recored()

        elif (self.s == 5):
            exit(0)


    @staticmethod
    def Home():
        print("", end="\n")

        print("*******************************************", end="\n")
        print("******** Libarary Manegment System ********", end="\n")
        print("*******************************************", end="\n")

        print("", end="\n")

        print("-------------------------------------------", end="\n")
        print("Index.")
        print("1. Search Available Books")
        print("2. Add Book")
        print("3. Deleate Book")
        print("4. View Books")
        print("5. Exit")

        print("-------------------------------------------", end="\n")



lib.Home()
ch=int(input("Enter choice [1-6]: "))
while ch!=6 :
    select=lib(ch)
    select.Choice()
    ch = int(input("Enter choice [1-6]: "))












