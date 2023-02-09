import re

def get_file():
    file_path = input()
    counter = 0
    with open(file_path) as file:
        for count, line in enumerate(file):
            process_line(count, line)
            if line.strip():
                if counter > 2:
                    line_message(str(count + 1), "S006", "More than two blank lines used before this line")
                counter = 0
            else:
                counter = counter + 1



def process_line(count, line):
    if len(line) > 79:
        line_message(str(count + 1), "S001", "Too long")

    if re.match('^(\s{4})+\S|^\S.*', line) is None and line.strip():
        line_message(str(count + 1), "S002", "Wrong indentation")

    #when there are no comments in line
    if line.endswith(";\n") and "#" not in line:
        line_message(str(count + 1), "S003", "Unnecessary semicolon")

    #when comment in line - # later in string than ;
    if "#" in line and ";" in line and line.index("#") > line.index(";"):
        line_message(str(count + 1), "S003", "Unnecessary semicolon")

    if "#" in line and not line.strip().startswith("#") and not re.match("^[^#]+\s\s+#.*", line):
        line_message(str(count + 1), "S004", "At least two spaces required before inline comments")

    if "#" in line and "todo" in line.lower():
        line_message(str(count + 1), "S005", "TODO found")


def line_message(line_no, code, message):
    print("Line {}: {} {}".format(line_no, code, message))

def main():
    get_file()

if __name__ == "__main__":
    main()