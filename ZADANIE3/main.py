import numpy as np
import matplotlib.pyplot as plt

# Wygeneruj dane (np. 2 tablice x i y o długości 10) za pomocą NumPy.
# Narysuj wykres punktowy (funkcją ax.scatter(...) lub plt.scatter(...)).
# Podpisz osie (np. X axis, Y axis) oraz ustaw tytuł.
# Funkcja ma zwracać obiekt matplotlib.figure.Figure, co ułatwi testy.


def draw_scatter_plot():
    """
    1) Wygeneruj dane x, y (np. np.arange(10) i jakieś y losowe).
    2) Rysuj wykres punktowy (scatter).
    3) Ustaw etykiety osi, tytuł, legendę.
    4) Zwróć obiekt Figure.
    """
    np.random.seed(123)
    
    # utwórz x, y
    x = np.arange(10)
    y = x**2
    
    fig, ax = plt.subplots()
    
    ax.scatter(x,y, label='x^2', color='blue')
    
    # label dla x, y, title, legend
    ax.set_xlabel('os X')
    ax.set_ylabel('os Y')
    ax.set_title('Wykres punktowy')
    
    # return rysunek
    return fig

if __name__ == '__main__':
    fig = draw_scatter_plot()
    plt.show()
