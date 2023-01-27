# Es isograma si no tiene letras repetidas aparte de espacios o guiones
def is_isogram(string):
    # paso a minúsculas y quito espacios y guiones
    str = string.lower().replace(" ", "").replace("-", "")
    return len(str) == len(set(str))
