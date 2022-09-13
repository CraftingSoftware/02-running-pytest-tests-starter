# Running Tests with pytest

## Due: Tuesday, September 20th, 2022 at 2:30 pm

## Introduction

In this lab assignment, you will run tests for an area-calculating module, `area.py`, with [pytest](https://docs.pytest.org). Analyzing the pytest results, you will fix bugs in the tests until all tests pass. Through this exercise, you will put into practice the following learning objective(s):

- How to run tests with pytest and analyze its results

## Instructions

Please perform each of the following steps in order.

### Analyze `area.py` and `tests/test_area.py`

Look through `area.py` and in `writing/reflection.md`, describe the code that someone would write to use the module to calculate the area of a square. Then, look through `tests/test_area.py`. In `writing/reflection.md`, explain the relationship between `area.py` and `tests/test_area.py`. Then, in `writing/reflection.md`, for one test in `tests/test_area.py`, identify the parts of the test. Lastly, in `writing/reflection.md`, describe how tests are named.

### Add pytest as a Development Dependency

First, run `poetry install` to install all of the dependencies listed in `pyproject.toml` in a local virtual environment. Then, run `poetry run pytest`. Notice that this command runs the `pytest` command in the virtual environment created by Poetry. When you run this command, you should see the following error:

```console
pyenv: pytest: command not found
```

Look through `pyproject.toml` and in `writing/reflection.md`, explain why this error occurred.

To install pytest in the local virtual environment, run `poetry add --dev pytest`. Remember that the `poetry add` command will install the specified dependency in the local virtual environment and add it to the list of dependencies in `pyproject.toml` so that anyone can replicate a virtual environment with all of the required dependencies for your project if they have your `pyproject.toml` file.

Notice that the `--dev` option was used in the `poetry add` command. The `--dev`, or `-D`, option will install the specified dependency as a _development_ dependency--that is, a dependency that is only required during the development of the project. You will notice in `pyproject.toml` that pytest is listed under the `[tool.poetry.dev-dependencies]` section, which lists all installed development dependencies. The `[tool.poetry.dependencies]` section, on the other hand, lists the _runtime_ dependencies, which are dependencies that are required during the runtime, or execution of the source code, of the project.

Any dependencies, such as testing and linting tools, that are used only during the development of a project should be installed as development dependencies. This is because when you distribute your project, and someone installs your package, their package manager (e.g. Poetry or pip) will install your package's runtime dependencies, but not its development dependencies. Package managers install only runtime dependencies since someone who uses your package only needs to execute your source code; and, installing only runtime dependencies means that your package will be faster to install and will add less bloat to their project (because all of your package's dependencies become their project's dependencies as well).

So, if any tools are not required during the runtime of a project, you should install them as development dependencies. One way to determine whether a tool is required during the runtime of a project is whether it is imported in the source code. Note that source code in this context does not include testing code. For example, Typer should be installed as a runtime dependency because you must `import typer` in the source code of your project. However, you do not `import pytest` in the source code of your project, pytest should be installed as a development dependency.

In `writing/reflection.md`, explain why you should add pytest as a _development_ dependency, rather than as a runtime dependency.

### Run pytest

Now that you have installed pytest, you can run the tests in `tests/test_area.py` by running `poetry run pytest`. Note that the `pytest` command will automatically run any files whose name starts or ends with `test`.

### Fix bugs in `tests/test_area.py`

In the pytest output, you will notice that half of the tests are failing. This is due to numerous bugs throughout `tests/test_area.py`. Using the pytest output, fix the bugs in `tests/test_area.py` until all tests pass. For a couple of bugs, you should refer to the [documentation for pytest's `approx` function](https://docs.pytest.org/en/7.0.x/reference/reference.html#pytest-approx).

In `writing/reflection.md`, explain why you had to use the `approx` function to fix some bugs in `tests/test_area.py`.

## GatorGrade

You can check the baseline requirements of this project by running department's assignment checking `gatorgrade` tool To use `gatorgrade`, you first need to make sure you have Python installed. Then, if you haven't done so already, you need to install `gatorgrade`:

- [install `pipx`](https://pypa.github.io/pipx/installation/)
- install `gatorgrade` with `pipx install gatorgrade`

Finally, you can run `gatorgrade`:

`gatorgrade --config config/gatorgrade.yml`

## Receiving Assistance

If you are having trouble completing any part of this assignment, then please talk with either the course instructor or a student technical leader during the lab session. Alternatively, you may ask questions in the Discord channel for this course. Finally, you can schedule a meeting during the course instructor's office hours.

## Assessment Strategy

This assignment will be assessed based on the following components:

- **Percentage of Passing GatorGrader Checks**: If source code is required, you should repeatedly update the implementation of your source code until it passes all of the GatorGrader checks by, for instance, producing the correct output. If technical writing is required, you should repeatedly revise your technical writing until it also passes all of GatorGrader's checks about, for instance, the length of its content.
- **Percentage of Passing GitHub Actions Checks**: You will receive checkmarks for any additional checks on source code and/or technical writing, other than the "Run GatorGrader" check, that are encoded in GitHub Actions. You will receive a checkmark for each passing GitHub Actions check. As with the previous grading component, you are encouraged to repeatedly amend your source code and/or technical writing until all of your GitHub Actions checks pass.

  - Please note that the "Check Spelling" GitHub Actions check may flag proper nouns or other real words if the dictionary it uses does not contain them. If your "Check Spelling" GitHub Actions check is failing due to a correctly spelled word being incorrectly flagged as "unknown" by CSpell, you will need to add the word to the list of words in `.github/cspell.json`.

- **Mastery of Software Engineering Concepts and Skills**: You will receive a checkmark for demonstrating mastery of each of the following concepts and skills of software engineering exercised in this assignment that is not checked by GatorGrader. If you receive checkmarks for all of the following concepts and skills and have all GatorGrader checks pass, you will know that you have mastered all of the learning objectives of this assignment. For this assignment, you must:

  - Make small, focused commits
  - Write commit messages that abide by [the seven rules of a great Git commit](https://cbea.ms/git-commit/message)
  - Correctly explain why you should add pytest as a _development_ dependency
  - Correctly explain why you had to use the `approx` function to fix some bugs in `tests/test_area.py`

All grades for this project will be reported through a student's GitHub gradebook repository (we will set this up soon).
