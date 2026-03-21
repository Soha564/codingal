def generate_parentheses(o_p, c_p, s, n):
    if len(s) == 2*n:
        print(s)
        return
    if o_p < n:
        generate_parentheses(o_p +1, c_p, s +"(", n)
    if c_p < o_p:
        generate_parentheses(o_p, c_p + 1, s +")", n)
n = int(input("Enter a number of pairs: "))
generate_parentheses(0,0,"", n)