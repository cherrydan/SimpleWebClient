from tests.libs.some_resource_client import SomeResourceClient


def main():
    some_client = SomeResourceClient('https://avito.ru')

    print(some_client.get_user_last_action_time(177868588))


if __name__ == '__main__':
    main()
