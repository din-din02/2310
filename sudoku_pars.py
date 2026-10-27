from sudoku import Sudoku
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

class Sudoku_class():
    def __init__(self):
        self.link = 'https://absite.ru/sudoku/2_7517.html'
        options = Options()
        self.driver = webdriver.Firefox(options=options)
        self.board1 = []
        self.board = []
        self.solution_list = []

    def driv(self):
        self.driver.get(self.link)
        time.sleep(2) 

    def itog(self):
        for i in range(0, 81):
            val = self.driver.find_element(By.ID, f'{i}').text.strip()
            self.board1.append(int(val) if val.isdigit() else None)
        board_size = int(len(self.board1)**0.5) 
        
        for i in range(0, board_size):
            self.board.append(self.board1[board_size*i : board_size*(i+1)])
        return self.board

    def rech(self):
        puzzle = Sudoku(3, 3, board=self.board)
        solution = puzzle.solve()
        solution.show()
        
        for row in solution.board:
            self.solution_list.extend(row)
        return self.solution_list
        
    def close(self):
        self.driver.quit()

    def zapolnit(self):
        actions = ActionChains(self.driver)
        for i in range(0, 81):
            val = self.driver.find_element(By.ID, f'{i}')
            val_0=val.text.strip()

            if not val_0:
                val.click()
                actions.send_keys(str(self.solution_list[i])).perform()
                time.sleep(0.05)

        button=self.driver.find_element(By.XPATH, '//*[@id="b_check"]')
        button.click()


if __name__ == "__main__":
    a = Sudoku_class()
    a.driv()
    a.itog() 
    a.rech()
    a.zapolnit()
    time.sleep(5)            