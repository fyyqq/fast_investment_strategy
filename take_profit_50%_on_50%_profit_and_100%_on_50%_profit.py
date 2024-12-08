# 1. PROFIT = 50% => TP = 50%
# 2. PROFIT = 50% => TP = 100%

a = 0.5 # 50%
b = 1  # 75%

capital = 10
fee = 0.35

txns = (capital - 0.35)
fifty_percent_profit = round(txns + (txns * a), 2)
sell_half_fifty_percent_profit = round(txns + (txns * a),2) / 2

print(f"Capital: ${capital}")
print(f"Buy Transaction: ${txns}")
print("-----------------------")

print(f"🟢 50% Profit: ${fifty_percent_profit}")
print(f"🔴 SELL HALF on 50% Profit: ${round(sell_half_fifty_percent_profit - fee, 2)} to wallet")

print("-----------------------")
print(f"Total Wallet: ${round(sell_half_fifty_percent_profit - fee, 2)}")
print(f"Total Fee: ${fee}")
print("-----------------------")

print(f"🚀 Capital Run: ${sell_half_fifty_percent_profit}")

print("-----------------------")
print(f"🚀 50% Profit on Capital Run: ${sell_half_fifty_percent_profit + (sell_half_fifty_percent_profit) * a}")
print(f"🔴 SELL 100% on 50% Profit: ${(sell_half_fifty_percent_profit + (sell_half_fifty_percent_profit) * a) - fee} to wallet")

print("-----------------------")
print(f"Total Wallet: ${round(sell_half_fifty_percent_profit - fee, 2) + (sell_half_fifty_percent_profit + (sell_half_fifty_percent_profit) * a) - fee}")
print(f"Total Fee: ${fee * 2}")
