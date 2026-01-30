

def read_matching_output(output_filename):
    matches = {}
    try:
        with open(output_filename, 'r') as f:
            for line in f.readlines():
                hospital_id, student_id = line.strip().split(',')
                matches[int(hospital_id)] = int(student_id.strip())
    except IOError:
        print("Error reading output file from Matching Engine")
    print(matches)
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
        return True, "Valid Matching"

def check_stability(matches):
    pass


if __name__ == '__main__':
    read_matching_output("../output.out")
    print("---------")

    n, hospital_prefs, student_prefs = read_input("../input/basic_stable_input.txt")
    print(n)
    print(hospital_prefs)
    print(student_prefs)

