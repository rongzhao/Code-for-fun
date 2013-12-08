"""This program is to create a very simple in-memory database, which has a very limited command set"""
class database:
    def __init__(self):
        self.variable = {}#dictionary that stores all variables
        self.value_count = {}#Create an index based on value
        self.initial_screenshot = {}#Initial status for the blocks
        self.block_num = 0#The latest block number

    #function to set variable
    def set_var(self, name, value):
        if self.block_num > 0:
            sub_status = self.initial_screenshot.setdefault(self.block_num, {})
            if name not in sub_status:
                if name in self.variable:
                    sub_status[name] = self.variable[name]
                else:
                    sub_status[name] = None
        if name in self.variable:
            original_value = self.variable[name]
            self.value_count[original_value] -= 1 
        self.variable[name] = value
        if value not in self.value_count:
            self.value_count[value] = 0
        self.value_count[value] +=  1

    #function to get variable value
    def get(self, name):
        if name in self.variable:
            print self.variable[name]
        else:
            print 'NULL'

    #function to unset a variable
    def unset(self, name):
        if self.block_num > 0:
            sub_status = self.initial_screenshot.setdefault(self.block_num, {})
            if name not in sub_status:
                if name in self.variable:
                    sub_status[name] = self.variable[name]
        if name in self.variable:
            self.value_count[self.variable[name]] = self.value_count[self.variable[name]] - 1
            if self.value_count[self.variable[name]] == 0:
                del self.value_count[self.variable[name]]
            del self.variable[name]
    
    #function to return the number of variables equal to a given value
    def num_equal_to(self, value):
        num = 0
        if value in self.value_count:
            num = self.value_count[value]
        print num

    #function to start a transactional block
    def begin_block(self):
        self.block_num += 1

    #function to rollback all the commands from the most recent block
    def rollback(self):
        if self.block_num == 0:
            print 'NO TRANSACTION'
        elif self.block_num in self.initial_screenshot:
            sub_status = self.initial_screenshot[self.block_num]
            for name in sub_status:
                if sub_status[name] == None:
                    self.unset(name)
                else:
                    self.set_var(name, sub_status[name])
            del self.initial_screenshot[self.block_num]
            self.block_num -= 1
        else:
            self.block_num -= 1

    #function to commit all the commands from all the blocks
    def commit(self):
        if self.block_num == 0:
            print 'NO TRANSACTION'
        else:
            self.block_num = 0
            self.initial_screenshot.clear()
    
    #function to run the database
    def run(self):
        while True:
            try:
                command = raw_input()
                ls = command.split()
                function_type = ls[0].upper()
                if function_type == 'SET':
                    self.set_var(ls[1], ls[2])
                elif function_type == 'GET':
                    self.get(ls[1])
                elif function_type == 'UNSET':
                    self.unset(ls[1])
                elif function_type == 'NUMEQUALTO':
                    self.num_equal_to(ls[1])
                elif function_type == 'BEGIN':
                    self.begin_block()
                elif function_type == 'ROLLBACK':
                    self.rollback()
                elif function_type == 'COMMIT':
                    self.commit()
                elif function_type == 'END':
                    break
                elif function_type == 'HELP':
                    self.get_help()
                else:
                    self.print_error()
            except IndexError:
                print "Number of input parameters does not match!"
    
    #function to print error message
    def print_error(self):
        print "Not a valid command:(  Please type HELP for help"

    #function to print help messages
    def get_help(self):
        print "============================================================="
        print "SET [name] [value]: \nSet a variable [name] to the value [value]. Neither variable names nor values will ever contain spaces"
        print
        print "GET [name]: \nPrint out the value stored under the variable [name]. Print NULL if that variable name hasn't been set."
        print
        print "UNSET [name]: \nUnset the variable [name]"
        print
        print "NUMEQUALTO [value]: \nReturn the number of variables equal to [value]. If no values are equal, this should output 0"
        print
        print "END: \nExit the program"
        print
        print "BEGIN: \nOpen a transactional block"
        print
        print "ROLLBACK: \nRollback all of the commands from the most recent transactional block"
        print
        print "COMMIT: \nPermanently store all of the operations from all presently open transactional blocks"
        print "=============================================================="
        print 


def main():
    db = database()
    print "Welcome to my database!"
    print "Type HELP to get started!"
    db.run()

if __name__ == '__main__':
    main()



