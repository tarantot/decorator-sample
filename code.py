
def my_decorator(func):
    def wrapper(text):
        decor, i_1, i_2, j = list(text), 0, 0, 0
        
        while i_1 in range(len(decor)):
            i_1 += 1
        print('+-' * i_1, end='+\n')

        while j in range(len(decor) + 1):
            decor.insert(j, '|')
            j += 2
        print(''.join(decor))

        while i_2 in range(len(text)):
            i_2 += 1
        print('+-' * i_2, end='+\n')

    return wrapper


@my_decorator
class Text:

    def __init__(self, text):
        self.text = text

    def res(self):
        return self.text


text = Text(input('Введите текст: '))
