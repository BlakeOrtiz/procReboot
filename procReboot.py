import os
import sys
import time
import subprocess


def watchProcess(path='', counter=0, ran=False):
    delimiter = '\\'

    name = path.rsplit(delimiter)
    name = name[-1]

    if not ran:
        if path == '' or name == '':
            path = input("Enter Full Path to Process to monitor (Ex: C:\\folder\\process.exe):\n")

            name = path.rsplit(delimiter)
            name = name[-1]

        if '.exe' not in name or not os.path.isfile(path):
            if counter >= 2:
                raise Exception("Look, ya dingus. The file either doesn't exist OR you're inputting an invalid path... Fix ya self!\n"
                                + "Path: {}\n".format(path)
                                + "File: {}\n".format(str(name)))
            else:
                counter += 1
                watchProcess(counter=counter)

    print("\n\n=== Watching \"{}\" ===".format(str(name)))

    while not os.system('TASKLIST | FINDSTR /I {}'.format(name)):
        time.sleep(15)
        continue

    print("[X] Process \"{}\" is down! Restarting...".format(name))

    time.sleep(3)

    runProcess(path, name)


def runProcess(path, name):
    os.popen("\"{}\"".format(path))

    print("Starting \"{}\"...\n\n".format(name))

    time.sleep(5)

    watchProcess(path, ran=True)


if __name__ == '__main__':
    try:
        passed_arg = sys.argv[1]
    except IndexError:
        passed_arg = ''

    if passed_arg == '':
        watchProcess()
    else:
        watchProcess(passed_arg)

