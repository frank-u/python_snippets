"""
   В области информационных технологий, очередь это структура данных с принципом
доступа к элементам «первый пришёл — первый вышел» (FIFO, First In — First Out).
Добавление элемента (принято обозначать словом "enqueue" — поставить в очередь
или "push") возможно лишь в конец очереди, выборка — только из начала очереди
(что принято называть словом "dequeue" — убрать из очереди или "pop"), при этом
выбранный элемент из очереди удаляется. То есть чтобы добраться до нового добав-
ленного элемента, нам надо "вытащить" элементы, которые были добавлены ранее.
 Попробуем сделать модель очереди на Python. Вам дана последовательность команд:

- "PUSH X" -- поставить в очередь X, где X - это буква в верхнем регистре.
- "POP" -- убрать из начала очереди элемент. Если очередь пустая, то это команда
ничего не делает.
Очередь содержит только буквы.

Вам необходимо обработать все команды и собрать все буквы, которые остались в
очереди, в одно слово, от начала до конца очереди.

Рассмотрим пример. Дана последовательность команд:
["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]

Команда 	Очередь 	Примечания
------------------------------------------
PUSH A 	A 	Добавили "A" в пустую очередь
POP 		Убрали "A"
POP 		Очередь уже пуста
PUSH Z 	Z
PUSH D 	ZD
PUSH O 	ZDO
POP 	DO
PUSH T 	DOT 	Результат

    Входные данные: Последовательность команд, как список (list) строк (str).
    Выходные данные: Содержание очереди, как строка (str).
"""
import re


def letter_queue(commands):
    stack = []
    match_re = re.compile("(POP|PUSH)(?:(?:\Z)|(?:\s([A-Z]{1})\Z))")
    for command in commands:
        match_obj = match_re.match(command)
        if match_obj:
            if match_obj.group(1) == 'PUSH':
                stack.append(match_obj.group(2))
            elif match_obj.group(1) == 'POP':
                if stack:
                    stack.pop(0)
    return "".join(stack)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(
        ["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP",
         "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
