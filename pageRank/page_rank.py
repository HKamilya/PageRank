import csv

import numpy

from matrix_generator import matrix_from_graph


def summary_page_rank(matrix, height, width, G_LIST):
    n = height
    POW = 20
    beta = 0.85
    k = (1 - beta) / n
    # исходная матрица
    M_matrix = matrix

    # вектор
    v_vector = numpy.matrix([1 / n for i in range(height)])

    M_matrix_powed = M_matrix

    # исходная матрица умноженная на beta
    v_vector.dot(M_matrix_powed)

    # возведение матрицы в степень, определение вектора итераций
    for i in range(POW):
        M_matrix_powed.dot(M_matrix)

    M_matrix_final = v_vector.dot(M_matrix_powed)
    MATRIX_RESULT_MxVxB = M_matrix_final.dot(beta)

    # единичная матрица
    e = numpy.ones(height)

    e = e.dot(k)
    result = MATRIX_RESULT_MxVxB + e

    print(result)
    print(result.sum())

    # вывод топ 7 ссылок
    get_top(result, G_LIST, 7)


def get_top(result, G_list, top):
    a_ = numpy.sort(result).tolist()[0]

    a_ = a_[-top:]
    b_ = numpy.argsort(result).tolist()[0][-top:]
    G_list = list(G_list)
    arr = []
    for i in range(top):
        arr.append(
            f"{top - i} {a_[i]} {G_list[b_[i]]}"
        )

    print('result page rank')
    print(result.sum())

    print('----------')
    print('top', top)
    for i in arr:
        print(i)


if __name__ == '__main__':
    matrix, height, width, G_LIST = matrix_from_graph()
    summary_page_rank(matrix, height, width, G_LIST)
