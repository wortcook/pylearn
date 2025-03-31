import io
import matplotlib.pyplot as plt
from PIL import Image

def fig2img(fig):
    """Converts a Matplotlib figure to a PIL Image.
    
    Args:
        fig (matplotlib.figure.Figure): Matplotlib figure to convert.
    
    Returns:
        PIL.Image.Image: PIL Image of the figure.
    """
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img = Image.open(buf)
    return img

import numpy as np

images = []

x = np.arange(0, 10, 0.1)
x2 = x**2 + np.random.randn(len(x)) * 10

for i in np.arange(0.1, 10, 0.1):
    x = np.arange(0, i, 0.1)
    
    #set the figure size to be 640x480
    plt.figure(figsize=(6.4, 4.8))
    plt.title('Title')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.grid()
    
    #plot x vs x2 from 0 to i
    plt.plot(x, x2[:len(x)], label='x2')
    
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    
    fig = plt.gcf() # Gets the current figure
    img = fig2img(fig)
    plt.clf()
    plt.close(fig)
    images.append(img)
    
images[0].save('drawme.gif', save_all=True, append_images=images[1:], optimize=True, duration=40, loop=0)
    