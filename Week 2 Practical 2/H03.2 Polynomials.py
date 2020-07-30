'''Polynomials'''

def eval_polynomial(poly, x):

    result = 0

    for i in range(len(poly)):    
        result += int(poly[i])*x**(len(poly)-i-1)

    print(result)

def add_polynomials(P, Q):
    result_list = []
    if len(Q) > len(P):
        p = Q
        q = P
    else:
        p = P
        q = Q

    for i in range(len(p)):
        try:
            result_list.append(p[i]+q[i])
        except IndexError:
            result_list.append(p[i])
    print(result_list)

def to_latex(P):
    current_power = len(P)-1
    latex_result = ''
    for i in P:
        if i != 0:
            latex_result += '+{0}x^{{{1}}}'.format(i, current_power)
        current_power -= 1
    print(latex_result[1:-5].replace('^{1}', ''))

eval_polynomial([1,2,4], 3)
eval_polynomial([4,5,6,7,8], 2)
add_polynomials([1, 2, 3], [4, 5, -6])
add_polynomials([1], [1, 2, 3, 4])
to_latex([5, 2, 0, 5, 4])
