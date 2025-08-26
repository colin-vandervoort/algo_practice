if __name__ == "__main__":
    import pytest
    import os

    solutions_dir = os.path.join(os.path.dirname(__file__), "..", "solutions")
    solutions_dir = os.path.abspath(solutions_dir)

    pytest.main([solutions_dir])
