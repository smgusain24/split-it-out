

def validate_name(e, name_error, add_contribution_btn, page):
    name = e.control.value
    if not name[0].isalpha():
        name_error.value = "Name must start with an alphabetic character."
        add_contribution_btn.disabled = True
    elif len(name) < 2 or len(name) > 50:
        name_error.value = "Name must be between 2 and 50 characters."
        add_contribution_btn.disabled = True
    else:
        name_error.value = ""
        add_contribution_btn.disabled = False
    page.update()

def validate_contribution(e, contribution_error, add_contribution_btn, page):
    try:
        contribution_value = float(e.control.value)
        if contribution_value <= 0:
            contribution_error.value = "Contribution must be greater than zero."
            add_contribution_btn.disabled = True
        else:
            contribution_error.value = ""
            add_contribution_btn.disabled = False
    except ValueError:
        contribution_error.value = "Contribution must be a valid float number."
        add_contribution_btn.disabled = True
    page.update()
