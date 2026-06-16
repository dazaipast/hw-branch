"""Student Branching App — точка входа."""

from profile import show_profile
from subjects import show_subjects


def main() -> None:
    print("Student Branching App")
    show_profile()
    show_subjects()


if __name__ == "__main__":
    main()
