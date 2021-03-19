listkawan = ['Alam', 'Jefri', 'Nurki', 'Ojat', 'Rahmat', 'Rafi', 'Nauval', 'Hafiz', 'Harry', 'Memed']

print ("Nama teman di indeks ke 4: ", listkawan[4])
print ("Nama teman di indeks ke 6: ", listkawan[6])
print ("Nama teman di indeks ke 7: ", listkawan[7])



listkawan[3] = 'Hani'
print ("list teman baru yang ada di indeks 3: ", listkawan[3])
listkawan[5] = 'Rengga'
print ("list teman baru yang ada di indeks 5: ", listkawan[5])
listkawan[9] = 'Rara'
print ('list teman baru yang ada di indeks 9: ', listkawan[9])

listkawan.append('Raka')
listkawan.append('Hafizh')

for teman in listkawan:
    print("saya mempunyai teman bernama", teman)


len(['Alam', 'Jefri', 'Nurki', 'Ojat', 'Rahmat', 'Rafi', 'Nauval', 'Hafiz', 'Harry', 'Rafli'])

jumlahkawan = (len(listkawan))
print ("teman saya ada", jumlahkawan)