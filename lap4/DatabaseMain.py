from The_Database import connect, selectfromtable, inserttrainee, updatetrainee, deletetrainee

(updatetrainee(2, "Nirmen", 25, 'CSS'))

connect()
print(selectfromtable("track"))
print(selectfromtable("trainee"))
inserttrainee(4, "Nabil", 25, "Python")
deletetrainee(4)