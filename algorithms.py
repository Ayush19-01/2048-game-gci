import random
def new1(n):
    matrix = []

    for i in range(n):
        matrix.append([0] * n)
    return matrix

def up(game):
    game = transpose(game)
    game, done = covered(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = covered(game)[0]
    game = transpose(game)
    return (game, done)


def down(game):
    game = reverse(transpose(game))
    game, done = covered(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = covered(game)[0]
    game = transpose(reverse(game))
    return (game, done)


def left(game):
    game, done = covered(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = covered(game)[0]
    return (game, done)


def right(game):
    game = reverse(game)
    game, done = covered(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = covered(game)[0]
    game = reverse(game)
    return (game, done)


def reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0])-j-1])
    return new
def transpose(mat):
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new

def covered(mat):
    new = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    done = False
    for i in range(4):
        count = 0
        for j in range(4):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return (new, done)


def merge(mat):
    done = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                done = True
    return (mat, done)

def status(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return 'win'
    for i in range(len(mat)-1):
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'not over'
    for i in range(len(mat)): 
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'
    for k in range(len(mat)-1):
        if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
            return 'not over'
    for j in range(len(mat)-1):
        if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
            return 'not over'
    return 'lose'
def addition(mat):
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)
    while mat[a][b] != 0:
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)
    mat[a][b] = 2
    return mat


