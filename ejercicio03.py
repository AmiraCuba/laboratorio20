salario_base = float(input("Salario base: "))
horas_extras = float(input("Horas extras: "))
pago_hora_extra = float(input("Pago por hora extra: "))
bono = float(input("Bono: "))
afp = float(input("Porcentaje AFP (%): "))
salud = float(input("Porcentaje Salud (%): "))

salario_bruto = round(salario_base + (horas_extras * pago_hora_extra))+ bono

descuento_afp = salario_base * (afp / 100)
descuento_salud = salario_base * (salud / 100)
descuentos_totales = round(descuento_afp + descuento_salud)

salario_neto = round(salario_bruto - descuentos_totales, 2)

print("\n--- RESULTADOS ---")
print(f"Salario bruto (sin descuentos): {salario_bruto}")
print(f"Descuentos totales: {descuentos_totales}")
print(f"Salario neto: {salario_neto}")
