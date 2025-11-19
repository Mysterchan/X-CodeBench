import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.DataFrame([['16-Jun-21', 0, 41.86, 2.33, 8.14, 41.86, 5.81], ['29-Jul-21', 0, 65.08, 0, 6.07, 24.51, 4.34], ['11-Aug-21', 0, 49.66, 0, 5.52, 37.93, 6.9], ['15-Sep-21', 0, 51.12, 0, 3.19, 31.63, 14.06],
['6-Oct-21', 0, 65.79, 0, 6.73, 20.56, 6.92], ['3-Nov-21', 0, 57.03, 0, 5.54, 34.06, 3.37],
['1-Dec-21', 0, 35.49, 17.74, 5.91, 32.53, 8.32], ['30-Dec-21', 0, 71.46, 0, 2.98, 21.84, 3.72], ['27-Jan-22', 0.21, 51.45, 0, 0.83, 42.74, 4.56], ['23-Feb-22', 0, 40, 0, 4, 46, 10],
['23-Mar-22', 0, 33.33, 15.52, 4.02, 38.51, 8.62], ['20-Apr-22', 0, 3.19, 0, 1.59, 94.02, 1.2],
['18-May-22', 0, 7.08, 17.7, 3.54, 64.16, 7.52], ['15-Jun-22', 0, 0, 56.46, 0, 33.88, 9.66],
['20-Jul-22', 0, 0, 15.23, 2.03, 78.17, 4.57]], columns=['Date', 'Cylindrospermopsis raciborskii', 'Merismopedia sp.', 'Aphanocapsa sp.', 'Chroococcus sp.', 'Gloeocapsa sp.', 'Planktolyngbya sp.'])

df2 = pd.DataFrame([['16-Jun-21', 330], ['29-Jul-21', 961], ['11-Aug-21', 834], ['15-Sep-21', 612], ['6-Oct-21', 564], ['3-Nov-21', 537], ['1-Dec-21', 595], ['30-Dec-21', 876], ['27-Jan-22', 518], ['23-Feb-22', 225],
['23-Mar-22', 710], ['20-Apr-22', 259], ['18-May-22', 476], ['15-Jun-22', 716], ['20-Jul-22', 219]], columns=['Date', 'Total Cyanobacteria'])

# Convert 'Date' columns to datetime for proper plotting
df1['Date'] = pd.to_datetime(df1['Date'], format='%d-%b-%y')
df2['Date'] = pd.to_datetime(df2['Date'], format='%d-%b-%y')

fig, ax1 = plt.subplots(figsize=(12,6))

# Plot stacked bar chart on ax1
df1.set_index('Date').plot(kind='bar', stacked=True, ax=ax1, legend=True)

# Plot line chart on ax1's twin axis ax2
ax2 = ax1.twinx()
ax2.plot(df2['Date'], df2['Total Cyanobacteria'], color='red', marker='o', label='Total Cyanobacteria')

# Set labels
ax1.set_xlabel('Date')
ax1.set_ylabel('Percentage')
ax2.set_ylabel('Total Cyanobacteria')

# Format x-axis ticks to show dates nicely
ax1.set_xticklabels([d.strftime('%d-%b-%y') for d in df1['Date']], rotation=45, ha='right')

# Add legend for line plot
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left')

plt.tight_layout()
plt.show()