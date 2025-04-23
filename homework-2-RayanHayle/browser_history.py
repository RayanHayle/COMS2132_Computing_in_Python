class BrowserHistory:
    #credits for yt videos i watched for helped/influence:
    #credit1: https://www.youtube.com/watch?v=ea8UCWNCUdM
    #credit2: https://www.youtube.com/watch?v=pvj8WQMPlGY&t=495s
    #credit3: https://www.youtube.com/watch?v=25AhZTeKF4w
    #credit4: https://www.youtube.com/watch?v=txnejI7LHPg 

    def __init__(self):
        self.history = []  #stack append
        self.forward_stack = []   #stack pointer to top always 
        self.current_index = -1  # stack pointer to 1 item below the top 

    def visit(self, url): #o(1) appending to the top
        self.history.append(url) # top 
        self.forward_stack = []  # Clear forward stack, first theres no visited urls
        self.current_index = len(self.history) - 1 

    def back(self): # 0(1) moving down 1 index
        if self.current_index > 0:
            self.forward_stack.append(self.history[self.current_index])  #append the current url b/c top is empty 
            self.current_index -= 1 # move down the stack each time 
            return self.history[self.current_index] 
        return None  

    def forward(self): # o(1) moving up 1 index 
        if self.forward_stack:
            self.history.append(self.forward_stack.pop()) 
            self.current_index += 1 #move up the stack each time 
            return self.history[self.current_index]
        return None 

    def recently_visited(self):# o(1) returns item 
        return self.history

if __name__ == "__main__":
  browser = BrowserHistory()
  browser.visit("google.com")
  browser.visit("yahoo.com")
  browser.visit("bing.com")
  print(browser.recently_visited())  # Output: ['google.com', 'yahoo.com', 'bing.com']
  print('Back: ', browser.back())
  print('Back: ',browser.back())
  print('Foward: ',browser.forward())
  print('Foward: ', browser.forward())
  print('Foward: ', browser.forward())





