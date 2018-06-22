from __future__ import print_function
from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)


@magics_class
class Vidette(Magics):

    def __init__(self, shell, data):
        # You must call the parent constructor
        super(Vidette, self).__init__(shell)
        self.ignore_counter = 0
        self.shell = shell
        self.cells = []

    # @line_magic
    # def vidette(self, line):
    #     "my line magic"
    #     print('holla!')
    #     print("Full access to the main IPython object:", self.shell)
    #     print("Variables in the user namespace:", list(self.shell.user_ns.keys()))
    #     return line

    @cell_magic
    def init(self, line, cell):
        "my cell magic"
        # if self.ignore_counter == 0:
        #     self.ignore_counter += 1
        #     self.shell.run_cell(cell)
        # if line not in self.cells:
        self.shell.run_cell(cell)
            # self.cells.append(line)

        # return 'sup', line, cell, self.ignore_counter



    # @line_cell_magic
    # def lcmagic(self, line, cell=None):
    #     "Magic that works both as %lcmagic and as %%lcmagic"
    #     if cell is None:
    #         print("Called as line magic")
    #         return line
    #     else:
    #         print("Called as cell magic")
    #         return line, cell

