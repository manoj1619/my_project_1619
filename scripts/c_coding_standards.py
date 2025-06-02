import re
import sys

def check_naming_convention(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    # Patterns for naming convention checks
    variable_pattern = re.compile(r"\b(int|char|float|double)\s+([a-z][a-z0-9_]*)\b")
    constant_pattern = re.compile(r"#define\s+([A-Z_]+)\s+")
    struct_enum_pattern = re.compile(r"\b(struct|enum)\s+([A-Z][a-zA-Z0-9]*)\b")
    function_pattern = re.compile(r"\b[a-z_][a-z0-9_]*\s+\**([a-z_][a-z0-9_]*)\s*\(.*\)\s*{?")
    function_arg_pattern = re.compile(r"\b(int|char|float|double)\s+([a-z][a-z0-9_]*)\b")
    
    errors = []
    
    for i, line in enumerate(lines, 1):
        # Check variable names
        for match in variable_pattern.finditer(line):
            var_name = match.group(2)
            if not re.match(r"^[a-z_][a-z0-9_]*$", var_name):
                errors.append(f"Line {i}: Variable '{var_name}' should be in snake_case.")

        # Check function names
        for match in function_pattern.finditer(line):
            func_name = match.group(1)
            if not re.match(r"^[a-z_][a-z0-9_]*$", func_name):
                errors.append(f"Line {i}: Function '{func_name}' should be in snake_case.")

        # Check function arguments
        for match in function_arg_pattern.finditer(line):
            arg_name = match.group(2)
            if not re.match(r"^[a-z_][a-z0-9_]*$", arg_name):
                errors.append(f"Line {i}: Function argument '{arg_name}' should be in snake_case.")

        # Check constants
        for match in constant_pattern.finditer(line):
            const_name = match.group(1)
            if not re.match(r"^[A-Z_]+$", const_name):
                errors.append(f"Line {i}: Constant '{const_name}' should be in SCREAMING_SNAKE_CASE.")

        # Check struct/enum names
        for match in struct_enum_pattern.finditer(line):
            struct_name = match.group(2)
            if not re.match(r"^[A-Z][a-zA-Z0-9]*$", struct_name):
                errors.append(f"Line {i}: Struct/Enum '{struct_name}' should be in CamelCase.")

    return errors

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python c_coding_standards.py <C_FILE>")
        sys.exit(1)

    filename = sys.argv[1]
    errors = check_naming_convention(filename)
    
    if errors:
        for error in errors:
            print(error)
        sys.exit(1)
    else:
        print("C Naming Conventions Passed")
