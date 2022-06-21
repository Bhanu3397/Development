weight = 4.8
groundshippingflatcharge = 20.00
droneshippingflatcharge = 0
groundshippingcost = float
groundshippingpremiumcost = float
droneshippingcost = float
# Ground Shipping
if weight <= 2:
  groundshippingcost = weight*1.50 + groundshippingflatcharge
elif weight > 2 and weight<= 6:
  groundshippingcost = weight*3.00 + groundshippingflatcharge
elif weight > 6 and weight<= 10:
  groundshippingcost = weight*4.00 + groundshippingflatcharge
else:
  groundshippingcost = weight*4.75 + groundshippingflatcharge
print("Ground shipping costs: $"+ str(groundshippingcost))

#Ground Shipping Premium
groundshippingpremiumcost = 125.00
print("Ground shipping premium costs: $"+ str(groundshippingpremiumcost))

#Drone Shipping
if weight <= 2:
  droneshippingcost = weight*4.50 + droneshippingflatcharge
elif weight > 2 and weight<= 6:
  droneshippingcost = weight*9.00 + droneshippingflatcharge
elif weight > 6 and weight<= 10:
  droneshippingcost = weight*12.00 + droneshippingflatcharge
else:
  droneshippingcost = weight*14.25 + droneshippingflatcharge
print("Drone shipping costs: $"+ str(droneshippingcost))