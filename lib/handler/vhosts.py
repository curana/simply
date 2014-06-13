import lib.tasks as tasks
import lib.cli as cli

class Vhosts(tasks.Tasks):

  HDL_EXIT    = 0
  HDL_CREATE  = 1
  HDL_REMOVE  = 2
  HDL_DISABLE = 3
  HDL_ENABLE  = 4

  menu = { HDL_EXIT:    '<< Go Back',
           HDL_CREATE:  'Create virtual Host',
           HDL_REMOVE:  'Remove virtual Host',
           HDL_DISABLE: 'Disable virtual Host',
           HDL_ENABLE:  'Enable virtual Host' }

  def __init__(self):
    self.hostname = ''
    self.username = ''
    self.enable   = False
    self.path     = '/www/vhosts/'

  def create(self):
    self.get_input()
    self.apply_changes()

  def get_input(self):
    ask = "Hostname"
    self.hostname = cli.get_raw_input(ask, True)

    ask = "Username"
    self.username = cli.get_raw_input(ask, True, self.hostname)

    ask = "Enable it?"
    self.enable   = cli.get_raw_input(ask, True, 'n', ['y', 'n'])

    ask = "Path"
    self.path     = cli.get_raw_input(ask, True, '/www/vhosts/' + self.hostname)

  def validate_input(self):
    pass

  def apply_changes(self):
    print self.hostname, self.username, self.enable, self.path
    print("%s is being created...done" % self.hostname)
    return False