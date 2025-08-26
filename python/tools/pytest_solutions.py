if __name__ == "__main__":
    import pytest
    import os

    base_project_directory = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
    solutions_dir = os.path.abspath(
        os.path.join(base_project_directory, "python", "solutions")
    )
    # cookiecutter_dir = os.path.abspath(
    #     os.path.join(
    #         base_project_directory, "python", "tools", "cookiecutter-leetcode-problem"
    #     )
    # )
    # ignored = [f"--ignore={dir}" for dir in [cookiecutter_dir]]

    pytest.main(
        [
            solutions_dir,
            # *ignored
        ]
    )
