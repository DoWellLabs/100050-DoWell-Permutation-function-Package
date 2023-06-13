from permutation import Permutation



if __name__ == '__main__':
    perm = Permutation('https://100050.pythonanywhere.com/permutationapi/api/')
    c = perm.retrieve('64876b58d2c3a28a0170d913')
    print(c)