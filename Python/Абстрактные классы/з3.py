from abc import ABC, abstractmethod


class AbstractDate(ABC):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @abstractmethod
    def format(self):
        pass

    @abstractmethod
    def iso_format(self):
        pass


class USADate(AbstractDate):
    def format(self):
        return f"{self.month:02d}-{self.day:02d}-{self.year}"

    def iso_format(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"


class ItalianDate(AbstractDate):
    def format(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def iso_format(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"


if __name__ == "__main__":
    usa_date = USADate(2025, 12, 23)
    italian_date = ItalianDate(2025, 12, 23)

    print("Американская дата:")
    print(f"format(): {usa_date.format()}")
    print(f"iso_format(): {usa_date.iso_format()}")

    print("\nИтальянская дата:")
    print(f"format(): {italian_date.format()}")
    print(f"iso_format(): {italian_date.iso_format()}")