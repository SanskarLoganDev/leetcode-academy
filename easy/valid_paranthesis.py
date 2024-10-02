def isValid(s):
    bracket_relation = {'(':')','[':']','{':'}'}
    bracket_list = [] # stack
    for bracket in s:
        if bracket in bracket_relation.keys():
            bracket_list.append(bracket)
        elif bracket in bracket_relation.values():
            if not bracket_list:
                return False # checking if closing bracket found in string when stack is empty
            if bracket!= bracket_relation[bracket_list[-1]]:
                return False
            bracket_list.pop()
    if len(bracket_list)==0:
        return True
    else:
        return False

print(isValid("()}[]"))