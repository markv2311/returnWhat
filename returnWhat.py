def add (answer):
    sum = 0
    if type(answer) == list:
        def sumList(sum, answer): 
            for i in answer:
                sum += answer[i]
            return sum 
        sumList(sum, answer)
  
answer = input("What would you like to enter? ")
add(answer)