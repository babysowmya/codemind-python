plt.figure(figsize=(8, 5))
plt.bar(df1['Year'], df1['Profit'], color='g', label='Profit')
plt.title('Yearly Profit Analysis')
plt.xlabel('Year')
plt.ylabel('Profit')
plt.xticks(df1['Year'])
plt.legend()
plt.show()
