import matplotlib.pyplot as plt
import numpy as np


labels = ['Ebola', 'MERS', 'SARS', 'COVID-19', 'Seasonal Flu']
low_estimate = [1.5, 0.42, 3, 1.5, 1.3]
high_estimate = [2.5, 0.92, 3, 3.5, 1.3]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, low_estimate, width, label='low estimate')
rects2 = ax.bar(x + width/2, high_estimate, width, label='high estimate')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Infection rate per infected infected person')
ax.set_title('Infection rates of viruses invovled in outbreaks worldwide as of 2020')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()