
def eh_palindromo(arr, esq=0, dir=None):
   
    if dir is None:
        dir = len(arr) - 1

    if esq >= dir:
        return True
    if arr[esq] != arr[dir]:
        return False

    return eh_palindromo(arr, esq + 1, dir - 1)
