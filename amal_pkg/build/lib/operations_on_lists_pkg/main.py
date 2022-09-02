import numpy as np

class MyClass(object):
    
    # attributes ---> variables
    # methods ---> functions
    
    # initialization
    # self --> object 
    def __init__(self, list_input):
        self.list_input = list_input

#------------------------------------------------------------------  

    #return max value    
    def return_max(self):
        # we having the user input as a list
        counter = 0
        if (len(self.list_input) == 0):
            return False
        else:
            max_value = self.list_input[0]
    
            for x in self.list_input:

                if (x > max_value):
                    max_value = x
                
                counter += 1
            
            return(max_value)
#------------------------------------------------------------------   

    #return min value    
    def return_min(self):
        # we having the user input as a list
        counter = 0
        if (len(self.list_input) == 0):
            return False
        else:
            min_value = self.list_input[0]
    
            for x in self.list_input:

                if (x < min_value):
                    min_value = x
                
                counter += 1
        
            return(min_value)
#------------------------------------------------------------------          

    #return the max value squared   
    def return_max_squared(self):
        # we having the user input as a list
        counter = 0
        if (len(self.list_input) == 0):
            return False
        else:
            max_value = self.list_input[0]
    
            for x in self.list_input:

                if (x > max_value):
                    max_value = x
                
                counter += 1
            
            return(max_value**2)
#------------------------------------------------------------------ 

    #return the length of the list
    def return_length(self):
        # we having the user input as a list
        
        return(len(self.list_input))      
#------------------------------------------------------------------ 

    #return the sum of all the positive elements    
    def return_positive_sum(self):
        # we having the user input as a list
        counter = 0
        if (len(self.list_input) == 0):
            return False
        else:
            max_value = 0
    
            for x in self.list_input:

                if (x > 0):
                    max_value += x
                
                counter += 1
            
            return(max_value)
#------------------------------------------------------------------  

#return the count of all the negative elements    
    def return_negative_count(self):
        # we having the user input as a list
        counter = 0
        if (len(self.list_input) == 0):
            return False
        else:
            negative_count = 0
    
            for x in self.list_input:

                if (x < 0):
                    negative_count += 1
                

                counter += 1
            
            return(negative_count)
#------------------------------------------------------------------  

#return the average of the list  
    def return_average(self):
        # we having the user input as a list
        counter = 0
        if (len(self.list_input) == 0):
            return False
        else:
            ave = 0
    
            for x in self.list_input:

                ave += x
                
                counter += 1
            
            return(ave/len(self.list_input))
#------------------------------------------------------------------  

#return the reverse of the list    
    def return_reverse_list(self):
    
        counter = 0
    
        for x in self.list_input:
            counter += 1
    
        index_number = 0
        y = 1
    
        for x in self.list_input:
            if (counter%2 == 0):
                while (y <= (counter/2)):
                
                    holder1 = self.list_input[index_number]
                    holder2 = self.list_input[(index_number*(-1)) -1]
                
                    self.list_input[index_number] = holder2
                    self.list_input[(index_number*(-1)) -1] = holder1
                
                    index_number += 1
                    y += 1
            
            else:
                counter -= 1
                while (y <= (counter/2)):
                
                    holder1 = self.list_input[index_number]
                    holder2 = self.list_input[(index_number*(-1)) -1]
                
                    self.list_input[index_number] = holder2
                    self.list_input[(index_number*(-1)) -1] = holder1
                
                    index_number += 1
                    y += 1
            
        return(self.list_input)
if __name__ == "__main__":
    MyClass()