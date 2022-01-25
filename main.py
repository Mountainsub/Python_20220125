import sys
import subprocess


def get_lines(cmd):
    '''
    :param cmd: str 実行するコマンド.
    :rtype: generator
    :return: 標準出力 (行毎).
    '''
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    while True:
        line = proc.stdout.readline()
        if line:
            yield line

        if not line and proc.poll() is not None:
            break


if __name__ == '__main__':
    count = 0
    for line in get_lines(cmd=['python', 'request5/request.py','request6/request.py']):
        count += 1
        f = open('file_1.txt', 'w')
        f.write(line.decode("sjis"))
        if count % 10 == 9:
            string = "file_"+ str(count) + ".txt"
            f = open(string, 'w')
            f.write(line.decode("sjis"))
            line = f.read()
            print("出力結果:" + line)
