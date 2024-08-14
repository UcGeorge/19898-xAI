flake8 .
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo "Code style errors detected. Please fix them to continue."
    exit 1
else
    echo "No code style errors detected. You're good to go!"
fi
