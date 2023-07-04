class MyStack:
    def __init__(self, size):
        self.container = [None]*size  # You don't want to assign [] to self
        self.top = -1
        self.capacity = size

    def push_stack(self, item):
        if self.top is not (self.capacity-1):
            self.top += 1
            self.container[self.top] = item
        else:
            print("Stack Overflow.")


    def pop_stack(self):
    	# Add your code here
        if(self.top is not -1):
            print(self.container[self.top])
            self.top -= 1
        else:
            print("Stack Underflow")

    def peek_stack(self):
    	# Add your code here
        print(self.container[self.top])
        return


if __name__ == "__main__":
    s = MyStack(5)
    s.push_stack('c')
    s.push_stack('a')
    s.push_stack('t')
    s.push_stack('g')
    s.pop_stack()
    s.pop_stack()
    s.peek_stack()