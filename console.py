#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        '''<Quit> Command To Exit The Program'''
        return True

    def do_EOF(self, args):
        '''Handles end of file'''
        return True

    def emptyline(self):
        '''dont execute anything when the user
           presses enter on an empty line
        '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

