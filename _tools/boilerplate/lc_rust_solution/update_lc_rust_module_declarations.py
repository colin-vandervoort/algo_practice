import os
import re
import sys

if __name__ == "__main__":
    base_project_directory = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..")
    )
    rust_leetcode_solutions_module_dir = os.path.abspath(
        os.path.join(
            base_project_directory,
            "rust",
            "solutions",
            "src",
            "leetcode",
        )
    )

    module_names = []
    with os.scandir(rust_leetcode_solutions_module_dir) as entries:
        for entry in entries:
            if entry.is_file():
                continue
            if re.match(r"(\.DS_Store)$", entry.name):
                continue
            module_names.append(entry.name)

    module_declaration_file_path = os.path.join(
        rust_leetcode_solutions_module_dir, "mod.rs"
    )

    try:
        with open(module_declaration_file_path, "w") as mod_dec_file:
            for name in module_names:
                mod_dec_file.write(f"pub mod {name};{os.linesep}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # if len(sys.argv) != 3:
    #     print(f"Usage: python {__file__} <file_path> <module_name>")
    #     sys.exit(1)

    # file_path = sys.argv[1]
    # module_name = sys.argv[2]
    # declaration_line = f"{os.linesep}pub mod {module_name};{os.linesep}"

    # try:
    #     with open(file_path, "a") as f:
    #         f.write(declaration_line)
    #     print(f"Appended {module_name} module declaration to {file_path}")
    # except Exception as e:
    #     print(f"Error: {e}")
    #     sys.exit(1)
