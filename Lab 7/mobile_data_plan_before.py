"""Original Lab 7 mobile data plan processor, preserved for fuzz reproduction."""


def parse_plan(text):
    plan, gb = text.split(":")
    return plan.strip().title(), float(gb)


def usage_average(usage_csv):
    values = [int(value) for value in usage_csv.split(",")]
    return sum(values) // len(values)


def payable_bill(text):
    bill, discount = text.split("|")
    total = float(bill) * 1.18 - float(discount)
    return max(total, 0)


def main():
    print("==== Running parse_plan ====")
    print("Plan and Data:", parse_plan(input("Enter plan:data in GB (e.g. standard:5): ")))
    print("\n==== Running usage_average ====")
    print("Average Usage:", usage_average(input("Enter daily usage in MB as CSV (e.g. 300,450,800): ")))
    print("\n==== Running payable_bill ====")
    print("Payable Bill:", payable_bill(input("Enter bill|discount (e.g. 399|50): ")))


if __name__ == "__main__":
    main()
