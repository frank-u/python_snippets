"""
    Наш калькулятор свихнулся на цензуре и отказывается использовать некоторые
слова. Вам необходимо обмануть его и написать программу для для суммирования
чисел.
    Дан массив чисел, необходимо найти сумму этих чисел. Ваше решение не должно
содержать запрещенные слова, даже как часть слов.
    Список запретных слов:
        sum
        import
        for
        while
        reduce

    Входные данные: Массив, как список (list) целых чисел (int).
    Выходные данные: Сумма чисел, как целое число (int).
    Предусловия: Тут нет больших чисел.
"""


# mine
def checkio(data):
    if len(data) == 1:
        return data[0]
    else:
        data[1] += data[0]
        result = checkio(data[1:])
    return result


# better solution right recursion:
def checkio_better(data):
    if not data:
        return 0
    return data[0] + checkio(data[1:])


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]  # sum is 15
    res = checkio_better(data)
    print("Summ: {0}.".format(res))