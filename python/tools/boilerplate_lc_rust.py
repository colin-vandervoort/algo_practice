if __name__ == "__main__":
    import os
    import shutil
    import subprocess
    import sys

    base_project_directory = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )

    boilerplate_base_config_file_path = os.path.abspath(
        os.path.join(
            base_project_directory,
            "_tools",
            "boilerplate",
            "lc_rust_outer",
        )
    )
    template_url_args = ["--template-url", boilerplate_base_config_file_path]

    golang_leetcode_problems_dir = os.path.abspath(
        os.path.join(
            base_project_directory,
            "rust",
            "solutions",
            "src",
            "leetcode",
        )
    )
    output_folder_args = ["--output-folder", golang_leetcode_problems_dir]

    boilerplate_bin_name = "boilerplate"

    if not shutil.which(boilerplate_bin_name):
        raise FileNotFoundError("The 'boilerplate' binary was not found in your PATH.")

    subprocess.run(
        [
            boilerplate_bin_name,
            *template_url_args,
            *output_folder_args,
            "--disable-dependency-prompt",
            *sys.argv[1:],
        ],
        check=True,
    )
