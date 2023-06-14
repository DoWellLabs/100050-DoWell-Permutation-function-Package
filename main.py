from permutation import Permutation



if __name__ == '__main__':
    perm = Permutation('https://100050.pythonanywhere.com/permutationapi/api/')
    c = perm.find(5,3, 'A')
    print(c)