from itertools import count

from numpy import diff

# %%

tab = [2, -5, 8, 15, 2, 4]
n = 6
k = 3


# Tworzenie ramki

new_tab = [] #[[2,-5,8],[15,2,4]]
counter = 0
ramka = []

for i in tab:
    for j in tab:
        
        if counter < k:
            ramka.append(i)

        
        if counter == k:
            new_tab.append(ramka)
            counter = 0
            ramka = []
        counter += 1

    print(counter)
print(new_tab)


# %%

# Ramka
dif_p = [2, -5, 8]

maks = []
maksimum_pair = 0

for i in dif_p:
    maks.append(i)

    for j in dif_p:
        maks.append(j)
        
        if len(maks) == 2:
            print(diff(maks))
            if maksimum_pair < abs(diff(maks)):
                maksimum_pair = abs(diff(maks))

    maks = []



# %%
