

def calculate_split(contributions):
    n = len(contributions)
    total_expense = sum(contributions.values())
    equal_share = total_expense / n
    balances = {person: contributions[person] - equal_share for person in contributions}

    owes = []
    owed = []

    for person, balance in balances.items():
        if balance < 0:
            owes.append((person, -balance))
        elif balance > 0:
            owed.append((person, balance))

    transactions = []
    i, j = 0, 0
    while i < len(owes) and j < len(owed):
        owe_person, owe_amount = owes[i]
        owed_person, owed_amount = owed[j]
        payment = min(owe_amount, owed_amount)
        transactions.append(f"{owe_person} pays {owed_person} {payment:.2f}")
        owes[i] = (owe_person, owe_amount - payment)
        owed[j] = (owed_person, owed_amount - payment)
        if owes[i][1] == 0:
            i += 1
        if owed[j][1] == 0:
            j += 1

    return transactions
