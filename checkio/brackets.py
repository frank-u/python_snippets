"""
    Дано выражение с цифрами, скобками и операторами. В данной задаче важны
только скобки. Скобки представлены в трех вариациях: "{}" "()" и "[]". Скобки
используются, чтобы определить порядок применения операторов или ограничить
участок выражения. Если скобка открывается, то она должна закрываться скобкой
того же типа. Участки ограниченные одной парой скобок, не должны пересекаться с
участками других скобок. В этой задаче, вам необходимо определить правильное ли
выражение или нет, основываясь на расположении скобок. И не обращайте внимание
на операторы и операнды.
    Входные данные: Выражение для проверки, как строка (str, unicode).
    Выходные данные: Решение, правильное выражение или нет, как булево значение
(True или False).
    Предусловия:
        Выражение содержит только скобки ("{}" "()" or "[]"), цифры и/или
операторы ("+" "-" "*" "/").
        0 < len(expression) < 103
"""


def checkio(expression):
    brackets_stack = []
    br = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    for i in expression:
        if i in br.values():
            brackets_stack.append(i)
        elif i in br:
            try:
                if brackets_stack.pop() is not br[i]:
                    return False
            except IndexError:
                return False
    if brackets_stack:
        return False
    return True

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    assert checkio("(((1+(1+1))))]") == False, "pop from empty list"
