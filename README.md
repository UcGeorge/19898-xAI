## Code Quality and Type Checking

This project uses GitHub Actions to enforce code quality, consistency, and type checking. All pull requests are automatically checked for PEP 8 violations using Flake8 and type issues using mypy.

To run the checks locally:

1. Install the required tools:
    ```
    pip install flake8 mypy
    ```

2. Run Flake8:
    ```
    flake8 .
    ```

3. Run mypy:
    ```
    mypy .
    ```

Please ensure your code passes all quality and type checks before submitting a pull request.
