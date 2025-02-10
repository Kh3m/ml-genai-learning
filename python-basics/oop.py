class Shirt:
    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price


shirt1 = Shirt(
    "Red",
    size=45,
    price=234,
    style="short"
)

print(shirt1.color)