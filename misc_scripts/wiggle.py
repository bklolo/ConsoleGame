import time

def print_list(char_list):
    print("".join(char_list), end="\r")

def move_a(char_list, steps):
    for _ in range(abs(steps)):
        if steps > 0:
            char_list.pop()
            char_list.insert(0, ' ')
        else:
            char_list.pop(0)
            char_list.append(' ')
        print_list(char_list)
        time.sleep(1)

def main():
    list_length = 20
    initial_char = '!'
    char_list = [initial_char] * (list_length)

    print_list(char_list)

    try:
        while True:
            move_a(char_list, 2)
            move_a(char_list, -2)
    except KeyboardInterrupt:
        print("\nProgram terminated.")

if __name__ == "__main__":
    main()

