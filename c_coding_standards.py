#!/usr/bin/env python3
import re
import sys

def check_naming_convention(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    errors = []
    inside_struct_or_enum = False
    last_comment_block = []

    for i, line in enumerate(lines, 1):
        line_strip = line.strip()

        # Track last Doxygen-style comment block
        if line_strip.startswith("/**") or line_strip.startswith("///"):
            last_comment_block = [line_strip]
            continue
        elif line_strip.startswith("*") and last_comment_block:
            last_comment_block.append(line_strip)
            continue
        elif line_strip.endswith("*/") and last_comment_block:
            last_comment_block.append(line_strip)
            continue

        # Skip empty or comment-only lines
        if not line_strip or line_strip.startswith("//") or line_strip.startswith("/*"):
            continue

        # Check #define constants
        match = re.match(r"#define\s+(\w+)", line_strip)
        if match:
            const_name = match.group(1)
            if not re.fullmatch(r"[A-Z][A-Z0-9_]*", const_name):
                errors.append(f"Line {i}: Constant '{const_name}' should be in SCREAMING_SNAKE_CASE.")
            continue

        # Check typedef struct/enum CamelCase names
        match = re.match(r"typedef\s+(struct|enum)\s+\w*\s*{?", line_strip)
        if match:
            inside_struct_or_enum = True
            continue

        match = re.match(r"}\s*(\w+);", line_strip)
        if inside_struct_or_enum and match:
            name = match.group(1)
            if not re.fullmatch(r"[se]_[A-Z][a-zA-Z0-9]*", name):
                errors.append(f"Line {i}: typedef name '{name}' should follow s_MyStruct or e_MyEnum CamelCase convention.")
            inside_struct_or_enum = False
            continue

        # Check variable declarations
        variable_matches = re.findall(r"\b(?:int|char|float|double|bool|uint\d*_t|int\d*_t)\s+(\w+)", line)
        for var in variable_matches:
            if not re.fullmatch(r"[a-z_][a-z0-9_]*", var):
                errors.append(f"Line {i}: Variable '{var}' should be in snake_case with meaningful name.")

        # Check function definitions and Doxygen comments
        match = re.match(r"(?:\w+\s+)+\*?(\w+)\s*\(([^)]*)\)\s*{?", line)
        if match:
            func_name = match.group(1)
            if not re.fullmatch(r"[a-z_][a-z0-9_]*", func_name):
                errors.append(f"Line {i}: Function '{func_name}' should be in snake_case.")

            # Check for Doxygen comment block above function
            if not any(tag in ''.join(last_comment_block) for tag in ["@brief", "@param", "@return"]):
                errors.append(f"Line {i}: Function '{func_name}' is missing proper Doxygen comment with @brief, @param(s), and @return.")
            last_comment_block = []

            # Check function arguments
            args = match.group(2).split(",")
            for arg in args:
                arg = arg.strip()
                parts = arg.split()
                if len(parts) == 2:
                    arg_name = parts[1]
                    if not re.fullmatch(r"[a-z_][a-z0-9_]*", arg_name):
                        errors.append(f"Line {i}: Function argument '{arg_name}' should be in snake_case.")

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
        print("C Naming Conventions Passed.")

is this code identifying indentation space error
