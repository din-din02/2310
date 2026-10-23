from sudoku import Sudoku
import time
import selenium
import os
import random
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import pandas as pd


class Sudoku_class():
    def __init__(self):
        self.link='https://absite.ru/sudoku/2_7517.html'
        options = Options()
        self.driver = webdriver.Firefox(options=options)

    def driv(self):
        driver=self.driver
        driver.get(self.link)

    def itog(self):
        board1=[]
        board = []
        for i in range (0, 81):
            board1.append(self.driver.find_element(By.ID, f'{i}').text)
        board_size=int(len(board)**0.5)
        for i in range(0, board_size):
            board.append(board1[board_size*i:board_size*(i+1)])
        return board

    def rech(self,board):
        puzzle = Sudoku(3, 3, board=board)
        solution = puzzle.solve()
        solution.show()


if __name__ == "__main__":
    a=Sudoku_class()
    a.driv()
    a.itog()
    a.rech()