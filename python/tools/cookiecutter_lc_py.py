if __name__ == "__main__":
    from cookiecutter.main import cookiecutter
    import os

    base_project_directory = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
    py_lc_solutions_dir = os.path.abspath(
        os.path.join(base_project_directory, "python", "solutions", "leetcode")
    )
    cookiecutter_template_python_solution = os.path.abspath(
        os.path.join(base_project_directory, "_tools", "cookiecutter", "lc_py")
    )

    cookiecutter(
        template=cookiecutter_template_python_solution, output_dir=py_lc_solutions_dir
    )
