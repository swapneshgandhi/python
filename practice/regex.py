import re

__author__ = 'swaps_000'


def main():
    str = 'purple alice-b@google.com monkey dishwasher'
    line = '172.16.0.3 - - [25/Sep/2002:14:04:19 +0200] ' \
           '"GET / HTTP/1.1" 401 - "" "Mozilla/5.0 (X11; U;' \
           ' Linux i686; en-US; rv:1.1) Gecko/20020827"'
    linetry = '172.16.0.3 - - [25/Sep/2002:14:04:19 +0200]'
    regexEx = r'([\w.-]+)@([\w.]+)'

    # print re.search(r'([(\d\.)]+) - - \[(.*?) (.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"',line).groups()

    print re.search(r'([\S]+) - - \[(\S+) (\S+)\] \"(\w+) ([\S \\]+) (\S+) (\d+) - \"\" \"[\S ]+', line).groups()


if __name__ == '__main__':
    main()
