import time
from queue import Queue

start_time = time.perf_counter()

file = open("input.txt")
n = int(file.readline())

student = {}
hospital = {}
unvisited = Queue()
matchings = ["none"] * n

for i in range(n):
    hospital[i + 1] = {"preferences" : [int(x) for x in file.readline().split(" ")], "matched" : "none", "visited" : "none"}
    unvisited.put(i + 1)

for i in range(n):
    student[i+1] = {"preferences" : [int(x) for x in file.readline().split(" ")], "matched" : "none", "visited" : "none"}

while not unvisited.empty():
    hospital_num = unvisited.get()
    student_index = 0
    if hospital[hospital_num]["visited"] != "none":
        student_index = hospital[hospital_num]["visited"]
    for i in range(student_index, len(hospital[hospital_num]["preferences"])):
        student_num = hospital[hospital_num]["preferences"][i]
        if student[student_num]["matched"] == "none":
            student[student_num]["matched"] = hospital_num
            break
        elif student[student_num]["preferences"].index(hospital_num) < student[student_num]["preferences"].index(int(student[student_num]["matched"])):
            hospital[int(student[student_num]["matched"])]["matched"] = "none"
            unvisited.put(int(student[student_num]["matched"])-1)
            student[student_num]["matched"] = hospital_num
            hospital[hospital_num]["matched"] = student_num
            hospital[hospital_num]["visited"] = i
        else:
            pass


end_time = time.perf_counter()
exec_time = end_time - start_time

print(student)
print(hospital)
print(exec_time)
