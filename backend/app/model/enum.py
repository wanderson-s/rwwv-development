import enum


class EnumEmploymentType(enum.Enum):
    manager = "manager"
    analyst = "analyst"
    director = "director"


class EnumMonthType(enum.Enum):
    income = "income"
    expenditure = "expenditure"


class EnumMonths(enum.Enum):
    january = 1
    february = 2
    march = 3
    april = 4
    may = 5
    june = 6
    july = 7
    august = 8
    september = 9
    october = 10
    november = 11
    december = 12


class EnumBudgetStatus(enum.Enum):
    draft = "draft"
    approve = "approve"
    refused = "refused"
    remake = "remake"
    approved = "approved"
