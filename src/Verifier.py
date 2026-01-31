# SHANE DOWNS AND SHASHANK GUTTA VERIFIER
import time
import sys

def read_matching_output(output_filename):  # Retrieve the outputs for verification
    matches = {}
    try:
        with open(output_filename, 'r') as f:
            for line in f.readlines():
                hospital_id, student_id = line.strip().split(',')
                matches[int(hospital_id)] = int(student_id.strip())
    except IOError:
        print("Error reading output file from Matching Engine")
    #print(matches)
    return matches

def read_input(input_filename):  # Read in the inputs used for matching engine
    hospital_prefs = dict()
    student_prefs = dict()
    n = None
    try:
        with open(input_filename, 'r') as f:
            n = int(f.readline().strip())

            for i in range(1, n + 1):
                prefs = list(map(int, f.readline().strip().split()))
                hospital_prefs[i] = prefs

            for i in range(1, n + 1):
                prefs = list(map(int, f.readline().strip().split()))
                student_prefs[i] = prefs

    except IOError:
        print("Error reading input file")

    return n, hospital_prefs, student_prefs

def check_validity(n, matches):
    if len(matches.keys()) != n:  # Check duplicates and hospital count
        return False, "Wrong number of hospitals in matches"
    elif len(set(matches.values())) != n:  # Ensure no duplicates and correct number of students
        return False, "Duplicate or missing students in matches"
    elif set(matches.keys()) != set(range(1, n + 1)):   # Hospital ID outside of scope
        return False, "Invalid hospital ids"
    elif set(matches.values()) != set(range(1, n + 1)):  # Check student id numbers in scope
        return False, "Invalid student ids"
    else:
        return True, "Valid Matchings"

def check_stability(n, matches, hospital_prefs, student_prefs):
    student_to_hospital = {s: h for h, s in matches.items()}
    # use reverse student->hospital map for lookup in later step
    for h in range(1, n + 1):  # Loop through all n hospitals
        curr_student = matches[h] # Find the current student the hospital is matched with
        for s in hospital_prefs[h]:
            if s == curr_student:  # keep looping while students are preferred over current match
                break
            students_curr_hospital = student_to_hospital[s]
            student_pref_list = student_prefs[s]
            if student_pref_list.index(h) < student_pref_list.index(students_curr_hospital):
                # If both h and s prefer another candidate, we have a blocking/unstable pair
                return False, f"Unstable: Hospital {h} and student {s} form blocking pair"

    return True, "Stable Matchings"

def run_verifier(input_file_path, output_file_path):
    #start_time = time.perf_counter()
    matches = read_matching_output(output_file_path)
    n, hospital_prefs, student_prefs = read_input(input_file_path)

    is_valid, message = check_validity(n, matches)
    print(message)

    if is_valid:
        is_stable, message = check_stability(n, matches, hospital_prefs, student_prefs)
        print(message)
    else:
        print("INVALID")
    #end_time = time.perf_counter()
    #elapsed_time = end_time - start_time

    #print(f"Elapsed Time: {elapsed_time} seconds")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 Verifier.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    run_verifier(input_file, output_file)