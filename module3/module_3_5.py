def get_multiplied_digits(number):
    str_ = str(number)
    first_digit = int(str_[0])
    if len(str_) <= 1:
        return first_digit
    return first_digit * get_multiplied_digits(int(str_[1:]))


print(get_multiplied_digits(40203))
