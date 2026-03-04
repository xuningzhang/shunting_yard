import tkinter as tk
import shunting_yard

class Unknown_operator(Exception):
    pass

class Parentesis(Exception):
    pass

def evaluate(expression : str) -> tuple[list[str], float]:
    tokens = shunting_yard.tokenize(expression)
    postfixed = shunting_yard.infix_to_postfix(tokens)
    result = shunting_yard.evaluate_postfix(postfixed)
    return postfixed, result

def main():
    #erase old expression
    postfixed_expression_box.config(text="Expression postfixée: ---")
    result_box.config(text="Résultat: ---")
    error_box.config(text="Erreur: ---")

    try:
        expression = input_text.get()

        #if expression doesn't contain any unwanted symbol.
        for element in expression.replace(" ",""):
            if element not in "1234567890-+*/().,":
                raise Unknown_operator("Opérateur inconnue")

        #if all parentesis are paired.
        if expression.count("(") != expression.count(")"):
            raise Parentesis("Parentèses non appariées")
        
        #Calculate
        postfixed, result = evaluate(expression)

        #GUI update
        postfixed_expression_box.config(text= f"Expression postfixée: {postfixed}")
        result_box.config(text=f"Résultat: {result}")

    except Unknown_operator as e:
        error_box.config(text=f"Erreur: {e}")
    except Parentesis as e:
        error_box.config(text=f"Erreur: {e}")
    except IndexError:
        error_box.config(text="Erreur: Expression invalide")
    except ZeroDivisionError:
        error_box.config(text="Erreur: Division par zero")
    except ValueError:
        error_box.config(text="Erreur: Nombre mal formé")
    except Exception as e:
        error_box.config(text=f"Erreur inconnue: {e}")

#Window
calculator = tk.Tk()
calculator.title("Calculatrice Python")

input_text = tk.StringVar()

name = tk.Label(calculator, text="Calculatrice super bien faite!!!\nVeuillez entrer votre expression mathématique.")
input_box = tk.Entry(calculator, textvariable= input_text)
convert_button = tk.Button(calculator, text= "Convertir l'expression en expression postfixé", command= main)
postfixed_expression_box = tk.Label(calculator, text= "Expression postfixée: ---")
result_box = tk.Label(calculator, text= "Résultat: ---")
error_box = tk.Label(calculator, text= "Erreur: ---")

name.pack()
input_box.pack()
convert_button.pack()
postfixed_expression_box.pack()
result_box.pack()
error_box.pack()

calculator.mainloop()