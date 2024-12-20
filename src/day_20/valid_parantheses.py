"""
Challenge 20

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Running in main():
The string [()[]] is valid: True
"""

class ValidParantheses:
    def isValid(self, input_str: str) -> bool:
        """ Determine if the input string is valid """
        stack = []
        parantheses_dict = {')': '(', '}': '{', ']': '['}

        for paranthesis in input_str:
            if paranthesis in parantheses_dict:
                top_element = stack.pop() if stack else '-'
                if parantheses_dict[paranthesis] != top_element:
                    return False
            else:
                stack.append(paranthesis)

        if len(stack) == 0:
            return True

        return False

if __name__ == "__main__":
    validParantheses = ValidParantheses()
    test_str = "["
    res = validParantheses.isValid(test_str)
    print(f"The string {test_str} is valid: {res}")
