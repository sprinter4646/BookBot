BOOK_PATH = '/home/oleg/REPOS/Bookbot/book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, page_size: int) -> list[str | int]:
    znaki = ',.!:;?'
    sample_size = page_size
    if len(text) <= page_size + start:
        sample_size = len(text) - start
    else:
        for i in range(page_size + start - 1, start, -1):
            if text[i] in znaki and text[i + 1] not in znaki:
                break
            sample_size -= 1
    return [text[start: start + sample_size], sample_size]


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        text = file.readlines()  # Пишет список построчно
        out_text = ''
        for i in text:
            out_text += i
    str_n = 1
    while out_text:
        book[str_n] = _get_part_text(out_text, 0, PAGE_SIZE)[0].lstrip('    \n')
        str_n += 1
        out_text = out_text[_get_part_text(out_text, 0, PAGE_SIZE)[1]:]
    '''for k, v in book.items():
        print(book[k], sep='\n')'''


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)
