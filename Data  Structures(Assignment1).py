## Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
def function(list,output,n):
    for i in range(n):
        for j in range(i+1):
            if array[i] + array[j] == given_result:
                print(array[i], array[j])

array=[1,2,3,4,5,6,7,8]
given_result=9

function(array,given_result,len(array))

##Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def reverse(array,n):
    i=0
    j=n-1
    while i < j:
        array[i],array[j]=array[j],array[i]
        i=i+1
        j=j-1
    print(array)
list=[1,2,3,4,5,6,7,8,9]
reverse(list,len(list))

#Q3. Write a program to check if two strings are a rotation of each other?
def isrotation(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        s3=s1+s1
        if s2 in s3:
            return True
        else:
            return False

a="Its Raining Today"
b=" Raining TodayIts"

print(isrotation(a,b))

##Q4. Write a program to print the first non-repeated character from a string?

def isrepeated(w1):
    w3=""
    for i in w1:
        if i not in w3:
            w3=w3+i
    print(w3)
a="shristi"
isrepeated(a) 

##Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
def hanoi(n,A,C,B):
    if n==0:
        return
    hanoi(n-1,A,B,C)
    print("Shift disk", n, "from",A, "to", C)
    hanoi(n-1,B,C,A)
n=3
hanoi(n, "A", "B", "C")

##Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
def isOperator(x):
    if x == "+":
        return True

    if x == "-":
        return True

    if x == "/":
        return True

    if x == "*":
        return True

    return False




def postToPre(post_exp):
    s = []


    length = len(post_exp)
    for i in range(length):
        if (isOperator(post_exp[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()

            temp = post_exp[i] + op2 + op1
            s.append(temp)


        else:
            s.append(post_exp[i])

    ans = ""
    for i in s:
        ans += i
    return ans



if __name__ == "__main__":
    post_exp = "AB+CD-"


    print("Prefix : ", postToPre(post_exp))

##Q7. Write a program to convert prefix expression to infix expression.
def prefixToInfix(prefix):
    stack = []

    
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):


            stack.append(prefix[i])
            i -= 1
        else:


            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1

    return stack.pop()


def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
        def prefixToInfix(prefix):
          stack = []

    
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):


            stack.append(prefix[i])
            i -= 1
        else:


            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1

    return stack.pop()


def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
        def prefixToInfix(prefix):
          stack = []

    
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):


            stack.append(prefix[i])
            i -= 1
        else:


            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1

    return stack.pop()


def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False



if __name__ == "__main__":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))

##Q8. Write a program to check if all the brackets are closed in a given code snippet.
def areBracketsBalanced(expr):
 stack = []


 for char in expr:
  if char in ["(", "{", "["]:


   stack.append(char)
  else:


   if not stack:
    return False
   current_char = stack.pop()
   if current_char == '(':
    if char != ")":
     return False
   if current_char == '{':
    if char != "}":
     return False
   if current_char == '[':
    if char != "]":
     return False
     if stack:
      return False
 return True



if __name__ == "__main__":
 expr = "{()}[]"


 if areBracketsBalanced(expr):
  print("Balanced")
 else:
  print("Not Balanced")

##Q9. Write a program to reverse a stack.
class Stack(object):
    def __init__(self):
        self.item=[]

    def push(self,item):
        self.item.append(item)

    def pop(self):
        if self.item==[]:
            return None
        else:
            return self.item.pop()

    def size(self):
        return len(self.item)


    def isempty(self):
        return self.item==[]

def reverse(str):
    TemStr=" "
    stack=Stack()

    for i in range(len(str)):
        stack.push(str[i])
        
    while not stack.isempty():
        Tem=stack.pop()
        TemStr= TemStr + Tem
    return TemStr

if __name__=="__main__":
    print(reverse("shristi srivastava"))

##Q10. Write a program to find the smallest number using a stack.
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


    def __str__(self):
        return "Node({})".format(self.value)


    __repr__ = __str__


class Stack:

    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top {} \n\nStack :\n{}'.format(self.top, out))
    
    __repr__ = __str__


    def getMin(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element in the stack is: {}".format(self.minimum))
    
    def isEmpty(self):

        if self.top == None:
            return True
        else:

            return False
    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count += 1
        return self.count

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            if self.top.value < self.minimum:
                print("Top Most Element is: {}".format(self.minimum))
            else:
                print("Top Most Element is: {}".format(self.top.value))
    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value
            if value < self.minimum:
             temp = (2 * value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted: {}".format(value))
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                print("Top Most Element Removed :{} ".format(self.minimum))
                self.minimum = ((2 * self.minimum) - removedNode)
            else:
                print("Top Most Element Removed : {}".format(removedNode))
stack = Stack()


stack.getMin()
stack.push(2)
stack.push(1)
stack.getMin()
stack.pop()
stack.getMin()
stack.pop()
stack.peek()


    
            
    





