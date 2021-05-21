import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button


if __name__ == '__main__':



    img = cv2.imread('test_image.png',0)

    fig, _ = plt.subplots()
    
    xaxis = plt.axes([0.2, 0.025, 0.2, 0.04], facecolor="lightgoldenrodyellow")
    yaxis = plt.axes([0.6, 0.025, 0.2, 0.04], facecolor="lightgoldenrodyellow")

    x = Slider(xaxis, "Minimum", 0, 1000, valinit=100)
    y = Slider(yaxis, "Maximum", 0, 1000, valinit=200)

    min_val = x.val
    max_val = y.val

    edges = cv2.Canny(img, min_val, max_val)

    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    

    def update(val):
        min_val = x.val
        max_val = y.val
        plt.subplot(122),plt.imshow(cv2.Canny(img, min_val, max_val),cmap = 'gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        fig.canvas.draw_idle()

    
    x.on_changed(update)
    y.on_changed(update)



    plt.show()