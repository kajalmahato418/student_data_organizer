#Collection Manipulator Student Data organizer 
print("Welcome to the Student Data Organizer!")
print()
#List-stores multiple student IDs
student_list = []

while True:

    print ("Select an option: ")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number from 1 to 6.")
        print()
        continue
    print()

    if choice==1:
        print("\nEnter student details: ")
        student_id = int(input ("Enter student id: "))
        name = input("Enter the student name: ")
        age = int(input("Enter your age: "))
        grade = input("Enter your grade: ")
        dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
        subjects = input("Enter the student subjects (comma-separated): ").split(",")

        subject_set = set()
        
        for subject in subjects:
            subject_set.add(subject.strip())


        # storing student id and dob in a Tuple
        std_info = (student_id,dob)
        
        student_dict = {
            "name": name,
             "age": age,
             "grade": grade,
             "subjects": subject_set,
              "info": std_info 
                }

        student_list.append(student_dict)
        print()
        print ("Student added successfully!")
        print()

    elif choice==2: 
        print ("--- Display All Students ---")

        for student in student_list:
            print(f"Student ID: {student['info'][0]} | Name: {student['name']} | Student AGE: is {student['age']} | Student grade is: {student['grade']} | Student dob is: {student['info'][1]} | Student subjects: {student['subjects']} " )

    elif choice==3:
        print ("\n--- update Student Information ---")
        up_id = int(input("Enter student ID to update: "))
        found = False

        for student in student_list:
            if student['info'][0] == up_id: 
                found = True
                print(f"Current Details-> Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Subjects: {student['subjects']}")

                student['name'] = input("Enter new name: ")
                student['age'] = int(input("Enter new age: "))
                student['grade'] = input("Enter new grade: ")

                print("Enter new subjects (comma-separated):")
                sub_input = input()
                student['subjects'] = set(s.strip() for s in sub_input.split(','))
                
                print("Student information updated successfully!")
                break

        if not found:
            print("Student ID not found!")

        print()

    elif choice==4:
        print("\n---Delete Student ---")
        del_id = int(input("Enter Student ID to delete: "))

        for i in range(len(student_list)):
            if student_list[i]['info'][0] == del_id:
                del student_list[i]
                print("Student deleted successfully!")
                break

        else:
            print("student ID not found!")

        print()

    elif choice==5:
        print("\n---Display Subjects Offered---")
        all_subjects = set()
        for s in student_list: 
            all_subjects.update(s['subjects'])

        if len(all_subjects) == 0:
            print("No subjects found!")
        else:
            print(f"Subjects Offered: {all_subjects}")
        print()

    elif choice==6:
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice! Please enter 1-6.")

                


                
