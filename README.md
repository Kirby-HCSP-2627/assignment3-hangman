# Assignment #1

### INSTALL
For this assignment, you won't need to run any commands. 

### Intro
This assignment is for you to practice using arithmetic operators, manipulating strings, and defining functions. 

### Relevant Info 
Remember, python is zero based. Meaning the first character of every string is 0, second is 1, third is 2 and so on. <br/>
len(str) returns the length of the the string. Ex. len("Hello") = 4, len("Hihowareyou") = 11 <br/>
str.upper() and str.lower() returns the string all capitalized or all lower case respectively. Ex. "h".upper() -> "H", "D".lower() -> "d"
#### Type-Casting
Often times you will find yourself in a place where you need to convert a string to an integer or float, or vice-versa. You can force python to change a variables type. This is called type casting. Below are some common examples: <br/>
score= 99 <br/>
print("Your score is " + str(99)) <br/><br/>

test_score_part_a = "24"<br/>
test_score_part_b = "77"<br/>
test_score_total = int(test_score_part_a) + int(test_score_part_b)<br/><br/>

You will most commonly be type casting into int(), float(), str(). <br/>
Just be careful when type casting between float and int. When you type cast into integer from a float. You will lose the decimals. Ex. int(45.7) -> 45

### The Program
You will not need to create a file this time around. Open the python file named assignment.py. In the file you will find the questions to answer. Careful to not change the name of this file, I will be running an auto grader!

### Example Output
Check auto-grader tests! 

### Testing
This assignment does not have extra tests! You will see the auto-grader tests in your GitHub. 

### Submitting 
To submit your project:
1. Open a terminal window in vscode in your project folder
2. run git add file_name.py , replacing it for whatever file you wrote code to
3. run git commit -m "Type your message in between the quotation marks. Your message should only be a couple words long and about what you changed"
4. run git push 
5. Confirm and check your auto-grade (if it's enabled) on your GitHub account, might take ~1 or 2 minutes to update on GitHub website
