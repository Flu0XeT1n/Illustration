"""
=================
Stacked bar chart
=================

This is an example of creating a stacked bar plot with error bars
using `~matplotlib.pyplot.bar`.  Note the parameters *yerr* used for
error bars, and *bottom* to stack the women's bars on top of the men's
bars.
"""

import matplotlib.pyplot as plt

# labels = [1, 2, 3, 4, 5]
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
test_means = [50, 46, 72, 28, 19]
men_std = [2, 3, 4, 1, 2]
women_std = [3, 5, 2, 3, 3]
width = 0.35  # the width of the bars: can also be len(x) sequence

ax = plt.subplot()  # type: Union[Optional[int], Any]
ax.bar(labels, men_means, width, label='Men')

'''ax.bar(labels, men_means, width, yerr=men_std, label='Men')
ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means, color='red',
      label='Women')'''

ax.bar(labels, women_means, width, bottom=men_means, color='red',
       label='Women')
ax.bar(labels, test_means, width, bottom=women_means, color='pink',
       label='Test')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

plt.show()
