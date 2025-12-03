ingreso_mensual = float(input("Ingreso mensual: "))
ingreso_anual = ingreso_mensual * 14

tramos = [
    (0, 20000, 0.0),
    (20000, 50000, 0.10),
    (50000, 100000, 0.20),
    (100000, float("inf"), 0.30)
]

impuesto_por_tramo = []
impuesto_total = 0
restante = ingreso_anual

for limite_inferior, limite_superior, tasa in tramos:
    if ingreso_anual > limite_inferior:
        tope = min(ingreso_anual, limite_superior)
        monto_tramo = max(0, tope - limite_inferior)
        impuesto = monto_tramo * tasa
        impuesto_por_tramo.append((f"{limite_inferior}-{limite_superior}", impuesto))
        impuesto_total += impuesto

print("\nImpuesto por tramo:")
for tramo, impuesto in impuesto_por_tramo:
    print(tramo, "=>", impuesto)

print("Total impuesto:", impuesto_total)
print("Tasa efectiva real (%):", (impuesto_total / ingreso_anual) * 100)