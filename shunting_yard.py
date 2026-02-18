def tokenize(expression: str) -> list[str]:
    expression = expression.replace(" ","")
    return_list = []
    for element in expression:
        match element:
            case "+" | "-" | "/" | "*" | "(" | ")":
                return_list.append(element)
            case _:
                if len(return_list) == 0:
                    return_list.append(element)
                else:
                    if return_list[-1] == "-":
                        match return_list[-2]:
                            case "+" | "-" | "/" | "*" | "(" | ")":
                                return_list[-1] += element
                            case _:
                                return_list.append(element)
                    else:
                        return_list.append(element)
    return return_list