#!/bin/bash

# APP VALUES
ENV_FILE="./.env"
MAIN_FILE_PATH="./src/app/main.py"
APP_NAME="app"

# DEFAULT VALUES
SCRIPT_MESSAGE="Bash SCRIPT (start_app.sh) MESSAGE:"
VENV_DIR=".venv"

# Detect OS type
OS_TYPE="unix"
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
    OS_TYPE="windows"
fi

# Create virtual environment if not exists
if [ ! -d "$VENV_DIR" ]; then
    echo "$SCRIPT_MESSAGE Creating virtual environment with uv..."
    uv venv "$VENV_DIR"
fi

# Activate virtual environment
if [ "$OS_TYPE" = "windows" ]; then
    source "$VENV_DIR/Scripts/activate"
else
    source "$VENV_DIR/bin/activate"
fi

# Load environment variables
if [ ! -f "$ENV_FILE" ]; then
    echo "$SCRIPT_MESSAGE Error: .env file not found at $ENV_FILE" >&2
    deactivate
    exit 1
fi

set -a
source "$ENV_FILE"
set +a

# Ensure main.py exists
if [ ! -f "$MAIN_FILE_PATH" ]; then
    echo "$SCRIPT_MESSAGE Error: main.py not found at $MAIN_FILE_PATH" >&2
    deactivate
    exit 1
fi

export PYTHONPATH="$(pwd)/src"

echo "$SCRIPT_MESSAGE Starting app..."
uv run "$MAIN_FILE_PATH" "$@"

# Deactivate virtual environment after the script ends
deactivate

echo "$SCRIPT_MESSAGE App stopped."
