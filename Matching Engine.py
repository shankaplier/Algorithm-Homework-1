import os
import time
from queue import Queue
import sys

if __name__ == "__main__":

    n = 0
    student = {}
    hospital = {}
    unvisited = Queue()

    with open(sys.argv[1], "r") as f:
        f.seek(0, os.SEEK_END)
        file_size = f.tell()

        if file_size == 0:
            raise Exception("Empty file")
        else:
            f.seek(0)

        index = 0
        n = int(f.readline())

        # try:
        for i in range(n):
            hospital[i + 1] = {"preferences" : [int(x) for x in f.readline().split(" ")], "matched" : "none", "visited" : "none"}
            unvisited.put(i + 1)

        for i in range(n):
            student[i+1] = {"preferences" : [int(x) for x in f.readline().split(" ")], "matched" : "none", "visited" : "none"}

        f.close()

    matchings = ["none"] * n

    start_time = time.perf_counter()
# except:
#     if len(hospital) > len(student):
#         print(f"given {len(student)} students instead of {n}. Please enter n students")
#     elif len(hospital) > len(student):
#         print(f"given {len(hospital)} hospitals instead of {n}. Please enter n hospitals")
#     elif len(hospital) == len(student):
#         print(f"given {len(hospital)} hospitals and student instead of {n}. Please enter n hospitals and students")
#     quit()

    while not unvisited.empty():
        hospital_num = unvisited.get()
        student_index = 0
        if hospital[hospital_num]["visited"] != "none":
            student_index = hospital[hospital_num]["visited"]
        for i in range(student_index, len(hospital[hospital_num]["preferences"])):
            student_num = hospital[hospital_num]["preferences"][i]
            if student[student_num]["matched"] == "none":
                student[student_num]["matched"] = hospital_num
                hospital[hospital_num]["matched"] = student_num
                hospital[hospital_num]["visited"] = i
                break
            elif student[student_num]["preferences"].index(hospital_num) < student[student_num]["preferences"].index(int(student[student_num]["matched"])):
                hospital[int(student[student_num]["matched"])]["matched"] = "none"
                unvisited.put(int(student[student_num]["matched"]))
                student[student_num]["matched"] = hospital_num
                hospital[hospital_num]["matched"] = student_num
                hospital[hospital_num]["visited"] = i
                break
            else:
                pass


    end_time = time.perf_counter()
    exec_time = end_time - start_time

    print(student)
    print(hospital)
    print(exec_time)
