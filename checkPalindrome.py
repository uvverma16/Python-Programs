def check_palindrome(str_list):
    res = []
    for str in str_list:
        if str[::-1].lower()==str.lower():
            res.append(str)
    return res

if __name__=='__main__':
    count = int(input())
    inp_str = []
    for i in range(count):
        inp_str.append(input())
    output = check_palindrome(inp_str)
    if len(output)!= 0:
        for i in output:
            print(i)
    else:
        print('No palindroe found')
