# Python-Unit-Testing

## Setup dev environement
- Create the venv ``` $$ python3 -m venv venv_name ```
- Activate the env ``` $$ source path/venv/bin/activate ```
- Install pipenv   ``` $$ pip3 install pipenv ```
- Use pipenv to install packages ``` $$ pipenv install pytest ```
- [VS Code configuration](https://code.visualstudio.com/docs/python/testing)

## Unit test library
- **unittest**
- **doctest**
- **pytest**

## Test execution
- **unittest**
    1. Add the main() function than execute the file  ``` $$ python demo/test_program_unittest.py [-v] ```
    2. Execute the file with the command ``` $$ python -m unittest demo/test_program_unittest.py [-v] ```

- **doctest**
    1. Execute the file with the command ``` $$ python demo/doctest_example.py [-v] ```

- **pytest**
    1. Execute the file with the command ``` $$ pytest demo/test_program_pytest.py [-v] ```

## Coverege Test
- Install coverage ``` $$ pipenv install coverage ```
- Execute ``` $$ coverage run -m unittest demo/test_program_unittest.py [-v] ```
- Create an HTML page of the coverage with the command ``` $$ coverage html ```

## Pytest HTML Report
- Install coverage ``` $$ pipenv install pytest-html ```
- Execute ``` $$ pytest demo/test_program_pytest.py [-v] --html=path/file.html ```

## Others
- [Run tests in parallel](https://code.visualstudio.com/docs/python/testing#_run-tests-in-parallel)
