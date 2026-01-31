import os
import time
from queue import Queue
import sys

output_filename = "../output/size-512.out"

if __name__ == "__main__":

    student = {}
    hospital = {}
    unvisited = Queue()

    try:
        with open(sys.argv[1], "r") as f:
            f.seek(0, os.SEEK_END)
            file_size = f.tell()

            if file_size == 0:
                raise ValueError(f"{sys.argv[1]} is an Empty file. Please input a non empty-file.")
            else:
                f.seek(0)

            # Variable that keeps track of how many students and hospitals are in the input file
            data_size = int(f.readline())

            for i in range(data_size):
                temp_array = f.readline().rstrip().split(" ")
                if temp_array == ['']:
                    raise ValueError(f"expected {data_size} hospitals but received {len(hospital)}. Please enter more hospitals")
                for index in range(len(temp_array)):
                    if int(temp_array[index]) <= data_size:
                        temp_array[index] = int(temp_array[index])
                    else:
                        raise ValueError(f"For hospital {i+1}, received student {int(temp_array[index])} who is greater than the number of students possible {data_size}. Please Rectify it")


                if len(temp_array) < data_size or len(temp_array) > data_size:
                    raise ValueError(f"For hospital {i+1}, received preference list of size {len(temp_array)} when it should be {data_size}.")
                elif len(set(temp_array)) < data_size:
                    raise ValueError(f"For hospital {i+1}, received duplicate students in preference list. Please make sure the students are distinct.")
                hospital[i+1] = {"preferences" : temp_array, "matched" : "none", "visited" : "none"}
                unvisited.put(i + 1)

            for i in range(data_size):
                temp_array = f.readline().rstrip().split(" ")
                if temp_array == ['']:
                    raise ValueError(f"expected {data_size} students but received {len(student)}. Please enter more students")
                for index in range(len(temp_array)):
                    if int(temp_array[index]) <= data_size:
                        temp_array[index] = int(temp_array[index])
                    else:
                        raise ValueError(
                            f"For student {i + 1}, received hospital {int(temp_array[index])} who is greater than the number of hospitals possible {data_size}. Please Rectify it")

                if len(temp_array) < data_size or len(temp_array) > data_size:
                        raise ValueError(f"For student {i+1}, received preference list of size {len(temp_array)} when it should be {data_size}.")
                elif len(set(temp_array)) < data_size:
                    raise ValueError(f"For student {i+1}, received duplicate hospitals in preference list. Please make sure the hospitals are distinct.")

                student[i + 1] = {"preferences": temp_array, "matched": "none", "visited": "none"}

            f.close()

        start_time = time.perf_counter()

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

        with open(sys.argv[2], "w") as f:
            for k, v in hospital.items():
                f.write(f'{k} {v["matched"]}\n')

        # print(exec_time)
    except ValueError as e:
        print(e)
