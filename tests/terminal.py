import subprocess


def qqq():
    return subprocess.run(
        args="whereis wine".split(" "),
        stdout=subprocess.PIPE,
    )

print(qqq().stdout.decode())