import numpy as np
#PROGRAM'S TASKS
#Calculation of the end-of-term grade ((Midterm *(40/100)) + (Final *(60/100)))
#Class mean,
#Finding the highest and lowest grades,
#Analysis of the class's achievement distribution using standard deviation,
#identification of student data for those falling below and those exceeding a specific threshold...
def term_grade(class_total_grades,student_names):
    left = np.sum(class_total_grades >= 60)
    passing = np.sum(class_total_grades < 60)
    print("**********************************")
    char_grade = get_char_grades(class_total_grades)
    for i in range(len(class_total_grades)):
        print(f"{student_names[i]} Term Grade : {class_total_grades[i]:.2f} , Char Grade = {char_grade[i]} {"Geçti" if class_total_grades[i] > 60 else "Kaldı"}")
    print(f"How Many People Left: {left} | How Many People Pass: {passing}")
    print("**********************************")

def get_char_grades(grades):
    chars= ["AA","BA","BB","CB","CC","DC","DD","FD","FF","F-"]
    conditions = [
        (grades >= 90), (grades >= 85), (grades >= 80), (grades >= 75),
        (grades >= 70), (grades >= 65), (grades >= 60), (grades >= 50),
        (grades >= 40), (grades < 40) # 0  - 39.9 -> F-
    ]
    return np.select(conditions, chars,default="F-")

def mean_hes(class_total_grade):

    class_mean = np.mean(class_total_grade)
    print("**********************************")
    print(f"Class Mean = {class_mean:.2f}")
    print("**********************************")


def best_min(class_total_grade,student_names):#BEST VE MİNİ GÖSTER LİSTEDEN
    print("**********************************")
    print(f"Best Grade in Class: {class_total_grade.max():.2f} His/Her İndex: {(class_total_grade.argmax())+1}  His/Her Name: {student_names[class_total_grade.argmax()]}")
    print(f"Min Grade in Class: {class_total_grade.min():.2f} His/Her İndex: {class_total_grade.argmin()+1}   His/Her Name: {student_names[class_total_grade.argmin()]}")
    print("**********************************")


def stand_devia(class_total_grade):
    print("**********************************")
    print(f"Standart Deviation Of Class: {class_total_grade.std():.2f} %")
    print("**********************************")


def dist_of_succ(class_total_grade):#grafiksel olarak yazdıracağız
    print("*********************************")
    slices = [0,40,50,65,70,75,80,85,90,95,100]
    yuzdelik_array = np.histogram(class_total_grade, bins=slices)
    print(f"Get F- Student: {yuzdelik_array[0][0]}---{(yuzdelik_array[0][0]/len(class_total_grade))*100:.3f}%")
    print(f"Get FF Student: {yuzdelik_array[0][1]}---{(yuzdelik_array[0][1]/len(class_total_grade))*100:.3f}%")
    print(f"Get FD Student: {yuzdelik_array[0][2]}---{(yuzdelik_array[0][2]/len(class_total_grade))*100:.3f}%")
    print(f"Get DD Student: {yuzdelik_array[0][3]}---{(yuzdelik_array[0][3]/len(class_total_grade))*100:.3f}%")
    print(f"Get DC Student: {yuzdelik_array[0][4]}---{(yuzdelik_array[0][4]/len(class_total_grade))*100:.3f}%")
    print(f"Get CC Student: {yuzdelik_array[0][5]}---{(yuzdelik_array[0][5]/len(class_total_grade))*100:.3f}%")
    print(f"Get CB Student: {yuzdelik_array[0][6]}---{(yuzdelik_array[0][6]/len(class_total_grade))*100:.3f}%")
    print(f"Get BB Student: {yuzdelik_array[0][7]}---{(yuzdelik_array[0][7]/len(class_total_grade))*100:.3f}%")
    print(f"Get BA Student: {yuzdelik_array[0][8]}---{(yuzdelik_array[0][8]/len(class_total_grade))*100:.3f}%")
    print(f"Get AA Student: {yuzdelik_array[0][9]}---{(yuzdelik_array[0][9]/len(class_total_grade))*100:.3f}%")
    print("*********************************")




def main():
    try:
        csv_file = "exdataset.csv"
        data = np.genfromtxt(csv_file, delimiter=",",dtype=None, names=True, encoding="utf-8")
        student_names = data["name"]
        student_midterm = data["midterm"]
        student_final = data["final"]
        student_grade_set = np.column_stack((student_midterm, student_final))

        class_total = np.array([])

        class_total = (student_grade_set[:,0]*0.4 + student_grade_set[:,1]*0.6)
        print("File Successfully Loaded!")
    except FileNotFoundError:
        print(f"Error: Don't find {csv_file}!")
        print("Please consolidate the size of your project in the directory!")
        return

    print("**********************************")
    print("Welcome to Student Analysis System")
    print("**********************************")
    program = True
    while program:
        print("1-)SHOW GRADE/CHAR\n2-)SHOW CLASS MEAN\n3-)SHOW BEST/MİN\n4-)SHOW STANDART DEVIATION\n5-)SHOW DISTRIBUTION OF SUCCESS\n6-)EXIT")
        choice = input("What would you like to choice?\n")
        if choice == "1":
            term_grade(class_total,student_names)
        elif choice == "2":
            mean_hes(class_total)
        elif choice == "3":
            best_min(class_total,student_names)
        elif choice == "4":
            stand_devia(class_total)
        elif choice == "5":
            dist_of_succ(class_total)
        elif choice == "6":
            program = False
        else:
            print("**********************************")
            print("Invalid Choice")
            print("**********************************")
    print("************************************")
    print("Goodbye and Have a nice day!")
    print("************************************")

if __name__ == "__main__":
    main()
