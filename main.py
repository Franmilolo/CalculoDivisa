def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

monto = float(input("Ingrese el monto en dolares: "))
ratio = float(input("Ingrese el ratio de conversion: "))

conversion = str(exchange_money(monto,ratio))

print("Sus dolares son equivalentes a " + conversion)

