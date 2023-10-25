def prompt_int(prompt_text, min_val, max_val):
    out = input(prompt_text)

    while not out.isnumeric():
        print("Ogiltigt värde. Vänligen välj ett tal")
        out = input(prompt_text)

    return validate_int(int(out), min_val, max_val)


def validate_int(num, min_val, max_val):
    # Begränsar värdet till ett värde mellan 1-99
    return max(min_val, min(max_val, num))
