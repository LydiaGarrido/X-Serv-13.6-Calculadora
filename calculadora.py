#!/usr/bin/python3

import sys


def suma(operando1, operando2):
    return operando1 + operando2


def resta(operando1, operando2):
    return operando1 - operando2


def multiplicacion(operando1, operando2):
    return operando1 * operando2


def division(operando1, operando2):
    return operando1 / operando2

try:
    operando1 = float(sys.argv[2])
    operando2 = float(sys.argv[3])
except ValueError:
    sys.exit("No estan permitidos operandos que no sean float")

if sys.argv[1] == 'sumar':
    print(suma(operando1, operando2))

elif sys.argv[1] == 'restar':
    print(resta(operando1, operando2))

elif sys.argv[1] == 'multiplicar':
    print(multiplicacion(operando1, operando2))

elif sys.argv[1] == 'dividir':
    try:
        print(division(operando1, operando2))
    except ZeroDivisionError:
        sys.exit("No me dividas entre cero")
