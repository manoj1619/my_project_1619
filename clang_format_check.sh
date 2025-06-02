#!/bin/bash

has_error=0

for file in "$@"; do
    # Skip non-existent files (e.g., deleted in git)
    [ -f "$file" ] || continue

    tmpfile=$(mktemp)

    # Generate formatted output
    clang-format "$file" > "$tmpfile"

    # Compare original and formatted output
    if ! diff -q "$file" "$tmpfile" > /dev/null; then
        echo "✖ $file is not properly indented. Run: clang-format -i $file"
        has_error=1
    fi

    rm "$tmpfile"
done

exit $has_error

