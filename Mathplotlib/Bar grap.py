import matplotlib.pyplot as plt

D = {u'Label1':26, u'Label2': 17, u'Label3':30}

plt.bar(range(len(tag)), list(tag.values()), align='center')
plt.xticks(range(len(tag)), list(tag.keys()))
# # for python 2.x:
# plt.bar(range(len(D)), D.values(), align='center')  # python 2.x
# plt.xticks(range(len(D)), D.keys())  # in python 2.x

plt.show()
