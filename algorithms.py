import numpy as np

def desenha_circulo(img, centro, raio, cor):
    cx, cy = centro

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if (x - cx)**2 + (y - cy)**2 <= raio**2:
                img[x, y] = cor

    return img


def desenha_reta(img, p1, p2, cor):
    x1, y1 = p1
    x2, y2 = p2

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    err = dx - dy

    while True:
        img[x1, y1] = cor

        if (x1, y1) == (x2, y2):
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x1 += sx

        if e2 < dx:
            err += dx
            y1 += sy

    return img