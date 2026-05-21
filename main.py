from models import SystemManagement

def main():

    system_management = SystemManagement()

    system_management.load_data()

    while True:
        print("\n=== students management system ===")

        print("1. add student")
        print("2. show students")
        print("3. search student")
        print("4. delete student")
        print("5. add course")
        print("6. show courses")
        print("7. search course")
        print("8. delete course")
        print("9. enroll student")
        print("10. unenroll student")
        print("11. exit")

        choice = input("choose: ").strip()

        if choice == "1":
            system_management.add_student()
            system_management.save_data()

        elif choice == "2":
            system_management.show_students()

        elif choice == "3":
            system_management.search_student()

        elif choice == "4":
            system_management.delete_student()
            system_management.save_data()

        elif choice == "5":
            system_management.add_course()
            system_management.save_data()

        elif choice == "6":
            system_management.show_courses()

        elif choice == "7":
            system_management.search_course()

        elif choice == "8":
            system_management.delete_course()
            system_management.save_data()

        elif choice == "9":
            system_management.enroll_student()
            system_management.save_data()

        elif choice == "10":
            system_management.unenroll_student()
            system_management.save_data()

        elif choice == "11":
            system_management.save_data()
            print("exited!")
            break

        else:
            print("invalid choice!")

if __name__ == "__main__":
    main()
