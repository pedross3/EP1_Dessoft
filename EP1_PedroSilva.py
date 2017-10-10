import turtle

regra = input("Regra inicial")
repo = input("Regra de reposição")
itera = int(input("Número de iterações"))

tortuga = turtle.Turtle()
tortuga.speed(10)

for i in range(itera):

    if "F" in regra:
        regra = regra.replace("F", repo)
    for b in regra:
        if b == "F":
            tortuga.forward(50)
            tortuga.right(45)
        elif b == "T":
            tortuga.backward(20)
            tortuga.circle(15)
        elif b == "-":
            tortuga.left(60)
        elif b == "+":
            tortuga.right(60)
        else:
            cursor.right(90)
            cursor.forward(10)
            cursor.dot(1, dot_colors[dot_index])

    #print(regra)
done()
