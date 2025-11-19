import matplotlib.pyplot as plt
import matplotlib

def plot_graph():
    fig, ax = plt.subplots(figsize=(6, 3))
    text = 'There are 多个汉字 👈👉 in between!'
    
    # Set the font properties for displaying Chinese characters and emojis
    plt.rcParams['font.family'] = 'SimHei'  # For Chinese characters
    plt.rcParams['font.sans-serif'] = 'Segoe UI Emoji'  # For emojis
    
    plt.figtext(0.3, 0.7, text, fontsize=12)
    plt.title(text, fontsize=14)
    plt.xlabel(text, fontsize=12)
    plt.ylabel(text, fontsize=12)
    import os
    output_dir = os.path.dirname(__file__)
    output_path = os.path.join(output_dir, '1.png')
    plt.savefig(output_path)

plot_graph()