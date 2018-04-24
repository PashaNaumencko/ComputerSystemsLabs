def print_number(number):
    result = ""
    for i in range(0, 5):
        result = "_%4s" % format(number & 15, 'b') + result
        number = number >> 4
    result = "|%3s" % format(number & 7, 'b') + result
    number = number >> 3
    result = "_%4s" % format(number & 15, 'b') + result
    number = number >> 4
    result = "|%4s" % format(number & 15, 'b') + result
    number = number >> 4
    result = "%s" % format(number, 'b') + result
    print(result)


def multiplication(first_num, second_num):
    if (first_num >> 23) & 255 == 0 or (second_num >> 23) & 255 == 0:
        return 0
    result = ((first_num >> 31) ^ (second_num >> 31)) << 31
    print("Sign: ", (first_num >> 31), " xor ", (second_num >> 31), " = ", ((first_num >> 31) ^ (second_num >> 31)))
    m1 = first_num & 8388607
    m2 = second_num & 8388607
    mantissa = (1.0 + m1 / 8388608) * (1.0 + m2 / 8388608)
    print("mantissa = 1.%s" % format(m1, 'b'), "* 1.%s" % format(m2, 'b'))
    shift = 0
    while mantissa >= 2:
        shift += 1
        mantissa /= 2
    mantissa = ((mantissa - 1) * 8388608) // 1
    result += int(mantissa)
    print("Normalize mantissa: 1.%s" % format(int(mantissa), 'b'), ", shift: ", shift)
    e1 = (first_num >> 23) & 255
    e2 = (second_num >> 23) & 255
    exponent = (e1 - 127) + (e2 - 127) + shift + 127
    result += exponent << 23
    print("Exponent: (%s - 1111111)" % format(e1, 'b'), " + (%s - 1111111)" % format(e2, 'b'),
          " + %s" % format(shift, 'b'), " + 1111111")
    return result
