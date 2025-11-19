import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def plot_graph():
    fig, ax = plt.subplots(figsize=(6, 3))
    text = 'There are 多个汉字 👈👉 in between!'

    # Use a font that supports both Chinese characters and emoji
    # Here we use a font that supports Chinese (SimHei) and fallback to a font that supports emoji (Segoe UI Emoji)
    # We create a FontProperties object with a list of fonts to try in order
    font = FontProperties(family=['SimHei', 'Segoe UI Emoji'])

    plt.figtext(0.3, 0.7, text, fontproperties=font)
    ax.set_title(text, fontproperties=font)
    ax.set_xlabel(text, fontproperties=font)
    ax.set_ylabel(text, fontproperties=font)

    import os
    output_dir = os.path.dirname(__file__)
    output_path = os.path.join(output_dir, '1.png')
    plt.savefig(output_path)

plot_graph()