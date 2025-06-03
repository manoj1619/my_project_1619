#!/bin/bash

echo "Setting up Git Hooks & Installing Dependencies..."

# Set custom hook directory
echo "Configuring Git to use custom hooks directory (.githooks/)..."
git config core.hooksPath .githooks/

# Ensure required tools are installed
MISSING_TOOLS=()
for TOOL in clang-format clang-tidy cppcheck pre-commit doxygen; do
    if ! command -v $TOOL &> /dev/null; then
        MISSING_TOOLS+=($TOOL)
    fi
done

if [ ${#MISSING_TOOLS[@]} -ne 0 ]; then
    echo " Missing tools detected: ${MISSING_TOOLS[*]}"
    echo "Installing missing tools: ${MISSING_TOOLS[*]}..."
    sudo apt-get update && sudo apt-get install -y ${MISSING_TOOLS[*]}
else
    echo "All required tools are already installed."
fi

echo "Setup complete! Pre-commit hooks will now run automatically when committing code."
