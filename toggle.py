import reference


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def conversion(s):
    mm = ""
    n = None
    count = 0
    length = len(str(s))
    if length > 1:
        for i in range(length):
            m = str(s)[i]
            if i+1 < length:
                n = str(s)[i+1]
            if n != None and m == n and not m == "(" and not n == "(":
                if m == ")" and n == ")":
                    pass
                else:
                    count += 1
            if n != None and m != n:
                tf_m = is_int(m)
                tf_n = is_int(n)
                if n == "(" or n == ")" and tf_m == True:
                    if n == "(":
                        ss = reference.change_dakuon(m,count)
                        mm += ss
                        count = 0
                    elif n == ")":
                        ss = reference.change_handakuon(m,count)
                        mm += ss
                        count = 0
                elif m == "(" or m == ")" or m == "." and tf_n == True:
                    pass
                else:
                    ss = reference.change(m,count)
                    mm += ss                   
                    count = 0
        if m == n:
            if m == "(" and n == "(":
                return mm
            elif m == ")" and n == ")":
                return mm
            else:
                st = reference.change(m,count-1)
                mm += st
                count = 0
    else:
        st = reference.change(int(s),0)
        print(st)
    return mm

if __name__=='__main__':
    s = input()
    text_str = conversion(s)
    print(text_str)
