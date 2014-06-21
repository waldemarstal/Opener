#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import webbrowser


class Opener(object):
    def __init__(self, browser, file_name, start, count):
        self.file = ''
        self.browser = browser
        self.file_name = file_name
        self.start = int(start) - 1
        self.count = int(count)
        self.url = 'www.google.pl/#q='
        self.lines = []
        self.browsers = dict(
            firefox='firefox',
            chrome='google-chrome',
            opera='opera',
            windows_default='windows-default',
            safari='safari'
        )

    def run(self):
        self.open_file()
        self.check_content()
        self.run_iteration()

    def check_content(self):
        size = len(self.lines)
        if not size:
            raise Exception('Empty file!')
        if size < (self.start + 1):
            raise Exception(
                'File have only %s lines! choose another start' % size)
        if self.start < 0:
            raise Exception('start must be greater than 0')
        if self.count <= 0:
            raise Exception('You can not open such an amount.')
        if not self.browsers.get(self.browser):
            raise Exception(
                'Your choice is not available. Choose a different browser.')

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
        curr_choice = self.browsers.get(self.browser)
        try:
            webbrowser.get(curr_choice).open_new_tab(self.url + line[3:-1])
        except Exception as e:
            print 'You have a problem with your browser.\n%s' % e


def main():
    args = sys.argv
    if len(args) != 5:
        print 'Incorrect number of arguments! Try again.'
        print 'python main.py browser file_name start count'
        sys.exit(0)
    browser, file_name, start, count = args[1], args[2], args[3], args[4]
    try:
        opener = Opener(browser, file_name, start, count)
        opener.run()
    except Exception as e:
        print e


if __name__ == '__main__':
    main()