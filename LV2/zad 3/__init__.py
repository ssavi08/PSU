import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")
img = img[:,:,0].copy()

print(img.shape)
print(img.dtype)

plt.figure()
plt.imshow(img, cmap="gray")
plt.show()

broj = 150

brightnes = img + broj #inkrementiran broj se dodaje svim pikselima slike
brightnes = np.clip(brightnes, 0, 255) #vrijednost brightnes mora biti unutar granica rgb 0-255

plt.figure() #prikaz slike
plt.imshow(img, cmap="gray") #prikazuje sliku koristeci mapu boja u sivoj razini
plt.title("brightnes") #naslov slike

plt.figure()
plt.imshow(img, cmap="gray")
plt.title("original")

rotacija = np.rot90(img, k = 1) #jedna rotacija za 90 stupnjeva suprotno od smjera kazaljke na satu
plt.figure()
plt.imshow(rotacija, cmap="grey")
plt.title("rotirana")

mirror = img[:, :: -1] #zrcaljena slika, rezanje polja slike, prvi :, oznacava sve sve retke slike a :: -1 oznacava sve stupce u obrnutom redosljedu (invertiramo redosljed piksela u svakom retku
plt.figure()
plt.imshow(mirror, cmap="gray")
plt.title("zrcaljena slika")

length = img.shape[0]
height = img.shape[1]

#rezana =

plt.figure()
plt.imshow(rezana, cmap="grey")
plt.title("rezana slika")

plt.show()
