class ApiAi(object):
    def __init__(self):
        self.name = "An api for ai and machine learning!!!"

    def introduce(self):
        print(self.name)
        return self.name


if __name__ == '__main__':
    stock_ai = ApiAi()
    stock_ai.introduce()
    
