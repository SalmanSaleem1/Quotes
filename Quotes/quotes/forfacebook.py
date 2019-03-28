import facebook

access_token = "EAADXxZAHyXZCwBANZBzxnIErswhAZCOlkABSjEqX01stUO4vrQvmU5DLWDIh31FhRamtYN6dZCnwwqSx4zXwO05jjAErtZCUzx9Q5Rynu4MFxKY9fobOcnBmRyv3PfdgCk2zkjysnUIZApZAbiUDzVVLOWX1EypjEsNY0kJvilKAJWLtD1GyEvF0jfGWLRskcpoZD"

fb = facebook.GraphAPI(access_token=access_token)


def post_image():
    fb.put_photo(open('default.jpg'), album_path='100007885390009/photo')


if __name__ == '__main__':
    post_image()
