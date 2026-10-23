#Q2
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
#Stage 1: Averages
for stu in students:
    m = 0
    n = 0
    for i in students[stu]:
        m = m + i
        n += 1
    ave = m/n
    print(f"{stu} {ave:.2f}") 

#Stage 2: Grades
for stu in students:
    m = 0
    n = 0
    for i in students[stu]:
        m = m + i
        n += 1
    ave = m/n 
    if ave >= 85:
        print(f"{stu} {ave:.2f} A")
    elif ave >= 70:
        print(f"{stu} {ave:.2f} B")
    elif ave >= 50:
        print(f"{stu} {ave:.2f} C")
    else:
        print(f"{stu} {ave:.2f} F") 

#Stage 3: Topper
t = 0
for stu in students:
    m = 0
    n = 0
    for i in students[stu]:
        m = m + i
        n += 1
    ave = m/n 
    if ave > t:
        t = ave
        top = stu
print(f"Topper: {top}")

#Stage 4: Menu
while True:
    print("1. Add Student")
    print("2. View All")
    print("3. Show Topper")
    print("4. Exit")
    uo = int(input("Enter option: "))
    if uo == 1:
        name = input("Enter Student Name: ")
        if name in students:
            print("Student already exists.")
            continue

        #Stage 5: Validation
        marks = []
        for subject in (1, 2, 3):
            while True:
                mark = int(input(f"Enter mark {subject}: "))
                if 0<= mark <= 100:
                    marks.append(mark)
                    break
                print("Invalid mark, try again.")
        students[name] = marks
  
    elif uo == 2:
            for name in students:
                print(f"{name}: {students[name]}")
    elif uo == 3:
        t = 0
        for stu in students:
            m = 0
            n = 0
            for i in students[stu]:
                m = m + i
                n += 1
            ave = m/n 
            if ave > t:
                t = ave
                top = stu
        print(f"Topper: {top}")
    elif uo == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid Input")

