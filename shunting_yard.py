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
                            if return_list[-1][0] == "-" and operator_counter > 1:
                                return_list[-1] += element
                            elif operator_counter == 0:
                                return_list[-1] += element
                            else:
                                return_list.append(element)
                operator_counter = 0 #reset to zero if the last added element isn't an operator.
    return return_list