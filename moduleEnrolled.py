import math


class Enrolled:

    def __init__(self, name, presents, absences):
        self.name = name
        self.presents = presents
        self.absences = absences

    def __str__(self):
        return f"{self.name},{self.presents},{self.absences}"

    def print_to_file(self):
        return f"{self.name}"

    def update_presents(self):
        self.presents += 1
        return self.presents

    def update_absences(self):
        self.absences += 1
        return self.absences


class FinalStats:

    def __init__(self, module_name, module_code, average_attendance, stars_bar):

        self.module_name = module_name
        self.module_code = module_code
        self.average_attendance = average_attendance
        self.stars_bar = stars_bar

    def __str__(self):
        return f"{self.module_name:<28}{self.module_code:<13}{self.average_attendance:<6.1f}" \
               f"{self.stars_bar}"


# class GetAttendanceAverage:
#
#     def __init__(self, filename: str):
#         self.filename = filename
#
#     def calculating_average(self):
#         attendance_list = []
#         absences_list = []
#
#         with open(self.filename) as my_file:
#             for line in my_file:
#                 line = line.rstrip()
#                 line_date = line.split(',')
#                 attendance_list.append(int(line_date[1]))
#                 absences_list.append(int(line_date[2]))
#
#         num_of_students = len(attendance_list)
#         sum_of_attendance = sum(attendance_list)
#
#         average_days_present = sum_of_attendance / num_of_students
#         total_num_days = attendance_list[0] + absences_list[0]
#         average_attendance = (average_days_present / total_num_days) * 100
#
#         return average_attendance


class Stars:

    def __init__(self, average_num):
        self.average_num = average_num

    def get_stars_bar(self):
        num_stars = math.floor((math.floor(self.average_num)) / 10)
        status_bar = num_stars * "*"

        return status_bar
