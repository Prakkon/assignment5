
students = {'Alice':85, 'Merry':56, 'Francis':94, 'Sebastian':89}

def task1():
    # dict stores name:marks pairs

    attempt = menu()
    try:
        if students[attempt]:
            print("{}'s marks: {}".format(attempt, students[attempt]))

    except KeyError:
        print("Student not found.")

    finally:
        y = input("Do you want to continue? [y/n]: ")
        if y == 'y':
            task1()
        else:
            exit()

    return

def menu():
    x = input("Enter the student's name: ")

    return x

task1()
