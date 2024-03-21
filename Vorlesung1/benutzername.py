# Liest den Namen eines Benutzers
# liest das Alter
# Gibt darauf aufbauend einen Benutzernamen aus
# z.B. "Andy", "21" -> "Andy21"

name = input("Wie heißt du?")
alter = input("Wie alt bist du?")
benutzername = name + alter
print("Dein Benutzername lautet", benutzername)
print(name, alter)