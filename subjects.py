"""Предметы и оценки."""


def list_subjects() -> list[str]:
    return ["Git", "Python", "Алгоритмы"]


def show_subjects() -> None:
    print("Предметы:")
    for subject in list_subjects():
        print(f"  - {subject}")
