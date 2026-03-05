def tokenize(expression: str) -> list[str]:
    expression = expression.replace(" ","")
    return_list = []
    operator_counter = 1        #track how many operator is before a number.
    for element in expression:
        match element:
            case "+" | "-" | "/" | "*" | "(" :
                return_list.append(element)
                operator_counter += 1
            case ")" :
                return_list.append(element)
                operator_counter = 0
            case _: #if not an operator
                if len(return_list) == 0:
                    return_list.append(element)
                else:
                    match return_list[-1]:
                        case "+" | "/" | "*" | "(" | ")":
                            return_list.append(element)
                        case _:
                            if operator_counter != 1:   #if the last one is a number or a "-" and there's more than one operator before it, it's a part of the number.
                                return_list[-1] += element
                            else:
                                return_list.append(element)
                operator_counter = 0 #reset to zero if the last added element isn't an operator.
    return return_list

def infix_to_postfix(tokens: list[str]) -> list[str]:
    cache = []              #temporary operator stack
    posfixed_tokens = []     #return list
    for element in tokens:
        match element:
            case "(" :
                cache.append(element)
            case ")" :
                while cache[-1] != "(":
                    posfixed_tokens.append(cache.pop())
                del cache[-1]
            case "+" | "-" | "/" | "*" :
                match element:
                    case "-" | "+" :
                        priority = "-+*/"
                    case "*" | "/" :
                        priority = "*/"
                condition = True
                while condition:
                    if len(cache) == 0:
                        condition = False
                    elif cache[-1] in priority:
                        posfixed_tokens.append(cache.pop())
                    else:
                        condition = False
                cache.append(element)
            case _:
                posfixed_tokens.append(element)
    posfixed_tokens.extend(reversed(cache))
    return posfixed_tokens

def evaluate_postfix(tokens: list[str]) -> float:
    cache = []
    for element in tokens:
        match element:
            case "+":
                cache.append(float(cache.pop())+float(cache.pop()))
            case "-":
                cache.append(float(cache.pop(-2))-float(cache.pop()))
            case "*":
                cache.append(float(cache.pop())*float(cache.pop()))
            case "/":
                cache.append(float(cache.pop(-2))/float(cache.pop()))
            case _: #if it's not an operator, it's a number, so we add it to the stack.
                cache.append(element)
    if len(cache) > 1:  #if there's more than one element in the stack, it means that the expression is invalid, because all the numbers haven't been used.
        raise IndexError("Invalid expression")
    return float(cache[0]) #float