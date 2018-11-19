import re
r1 = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
# it wouldn't match anything and return NoneType
r2 = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')

def judge():
    test = input('Input your name')
    if re.match(r'your_regular_expression', test):
        print('Matched!')
    else:
        print('Failed!')

def string_split():
    s = 'a b   c'
    # it cannot recogonize continous blankspaces
    s1 = s.split(' ')
    # re.split can recogonize a regular expression,
    # which means it can recogonize the continuous blankspaces
    # and also other regular expressions
    s2 = re.split(r'\s+', s)
    s3 = re.split(r'[\s\,]', 'a,b, c d')
    s4 = re.split(r'[\s\,\;]', 'a,b;; c, d ;')

def the_groups():
    g = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
    print(g.groups())
    print(g.group(0), g.group(1), g.group(2))

def greedy():
    g1 = re.match(r'^(\d+)(0*)$', '1023000').groups()
    g2 = re.match(r'^(\d+?)(0*)$', '1023000').groups()
    print(g1, '\n', g2)

def do_compile():
    compiled_re = re.compile(r'^(\d{3})-(\d{3,8})$')
    r1 = compiled_re.match('010-12345').groups()
    r2 = compiled_re.match('022-5677').groups()
    print(r1, '\n', r2)

# someone@gmail.com
# bill.gates@microsoft.com
# <Tom Paris> tom@voyager.org

