# import sudokuSolver
from SudokuSolverGui import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc



class Solver(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.edit_board_button.clicked.connect(self.edit_board)
        self.ui.all_solutions_button.clicked.connect(self.all_solutions)
        self.ui.solve_button.clicked.connect(self.solve)

        
    def edit_board(self):
        print("yay")

    def all_solutions(self):
        print("all solutions")
    
    def solve(self):
        print("solve the board")


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = Solver()
    widget.show()

    app.exec_()