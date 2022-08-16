from importlib.resources import path
from letters import Letters
import random
list_random = [Letters.lower_case_letters,Letters.digits,Letters.upper_case_letters,Letters.special_letters]

class CreatePassword():
    
    def generator(self,length,path):
        password = ""
        while len(password) < length:
            for i in range(1):
                choice = random.choice(list_random)
                letter = random.choice(choice)
                password += letter
        with open(path,"a",encoding="utf-8") as file:
            file.write(password+"\n")