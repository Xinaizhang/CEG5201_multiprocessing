import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('d1.xlsx')

x = range(len(data))

print(data)

plt.figure(figsize=(10, 6))
plt.plot(x, data['1Measured Speed up '], label='Processor=1 Measured Speed Up')
plt.plot(x, data['2Measured Speed up '], label='Processor=2 Measured Speed Up')
plt.plot(x, data['3Measured Speed up '], label='Processor=4 Measured Speed Up')
plt.plot(x, data['4Measured Speed up '], label='Processor=8 Measured Speed Up')
plt.xlabel('Array')
plt.ylabel('Measured Speed Up')
plt.title('Measured Speed Up With Different Processor Number')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(x, data['1Cumulative Speed up'], label='Processor=1 Cumulative Speed Up')
plt.plot(x, data['2Cumulative Speed up'], label='Processor=2 Cumulative Speed Up')
plt.plot(x, data['3Cumulative Speed up'], label='Processor=4 Cumulative Speed Up')
plt.plot(x, data['4Cumulative Speed up'], label='Processor=8 Cumulative Speed Up')
plt.xlabel('Array')
plt.ylabel('Cumulative Speed Up')
plt.title('Cumulative Speed Up With Different Processor Number')
plt.legend()
plt.grid()
plt.show()
