class A(object):
    def __init__(self, arg1):
        self.arg1 = arg1
        print("Initialized")

def exec_command(module, command):
    connection = A(module)
    out = connection.exec_command(command)

exec_command('obj','show nanner')
