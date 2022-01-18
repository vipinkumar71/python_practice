"""
Basic concepts of object-oriented programming
"""


class InterchangeElements:
    """Class to interchange the first and last element"""

    def __init__(self):
        self.elements = []

    def exchange_element(self):
        temp = self.elements[0]
        self.elements[0] = self.elements[-1]
        self.elements[-1] = temp
        print(f"After exchange:{self.elements}")

    def get_input(self):
        length = int(input("Enter length of list:"))
        for el in range(length):
            self.elements.append(int(input(f"Enter element for {el}th index:")))
        print(f"Before exchange:{self.elements}")


if __name__ == '__main__':
    interchange_elements = InterchangeElements()
    interchange_elements.get_input()
    interchange_elements.exchange_element()
