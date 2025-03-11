#!/bin/bash

# APP VALUES
ENV_FILE="../.env"
MAIN_FILE_PATH="../src/app/main.py"


# DEFAULT VALUES
PYTHON_CMD="python3"
OS_TYPE="unix"
SCRIPT_MESSAGE="Bash SCRIPT (start_app.sh) MESSAGE:"

while getopts "uw" opt; do
  case $opt in
    u) OS_TYPE="unix";;
    w) OS_TYPE="windows";;
    *) echo "$SCRIPT_MESSAGE Usage: $0 [-u] [-w]" >&2
       exit 1
  esac
done
shift $((OPTIND-1))

if [ "$OS_TYPE" = "windows" ]; then
    PYTHON_CMD="py"
else
    if ! command -v python3 &> /dev/null; then
        echo "$SCRIPT_MESSAGE Python3 not found, trying py..."
        PYTHON_CMD="py"
    fi
fi

if [ ! -f "$ENV_FILE" ]; then
    echo "$SCRIPT_MESSAGE Error: .env file not found at $ENV_FILE" >&2
    exit 1
fi

set -a
source "$ENV_FILE"
set +a

if [ ! -f "$MAIN_FILE_PATH" ]; then
    echo "$SCRIPT_MESSAGE Error: main.py not found at $MAIN_FILE_PATH" >&2
    exit 1
fi

if ! command -v $PYTHON_CMD &> /dev/null; then
    echo "$SCRIPT_MESSAGE Error: Python command not found ($PYTHON_CMD)" >&2
    exit 1
fi

exec $PYTHON_CMD "$MAIN_FILE_PATH" "$@"
