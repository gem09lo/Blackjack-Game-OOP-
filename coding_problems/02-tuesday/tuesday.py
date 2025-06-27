def multi_table(number: int) -> str:
    multiplication_table = []

    for i in range(1, 11):
        multiplication_table.append(f"{i} * {number} = {number * i}")
    return "\n".join(multiplication_table)


print(multi_table(5))
