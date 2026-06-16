"""Student Branching App — точка входа."""

from profile import show_profile
from subjects import show_subjects
from report import show_report


def main() -> None:
    print("Student Branching App")
    show_profile()
    show_subjects()
    show_report()


if __name__ == "__main__":
    main()
