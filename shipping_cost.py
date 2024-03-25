weight = 41.5
cost_premium_shipping = 125.00
# Ground shipping
if weight >= 10:
  cost_ground_shipping = weight * 4.75 + 20.00
elif weight > 6:
  cost_ground_shipping = weight * 4.00 + 20.00
elif weight > 2:
  cost_ground_shipping = weight * 3.00 + 20.00
else:
  cost_ground_shipping = weight * 1.5 + 20.00
print("Ground shipping cost: $", cost_ground_shipping)

# Premium ground shipping
print("Premium ground shipping cost: $", cost_premium_shipping)

# Drone shipping
if weight > 10:
  cost_drone_shipping = weight * 14.25
elif weight > 6:
  cost_drone_shipping = weight * 12.00
elif weight > 2:
  cost_drone_shipping = weight * 9.00
else:
  cost_drone_shipping = weight * 4.50
print("Drone shipping cost: $", cost_drone_shipping)
