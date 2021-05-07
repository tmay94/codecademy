weight = 20
#
# Ground Shipping
flat_charge = 20
if weight <= 2:
  ppp = 1.50
elif weight > 2 and weight <= 6:
  ppp = 3.00
elif weight > 6 and  weight <= 10:
  ppp = 4.00
elif weight > 10:
  ppp = 4.75
else:
  print("ERROR!")
#print("DEBUG:",ppp, weight, flat_charge)
ground_total = ppp * weight + flat_charge
print("Gound Shipping Total Cost:", ground_total)
#
# Ground Shipping Premium
premium_charge = 125
premium_total = premium_charge
print("Ground Shipping Premium Total Cost:", premium_total)
#
# Drone Shipping
if weight <= 2:
  ppp = 4.50
elif weight > 2 and weight <= 6:
  ppp = 9.00
elif weight > 6 and  weight <= 10:
  ppp = 12.00
elif weight > 10:
  ppp = 14.25
else:
  print("ERROR!")
#print("DEBUG:",ppp, weight, flat_charge)
drone_total = round(weight * ppp,2)
print("Drone Shipping Total Cost:", round(weight * ppp,2))
#
# Extra
ground_cheap = "Ground shipping is the cheapest method for your package!"
premium_cheap = "Ground Premium shipping is the cheapest method for your package!"
drone_cheap = "Drone shipping is the cheapest method for your package!"
if ground_total < premium_total and drone_total:
  print("\n","*",ground_cheap)
elif premium_total < ground_total and drone_total:
  print("\n","*",premium_cheap)
elif drone_total < premium_total and ground_total:
  print("\n","*",drone_cheap)
else:
  print("ERROR")