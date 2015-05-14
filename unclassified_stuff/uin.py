"""
  Created on 20.11.2012
  @author: Oleksandr Poliatykin

  Script to parse Ukrainian Personal ID numbers.
  Set UIN as first command-line parameter
"""
import sys
from datetime import timedelta, date


def decrypt_ua_id(uin):
    """
        Function that takes identification number and returns dictionary with
    data in human readable format

    :param uin: A valid identification number, must contain 10 digits
    :return: dictionary of key:value pairs for sex, birthday and checksum
    """
    result = dict()

    sex = ["F", "M"]
    result.update(
        {"sex": sex[int(uin[8]) % 2]}
    )
    birthday = str(date(1900, 1, 1) + timedelta(days=(int(uin[:5]) - 1)))
    result.update(
        {"birthday": birthday}
    )

    # polinom_coeffs = [2,4,10,3,5,9,4,6,8]
    polinom_coeffs = [-1, 5, 7, 9, 4, 6, 10, 5, 7]
    uin_nums = map(int, list(uin[:9]))
    # OR sum(map(lambda i,j:i*j, polinom_coeffs, uin_nums))%11
    if sum([i * j for i, j in zip(polinom_coeffs, uin_nums)]) % 11 == int(
            uin[9]):
        checksum_validity = True
    else:
        checksum_validity = False
    result.update({"checksum": checksum_validity})
    return result


if __name__ == '__main__':
    print("UIN: {0}. Parsed: {1}".format(
        sys.argv[1],
        decrypt_ua_id(sys.argv[1]))
    )
