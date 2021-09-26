# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from argparse import ArgumentParser


from entities.user import User
from generator.user_generator import UserGenerator
from producer.user_producer import UserProducer


def parse_command_line_args():
    arg_parser = ArgumentParser()

    arg_parser.add_argument("--topic", required=False, default='camp-users', help="Topic name")
    arg_parser.add_argument("--bootstrap-servers", required=False, default="localhost:9092", help="Bootstrap server address")
    arg_parser.add_argument("--schema-registry", required=False, default="http://localhost:8081", help="Scema registry url")
    arg_parser.add_argument("--schema-file", required=False, default="create user request.avsc",  help="File name of Avro to use")

    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_command_line_args()
    user_producer = UserProducer(args)
    user = User.generate_random_user()
    for users in UserGenerator.generate():
        user_producer.send_records(users)




