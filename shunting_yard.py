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
                    match return_list[-1][0]:
                        case "+" | "/" | "*" | "(" | ")":
                            return_list.append(element)
                        case "-":
                            if operator_counter > 1:
                                return_list[-1] += element
                            else:
                                return_list.append(element)
                        case _:
                            if operator_counter == 0: #if the last added element is a number:
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
            case "-" | "+" :
                priority = "-+*/"
            case "*" | "/" :
                priority = "*/"
        match element:
            case "(" :
                cache.append(element)
            case ")" :
                while cache[-1] != "(":
                    posfixed_tokens.append(cache.pop())
                del cache[-1]
            case "+" | "-" | "/" | "*" :
                condition = True
                while condition:
                    if len(cache) <= 0:
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