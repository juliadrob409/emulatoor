import os
import sys

VFS_NAME = "VFS"


def parse_command(line):
    parts = line.split()

    if not parts:
        return None, []

    for i in range(len(parts)):
        if parts[i].startswith("$"):
            var = parts[i][1:]
            parts[i] = os.environ.get(var, parts[i])

    expanded_parts = [os.path.expandvars(part) for part in parts]

    return expanded_parts[0], expanded_parts[1:]


def execute_command(command, args):
    if command == "ls":
        print("ls", *args)
        return True

    if command == "cd":
        print("cd", *args)
        return True

    if command == "exit":
        if args:
            print("Ошибка: команда exit не принимает аргументы.")
            return True
        return False

    print(f"Ошибка: неизвестная команда '{command}'.")
    return False


def run():
    if len(sys.argv) != 3:
        print("Ошибка: необходимо указать путь к VFS и путь к стартовому скрипту.")
        return

    vfs_path = sys.argv[1]
    script_path = sys.argv[2]

    print("Параметры запуска:")
    print("Путь к VFS:", vfs_path)
    print("Путь к стартовому скрипту:", script_path)

    print()
    print("Эмулятор UNIX-подобной оболочки")
    print("Доступные команды: ls, cd, exit")

    if not os.path.exists(script_path):
        print("Ошибка: стартовый скрипт не найден.")
        return

    with open(script_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            print(f"{VFS_NAME}$ {line}")

            command, args = parse_command(line)

            if command is None:
                print("Ошибка: команда не введена.")
                continue

            if not execute_command(command, args):
                print("Завершение работы.")
                break


if __name__ == "__main__":
    run()