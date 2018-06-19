def count_char(words):
    letters = {}
    for l in words:
        letters[l] = words.count(l)
    for result in sorted(letters):
        print(result + ':' + str(letters[result]))


def main():
    count_char('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ac'
    'cumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praes'
    'ent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit met'
    'us, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volu'
    'tpat eget massa. Donec nec velit non ligula efficitur luctus.')


if __name__ == '__main__':
    main()
