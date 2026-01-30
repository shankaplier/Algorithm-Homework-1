# SHANE DOWNS AND SHASHANK GUTTA VERIFIER

def read_matching_output(output_filename):
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

def read_input(input_filename):
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
    if len(matches.keys()) != n:
        return False, "Wrong number of hospitals in matches"
    elif len(set(matches.values())) != n:
        return False, "Duplicate or missing students in matches"
    elif set(matches.keys()) != set(range(1, n + 1)):
        return False, "Invalid hospital ids"
    elif set(matches.values()) != set(range(1, n + 1)):
        return False, "Invalid student ids"
    else:
        return True, "Valid Matchings"

def check_stability(n, matches, hospital_prefs, student_prefs):
    student_to_hospital = {s: h for h, s in matches.items()}
    for h in range(1, n + 1):
        curr_student = matches[h]
        for s in hospital_prefs[h]:
            if s == curr_student:
                break
            students_curr_hospital = student_to_hospital[s]
            student_pref_list = student_prefs[s]
            if student_pref_list.index(h) < student_pref_list.index(students_curr_hospital):
                return False, f"Unstable: Hospital {h} and student {s} form blocking pair"

    return True, "Stable Matchings"

if __name__ == '__main__':
    matches = read_matching_output("../output.out")
    n, hospital_prefs, student_prefs = read_input("../input/basic_stable_input.txt")

    is_valid, message = check_validity(n, matches)
    print(message)

    if is_valid:
        is_stable, message = check_stability(n, matches, hospital_prefs, student_prefs)
        print(message)
    else:
        print("INVALID")
