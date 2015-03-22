from cmd2 import Cmd
 
__version__ = '0.1'
 
class Application(Cmd):
    """
   The main Application class
 
   """
 
    def __init__(self):
        Cmd.__init__(self)
 
    def do_hello(self, line):
        print "Hello:", line
 
if __name__ == '__main__':
    app = Application()
    app.cmdloop()
