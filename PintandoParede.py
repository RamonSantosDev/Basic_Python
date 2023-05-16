width = float(input("Largura da parede: "))
height = float(input("Altura da parede: "))
area = width * height

print("Sua parede tem a dimensão de {}x{} e sua área é de {}m²".format(width,height,area))
tinta = area / 2
print("Para pintar precisa {}L".format(tinta))