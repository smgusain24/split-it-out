from splitapp.logic.calculate import calculate_split


def display_result(contributions, result_text, page):
    if contributions:
        transactions = calculate_split(contributions)
        result_text.value = "\n".join(transactions)
    else:
        result_text.value = "No contributions added."
    page.update()
