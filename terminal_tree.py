import argparse
import os
import random
import time

BALL = '⏺'
COLOR = {
    'blue': '\033[94m',
    'yellow': '\033[93m',
    'cyan': '\033[96m',
    'green': '\033[92m',
    'magenta': '\033[95m',
    'white': '\033[97m',
    'red': '\033[91m'
}
STAR = '★'


def random_change_char(string, value):
    indexes = random.sample(range(0, len(string)), value)
    string = list(string)
    for idx in indexes:
        if string[idx] != ' ' and string[idx] == '_':
            string[idx] = BALL
    return ''.join(string)


def tree(height=13, screen_width=80):
    star = (STAR, 3 * STAR)
    if height % 2 != 0:
        height += 1
    body = ['/_\\', '/_\\_\\']
    trunk = '[___]'
    begin = '/'
    end = '\\'
    pattern = '_/'
    j = 5
    for i in range(7, height + 1, 2):
        middle = pattern + (i - j) * pattern
        line = ''.join([begin, middle[:-1], end])
        body.append(line)
        middle = middle.replace('/', '\\')
        line = ''.join([begin, middle[:-1], end])
        body.append(line)
        j += 1

    return [line.center(screen_width) for line in (*star, *body, trunk)]


def balls(tree):
    for idx, _ in enumerate(tree[:-3], 2):
        tree[idx] = random_change_char(tree[idx], len(tree[idx]) // 8)
    return tree


def colored_stars_balls(tree):
    for idx, _ in enumerate(tree):
        string = list(tree[idx])
        for pos, _ in enumerate(string):
            if string[pos] == STAR:
                string[pos] = ''.join([COLOR['yellow'], STAR, '\033[0m'])
            elif string[pos] == BALL:
                string[pos] = ''.join([random.choice(list(COLOR.values())), BALL, '\033[0m'])
        tree[idx] = ''.join(string)
    return tree


def cli():
    parser = argparse.ArgumentParser(prog="Python Christmas Tree by Chico Lucio from Ciencia Programada",
                                     epilog="Ctrl-C interrupts the Christmas :-(")

    # Removed size and width arguments since we will use terminal size
    args = parser.parse_args()

    # Get terminal size
    screen_width, height = os.get_terminal_size()
    
    # Set height to a minimum of 5
    height = max(5, height - 2)  # Subtracting 2 to account for terminal borders

    # Hide cursor
    print("\033[?25l", end='')

    try:
        while True:
            time.sleep(random.uniform(.1, 1))
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n'.join(colored_stars_balls(balls(tree(height, screen_width)))))
    
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{'Merry Christmas!!':^{screen_width}}", end='\n\n')
    
    finally:
        # Show cursor again before exiting
        print("\033[?25h", end='')


if __name__ == '__main__':
    cli()
