def showmenu():
    marks={}
    while(True):
        print("***********Exam menu*********\n1.Marks Entry\n2.All Mark Display\n3.Student Marks\n4.Delete Entry\n5.Exit")
        c=2
        try:
            c=int(input("Please enter you choice:"))#valueError
        except ValueError:
            print("you must enter value between 1 to 5 only")
        match c:
            case 1:
                print("Mark entry:")
                roll=input("enter student rollno ")
                try:
                    n=int(input("enter marks"))#valueError
                    marks.update({roll: n})
                except ValueError:
                    print("marks values must be integer")
                print("--------marks entry successfully-----")
            case 2:
                print("All student marks")
                for k,v in marks.items():
                    print(f"marks of rollno {k} is {v}")
                print("--------marks displayed successfully-----")
            case 3:
                try:
                    r=input("enter student rollno")#keyError
                    print(f"marks of student with rollno {r} is {marks[r]}")

                except KeyError:
                    print("student rollno does not exist in our records")
                print("--------student marks displayed successfully-----")
            case 4:
                try:
                    r=input("enter student rollno")#keyError
                    marks.pop(r)
                except KeyError:
                    print("student rollno does not exist in our records")

                print("--------marks deleted successfully-----")

            case 5:
                print("--------program exit successfully-----")
                break





showmenu()