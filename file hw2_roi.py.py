# hw2_roi.py

initial_investment = float(input("Nhập tổng vốn ban đầu: "))
final_value = float(input("Nhập tổng giá trị bán ra: "))

net_profit = final_value - initial_investment
roi = (net_profit / initial_investment) * 100

print(f"Lợi nhuận ròng: {net_profit:.0f} đồng")
print(f"Tỷ lệ ROI: {roi:.2f}%")
