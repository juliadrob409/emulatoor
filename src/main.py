import os
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
    return True


def run():
    print("Эмулятор UNIX-подобной оболочки")
    print("Доступные команды: ls, cd, exit")

    while True:
        line = input(f"{VFS_NAME}$ ")
        command, args = parse_command(line)

        if command is None:
            print("Ошибка: команда не введена.")
            continue

        if not execute_command(command, args):
            print("Завершение работы.")
            break


if __name__ == "__main__":
    run()
