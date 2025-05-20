from os import system as limp
limp('cls')

curso="pYtHon"
print(curso.upper())
print(curso.lower())
print(curso.title())

curso="    Python  "
print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())

curso="Python"
print(curso.center(10,"#"))
print(".".join(curso))