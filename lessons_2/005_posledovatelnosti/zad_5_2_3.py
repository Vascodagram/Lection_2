def main():
    list_words = input('Напишите текст:').split(' ')
    adc_list_words = sorted(list_words)
    for i in adc_list_words:
        print(i)


if __name__ == '__main__':
    main()