# 1. PROFIT = 50% => TP = 100%

a = 0.5 # 50%
b = 1  # 75%

capital = 50
fee = 0.35

txns = (capital - 0.35)
fifty_percent_profit = round(txns + (txns * a), 2)
sell_half_fifty_percent_profit = round(txns + (txns * a),2) / 2


print(f"Capital: ${capital}")
print(f"Buy Transaction: ${txns}")
print("-----------------------")

print(f"🟢 50% Profit: ${fifty_percent_profit}")
print(f"🔴 SELL 100% Profit: ${fifty_percent_profit - fee}")
print("-----------------------")
print(f"Total Wallet: ${fifty_percent_profit - fee}")
print(f"Total Fee: ${fee}")