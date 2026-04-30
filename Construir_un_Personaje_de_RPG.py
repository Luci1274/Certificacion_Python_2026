full_dot = '●'
empty_dot = '○'

def create_character(nombre, fuerza, inteligencia, carisma):
    total_dot = 10

    if not isinstance(nombre, str):
        return "The character name should be a string"
    if nombre == "":
        return "The character should have a name"
    if len(nombre) > 10:
        return "The character name is too long"
    if " " in nombre:
        return "The character name should not contain spaces"

    if not isinstance(fuerza, int) or not isinstance(inteligencia, int) or not isinstance(carisma, int):
        return "All stats should be integers"
    if fuerza < 1 or inteligencia < 1 or carisma < 1:
        return "All stats should be no less than 1"
    if fuerza > 4 or inteligencia > 4 or carisma > 4:
        return "All stats should be no more than 4"
    if fuerza + inteligencia + carisma != 7:
        return "The character should start with 7 points"

    full_dot_STR = full_dot * fuerza
    full_dot_INT = full_dot * inteligencia
    full_dot_CHA = full_dot * carisma

    empty_dotSTR = total_dot - fuerza
    empty_dotINT = total_dot - inteligencia
    empty_dotCHA = total_dot - carisma

    hoja_personaje = f"{nombre}\nSTR {full_dot_STR + empty_dot * empty_dotSTR}\nINT {full_dot_INT + empty_dot * empty_dotINT}\nCHA {full_dot_CHA + empty_dot * empty_dotCHA}"
    
    return hoja_personaje