import csv

# Use an infinite while loop so the menu stays open until choice 6 is selected
while True:
    print("\n--- Student Management System ---")
    print("1. View Students")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Add Student")
    print("6. Exit")
    
    choice = int(input("Enter the choice: "))

    # 1. VIEW ALL STUDENTS
    if choice == 1:
        print("\n--- Student List ---")
        try:
            m = open("excel_workbook.csv", "r")
            reader = csv.reader(m)
            
            # Print column headers nicely
            print(f"{'Roll No':<10} {'Student Name':<20} {'Course':<15} {'Marks':<10}")
            print("-" * 60)
            
            for row in reader:
                if row:
                    print(f"{row[0]:<10} {row[1]:<20} {row[2]:<15} {row[3]:<10}")
            m.close()
        except FileNotFoundError:
            print("No records found. The file does not exist yet.")

    # 2. SEARCH STUDENT
    elif choice == 2:
        search_name = input("Enter the Student Name to search: ").strip().lower()
        found = False
        
        try:
            m = open("excel_workbook.csv", "r")
            reader = csv.reader(m)
            for row in reader:
                if row and row[1].lower() == search_name:
                    print(f"\nStudent Found:\nRoll No: {row[0]}\nName: {row[1]}\nCourse: {row[2]}\nMarks: {row[3]}")
                    found = True
                    break
            m.close()
            if not found:
                print("Student not found.")
        except FileNotFoundError:
            print("No data available to search.")

    # 3. UPDATE STUDENT
    elif choice == 3:
        search_name = input("Enter the Student Name to update: ").strip().lower()
        updated_rows = []
        found = False
        
        try:
            m = open("excel_workbook.csv", "r")
            reader = csv.reader(m)
            for row in reader:
                if row:
                    if row[1].lower() == search_name:
                        print(f"Current Details: {row}")
                        # Roll number stays the same, we update the other details
                        student_name = input("Enter new Student Name: ")
                        course = input("Enter new course: ")
                        marks = input("Enter new Marks: ")
                        updated_rows.append([row[0], student_name, course, marks])
                        found = True
                    else:
                        updated_rows.append(row)
            m.close()
            
            if found:
                m = open("excel_workbook.csv", "w", newline="")
                writer = csv.writer(m)
                writer.writerows(updated_rows)
                m.close()
                print("Student details updated successfully.")
            else:
                print("Student not found.")
        except FileNotFoundError:
            print("No data available to update.")

    # 4. DELETE STUDENT & AUTO-SEQUENCE