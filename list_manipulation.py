#!/usr/bin/env python
# coding: utf-8

# # List

# <h2>Soal 1: Sifat List</h2>
# 
# Jawab Pertanyaan di bawah ini:
# 
# Jenis data apa saja yang bisa ada di dalam List?

# List dapat diisi nilai dengan tipe data string, integer, float, Boolean, tuple, dictionary bahkan list dapat diisi dengan list juga (bersarang)

# <h2>Soal 2: Akses List</h2>
# 
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan

# In[ ]:


a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
# slicing list
del a[0]
del a[4]
print(a)


# Expected Output :
# 
# [ '13b', 'aa1', 1.32, 22.1 ]

# <h2>Soal 3: Nested List</h2>
# 
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan

# In[ ]:


a = [1.32, 22.1, 2.34]
b = ['1', '13b', 'aa1']
c = [3, 40, 100]
# combine list
acb = [a,c,b]
print(acb)


# Expected Output :
# 
# [ [1.32, 22.1, 2.34], [3, 40, 100], ['1', '13b', 'aa1'] ]

# <h2>Soal 4: Akses Nested List</h2>
# 
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan

# In[1]:


a = [
    [5, 9, 8],
    [0, 0, 6]
    ]
# subsetting list
print(a[0][0:3])


# Expected Output :
# 
# 
# [0, 6]

# <h2>Soal 5: Built in Function List</h2>
# 
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan

# In[ ]:


p = [0, 5, 2, 10, 4, 9]
# ordered list
print(sorted(p, reverse=False))
# get max value of list
print(max(p))


# Expected Output :
# 
# [0, 2, 4, 5, 9, 10]
# 
# 10

# <h2>Soal 6: List Operation</h2>
# 
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan

# In[ ]:


a = [1, 3, 5]
b = [5, 1, 3]
# combine list
for x in a:
  b.append(x)

print(b)


# Expected Output :
# 
# [5, 1, 3, 1, 3, 5]

# <h2>Soal 7: List Manipulation</h2>
# 
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan

# In[ ]:


a = [
    [5, 9, 8],
    [0, 0, 6]
    ]
# change list value
a[0][2]=10
# change list value
a[1][0]=11
print(a)


# Expected Output :
# 
# [ [5, 9, 10], [11, 0, 6] ]

# <h2>Soal 8: Delete Element List</h2>
# 
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan

# In[ ]:


areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Hilangkan elemen yang bernilai "bathroom" dan 10.50 dalam satu statement code
del areas[8:10]
print(areas)


# Expected Output:
# 
# ['hallway',
#  11.25,
#  'kitchen',
#  18.0,
#  'chill zone',
#  20.0,
#  'bedroom',
#  10.75,
#  'poolhouse',
#  24.5,
#  'garage',
#  15.45]
# 
# 

# ## Soal 9: List Comprehension
# 
# Gunakan metode **list comprehension** untuk mencari anggota dari S yang habis di bagi 2, kemudian assign hasilnya dalam bentuk list ke dalam variabel T.

# In[ ]:


S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

T = [ x for x in S if x % 2 == 0]

print(T)


# Expected Output:
# 
# [0, 4, 16, 36, 64]

# # Dictionary

# <h2>Soal 10: Akses Dictionary</h2>
# 
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan

# In[ ]:


europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# print semua key yang ada di objek europe
print (europe.keys())
# print nilai dari key franche
print(europe['france'])


# Expected Output:
# 
# dict_keys(['spain', 'france', 'germany', 'norway'])
# 
# paris

# <h2>Soal 11: Menambahkan key-value baru ke Dictionary</h2>
# 
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan

# In[ ]:


europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# tambahkan key itali ke objek dictionary dengan value roma
europe["italy"]="roma"

# cek apakah itali ada di dalam objek dictionary
print('italy' in europe.keys())


# Expected Output:
#     
# True

# <h2>Soal 12: Update dan Remove Dictinary</h2>
#     
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan

# In[ ]:


europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# update nilai ibukota german ke berlin
europe["germany"] = "berlin"

# remove australia dari europa
europe.pop("australia")

print(europe)


# Expected Output:
# 
# {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw'}

# <h2>Soal 13: Nested Dictionary</h2>
#     
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan

# In[ ]:


country = { 
           'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } 
         }

# berapa populasi dari kota german?
print(country["germany"]["population"])

# update data baru, yaitu negara indonesia dengan capital jakarta dan poulasi 250
country["indonesia"]={'capital':'jakarta','population':250}

print(country)


# Expected Output:
# 
# 80.62
# 
# {'spain': {'capital': 'madrid', 'population': 46.77}, 'france': {'capital': 'paris', 'population': 66.03}, 'germany': {'capital': 'berlin', 'population': 80.62}, 'norway': {'capital': 'oslo', 'population': 5.084}, 'indonesia': {'capital': 'jakarta', 'population': 250}}

# <h2>Soal 14: Loop Dictionary</h2>
#     
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan

# In[ ]:


country = { 
           'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 },
           'indonesia' : {'capital':'jakarta', 'population':250}
         }

for k, v in country.items():
        print("Ibukota", k, "adalah", v["capital"])
    


# Expected Output:
#     
# Ibukota spain adalah madrid
# 
# Ibukota france adalah paris
# 
# Ibukota germany adalah berlin
# 
# Ibukota norway adalah oslo
# 
# Ibukota indonesia adalah jakarta

# 
# <h2>TUGAS TAMBAHAN 1</h2>
# <h3>1. Remove Duplicate List</h3>

# In[ ]:


# solusi tanpa menggunakan set
def remove_duplicate(obj_list):
    new_list = []
    #code Here
    for num in obj_list:
        if num not in new_list:
            new_list.append(num)
    return new_list

# solusi dengan menggunakan set
def remove_duplicate_with_set(obj_list):
    new_list = list(set(obj_list))
    return new_list

#Driver Code
obj_list = [1, 2, 4, 6, 2, 1, 4, 5, 7, 8, 6]
print(remove_duplicate(obj_list))
print(remove_duplicate_with_set(obj_list))


# <h2>TUGAS TAMBAHAN 2</h2>
# <h3>2. Membuat ChatBot Sederhana</h3>

# In[ ]:


# import library
from datetime import datetime
import random

# ganti dengan sebuah nama
nama  = "Nurdeka Hidayanto"
# variabel tanggal
tanggal = datetime.now().day
# default variabel untuk pertanyaan tidak diketahui
default = "maaf, aku tidak tahu jawaban dari pertanyaanmu"

# Membuat objek dictionary berisi berbagai opsi jawaban

# list jawaban untuk pertanyaan tentang nama
jawaban_nama = [
      "nama saya  {0}".format(nama),
      "orang-orang memanggil saya {0}".format(nama),
      "panggil saja saya {0}".format(nama)
   ]

# list jawaban untuk pertanyaan tentang tanggal
jawaban_tanggal = [
      "hari ini tanggal {0}".format(tanggal),
      "ya ampun masa tidak tahu, hari ini tanggal {0}".format(tanggal)
    ]

# opsi pertanyaan yang bisa dijawab
pertanyaan = {
  "nama kamu siapa?": jawaban_nama,
  "kamu siapa?" : jawaban_nama,
  "tanggal berapa hari ini?": jawaban_tanggal,
  "hari ini tanggal berapa?" : jawaban_tanggal,
  "default": default
}

# list jawaban untuk sebuah argument selain pertanyaan
statement =  [
                  'ceritakan lebih banyak!',
                  'kenapa kamu berpikir begitu?',
                  'sudah berapa lama kamu merasa seperti ini?',
                  'Itu sangat menarik!',
                  'oh wow!',
                  ':)'
              ]

# respon keseluruhan
responses = {
    'pertanyaan' : pertanyaan,
    'statement' : statement
}
#------
             
# ayo buat chatbotmu
def chatbot(message):
    if message.endswith('?'):
        if message not in pertanyaan:
            return responses['pertanyaan']['default']
        elif message in pertanyaan:
            return random.choice(responses['pertanyaan'][message])
    else:
        return random.choice(responses['statement'])
    
    
print(chatbot('Selamat Pagi'))
print(chatbot('Mau bermain bersamaku?'))
print(chatbot('nama kamu siapa?'))
print(chatbot('hari ini tanggal berapa?'))


# In[ ]:




