import matplotlib.pyplot as plt


def plot_graph():
    fig, ax = plt.subplots(figsize=(6, 3))
    text = 'There are 多个汉字 👈👉 in between!'
    plt.rcParams['font.family'] = ['Segoe UI Emoji', 'SimHei']
    plt.figtext(0.3, 0.7, text)
    plt.title(text)
    plt.xlabel(text)
    plt.ylabel(text)
    plt.show()


plot_graph()