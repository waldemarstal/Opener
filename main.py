#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import webbrowser


class Opener(object):
    def __init__(self, file_name, start, count):
        self.file = ''
        self.file_name = file_name
        self.start = int(start) - 1
        self.count = int(count)
        self.url = 'www.google.pl/#q='
        self.lines = []

    def run(self):
        self.open_file()
        self.check_content()
        self.run_iteration()

    def check_content(self):
        size = len(self.lines)
        if not size:
            raise Exception('Empty file!')
        elif size < (self.start + 1):
            raise Exception(
                'File have only %s lines! choose another start' % size)
        elif self.count <= 0:
            raise Exception('You can not open such an amount.')

    def open_file(self):
        self.file = open(self.file_name, 'r')
        self.lines = self.file.readlines()

    def run_iteration(self):
        curr = 0
        for line in self.lines[self.start:]:
            curr += 1
            if curr > self.count:
                break
            self.open_in_browser(line)

    def open_in_browser(self, line):
        try:
            webbrowser.open_new_tab(self.url + line[3:-1])
        except Exception as e:
            print 'You have a problem with your browser.\n%s' % e
        else:
            webbrowser.get('firefox').open_new_tab(self.url + line[3:-1])


def main():
    args = sys.argv
    if len(args) != 4:
        print 'Incorrect number of arguments! Try again.'
        print 'python main.py file_name start count'
        sys.exit(0)
    file_name, start, count = args[1], args[2], args[3]
    try:
        opener = Opener(file_name, start, count)
        opener.run()
    except Exception as e:
        print e

if __name__ == '__main__':
    main()