def give_url(urls):
    add_url = input('Введите ссылку: ')
    short_url = input('Введите сокращенное имя: ')
    urls[short_url] = add_url


def get_url(urls):
    get_url_name = input('Введите название ссылки: ')
    value_name_url = urls.get(get_url_name)
    if value_name_url is None:
        print('Введено неверное значение, повторите попытку', '\n')
        main()
    else:
        print(value_name_url, '\n')


def main():
    urls = {}

    while True:
        print('1 - Добавить ссылку')
        print('2 - Взять ссылку')
        print('3 - Выход')
        int_res = input('Введите значение: ')
        if int_res == "1":
            give_url(urls)
        elif int_res == "2":
            get_url(urls)
        elif int_res == "3":
            exit('Завершение программы.')
            print()
        else:
            print('Введено неверное значение, повторите попытку', '\n')


if __name__ == '__main__':
    main()