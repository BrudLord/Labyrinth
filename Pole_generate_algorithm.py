import Variables as var


def generate_pole(size, colors):
    # Пока пусть возвращает это поле, потом добавим алгоритм
    colors = list(var.COLOR_VALUE.keys())[: colors]
    pole = [
        [['s', 'b', 'n', 's'], ['s', 'b', 'n', 'b'], ['s', 'r', 'n', 'b'], ['s', 'b', 'g', 'r'], ['s', 'r', 'n', 'b'],
         ['s', 's', 'r', 'r']],
        [['n', 'r', 'b', 's'], ['n', 'r', 'n', 'r'], ['n', 'g', 'b', 'r'], ['g', 'b', 'r', 'g'], ['n', 'g', 'n', 'b'],
         ['r', 's', 'b', 'g']],
        [['b', 'g', 'n', 's'], ['n', 'b', 'n', 'g'], ['b', 'b', 'g', 'b'], ['r', 'g', 'r', 'b'], ['n', 'r', 'n', 'g'],
         ['b', 's', 'n', 'r']],
        [['n', 'r', 'b', 's'], ['n', 'b', 'g', 'r'], ['g', 'n', 'r', 'b'], ['r', 'b', 'n', 'n'], ['n', 'n', 'g', 'b'],
         ['n', 's', 'g', 'n']],
        [['b', 'r', 's', 's'], ['g', 'b', 's', 'r'], ['r', 'b', 's', 'b'], ['n', 'g', 's', 'b'], ['g', 'r', 's', 'g'],
         ['g', 's', 's', 'r']]]
    return pole, colors