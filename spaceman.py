# author : Mohit Narula

import os
import re
import datetime

my_path = "C:\\"
age_threshold = input("Enter age threshold in number of days: ")
user_file = input("Enter the file extension you'd like to get deleted -->\n"
                  "eg : .doc, .docx, .txt, .pdf, .xls = ")


def locate():
    locate_list = []
    for three in os.walk(my_path):
        for f in os.listdir(three[0]):
            if re.findall(r'{}'.format(user_file), f):
                file_time = datetime.date.fromtimestamp(
                    os.path.getmtime(three[0]+"\\"+f))
                log_age = abs(datetime.date.today()-file_time)
                if log_age.days > int(age_threshold):
                    locate_list.append(three[0]+"\\"+f)

    if len(locate_list) > 0:
        if len(locate_list) == 1:
            print("\nSpaceman found {} {} file older than {} days,"
                  .format(len(locate_list), user_file, age_threshold))
        print("\nSpaceman found {} {} files older than {} days,"
              .format(len(locate_list), user_file, age_threshold))
    return locate_list


def make_space():

    my_list = locate()
    if len(my_list) == 0:
        print("\nNothing to delete..Exiting..\n")
        return

    for item in my_list:
        try:
            os.remove(item)
        except WindowsError:
            print("Can't delete file = {} due to access issues, "
                  "moving on!".format(item))
    print("\nDeleted..! Enjoy more space!\n".format(user_file))


if __name__ == "__main__":
    make_space()
