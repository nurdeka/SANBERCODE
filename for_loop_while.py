#!/usr/bin/env python
# coding: utf-8

# <h2>Soal 1: Comparison Operator</h2>
# 
# - Berikan contoh comparison dari tipe data string
# - Berikan contoh comparison dari tipe data boolean
# - Berikan contoh comparison dari tipe data integer

# In[30]:


#Comparison tipe data string

negara = "Indonesia"
print("_Comparison tipe data string_")
print("negara == Indonesia :" , negara == "Indonesia")
print("negara != Indonesia :" ,negara != "Indonesia")
print("               ")

#Comparison tipe data Boolean
print("_Comparison tipe data Boolean_")
print("9 > 10 :", 9>10)
print("9 = 10 :", 9==10)
print("9 < 10 :", 9<10)
print("               ")

#Comparison tipe data Integer
print("_Comparison tipe data Integer_")
a = 10
b = 20
print("a = 10")
print("b = 20")
print("               ")
print("a = b :", a == b)
print("a != b :",a != b)
print("a > b :",a > b)
print("a < b :",a < b)
print("a >= b :",a >= b)
print("a <= b :",a <= b)


# <h2>Soal 2: Boolean Comparison</h2>
# 
# - Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'and'
# - Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'or'
# - Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'not'

# In[33]:


print((12 > 11) and (5 < 4))  
print((8 == 8) or (6 != 6)) 
print(not(3 <= 1))         


# <h2>Soal 3: If-Else Statement</h2>
# 
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan
# 
# - Bualah sebuah if-else statement yang dimana akan mem-print 'Besar' jika ruangan adalah 'Kamar' dan ukuran lebih dari 12, kemudian mem-print 'Sedang' jika ruangan adalah 'Kamar' dan ukuran lebih dari 6 dan memprint 'Kecil' jika ruangan adalah 'Kamar' dan ukuran ruangan lebih kecil dan sama dengan 6.

# In[74]:


ruangan = "Kamar"
size = int(input("Input size : " ))

if ruangan == "Kamar" and size > 12:
    print('Besar')
elif ruangan == "Kamar" and size > 6:
    print('Sedang')
else :
    print('Kecil')


# <h2>Soal 4: Comparison Operator dengan fungsi</h2>
# 
# Buatlah sebuah fungsi yang menerima satu argument bertipe data numeric dan menghasilkan sebuah return sebagai berikut :
# - menghasilkan return 'Aneh' jika nilai dari argument tersebut adalah bilangan ganjil
# - menghasilkan return 'Tidak Aneh' jika nilai dari argument tersebut adalah bilangan genap dan diantara nilai 2 sampai 5 (2 dan 5 termasuk)
# - menghasilkan return 'Aneh' jika nilai dari argument tersebut adalah bilangan genap dan diantara nilai 6 sampai 20 (6 dan 20 termasuk)
# - menghasilkan return 'Tidak Aneh' jika nilai dari argument tersebut adalah bilangan genap dan lebih besari dari 20

# In[23]:


def num(k):
    if (k % 2) != 0 :
        result = "Aneh"
    elif (k % 2) == 0 and k >= 2 and k <= 5 :
        result = "Tidak Aneh"
    elif (k % 2) == 0 and k >= 6 and k <= 20 :
        result = "Aneh"
    elif (k % 2) == 0 and k > 20 :
        result = "Tidak Aneh"
    else :
        result = "lainnya"
    return result
num(int(input("Input number : " )))


# <h2>Soal 5: While Loop dan For Loop</h2>
# 
# - Apa perbedaan while loop dan for loop?
# - Berikan contoh sederhana cara menggunakan while loop dan for loop

# In[25]:


#=====================Perbedaan While dan Loop========================================
#    Perulangan for disebut counted loop (perulangan yang terhitung),
#    sementara perulangan while disebut uncounted loop (perulangan yang tak terhitung).
#    Perbedaannya adalah perulangan for biasanya digunakan untuk mengulangi kode yang sudah diketahui banyak perulangannya.
#    Sementara while untuk perulangan yang memiliki syarat dan tidak tentu berapa banyak perulangannya.

# Tulis Kode While
i = 0
while i < 6:
  print(f"While ke {i}")
  i += 1

# Tulis Kode For Loop
for x in range(6):
  print(f"Loop ke {x}")


# <h2>Soal 6: While Loop</h2>
#     
# Buatlah sebuah code while loop sebagai berikut :
# - Buatlah suatu fungsi yang merima satu input nilai numeric
# - Dalam fungsi, Buat sebuah while-loop dengan melakukan comparasi terhadap inputan tersebut, dimana looping/iterasi terus berjalan apabila nilai inputan tidak sama dengan 0
# - Dalam setiap iterasi update nilai variable inputan itu, jika input lebih dari 0, maka kurangi variabel tersebut sebesar 1, selain itu tambahkan 1
# - print nilai variable input dalam setiap awal iterasi

# In[1]:


a = 10

def fungsi_while(a):
    while (a > 0):
        print("\n", a)
        a -= 1
        if a == 0:
            break
#    print("\n", n)
    while a < 0:
        print("\n", a)
        a += 1
        if a ==0:
            break
#    print("\n", n)
    else :
        print(" ")
#print('Loop ended.')
fungsi_while(a)


# Expected Output:
# 
# 10
# 
# 9
# 
# 8
# 
# 7
# 
# 6
# 
# 5
# 
# 4
# 
# 3
# 
# 2
# 
# 1

# <h2>Soal 7: For Loop</h2>
#     
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan:
# 
# - Buatlah sebuah loop dengan mengiterasi sebuah objek list kemudian di kalikan dengan index dari list tersebut dan print hasilnya

# In[2]:


obj_list= [1, 16, 11, 10, 5]

# lengkapi code di bawah
for index, i in enumerate(obj_list):
    print(index*i)


# Expected Output:
# 
# 0
# 
# 16
# 
# 22
# 
# 30
# 
# 20
# 
