class Jewelry(object):
    def __init__(self):
        #Public attributes to access by variables from MainHandler.
        self.jewelry = ''
        self.quantity = 0
        self.price = 0
        self.email = 0
        self.question = ''
        self.__total = 0 #Private attribute
        self.message = ''

    #getter and setter that gives the access to the total
    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, new_total):
        self.__total = new_total

#This assign functions to reuse data.
class Jewels(object):
    def __init__(self):
        self.__question = ''
        self.__message = ''
        self.__total = 0

    #getter and setter that gives the access to the first message
    @property
    def question(self):
        return self.__question

    @question.setter
    def question(self, new_question):
        self.__question = new_question

    #function to return message
    def question_answer(self):
        self.__question = 'Did find something you like? If not be sure to leave your email.'
        return self.__question

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, new_total):
        self.__total = new_total

    #returns the result of price * quantity that was entered by user
    def total_price(self, price, quantity):
        self.__total = int(price) * int(quantity)
        return self.__total

    #getter gives the access to read message
    @property
    def message(self):
        return self.__message
    #setter gives access to update the second message attribute
    @message.setter
    def message(self, new_message):
        self.__message = new_message

    ##function to return message after input data in the view.
    def messages(self):
        self.__message = 'Thank you for shopping with us!'
        return self.__message