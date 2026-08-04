import matplotlib.pyplot as plt
values = [2, 4, 3]
for index, value in enumerate(values):
    plt.bar(index, value, color="steelblue")
plt.title("Bookings")
plt.show()
