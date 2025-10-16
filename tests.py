from lexer import *
# Pruebas
tests = [
        #Test 0 
        '''
var afd: hola + mundo
''',
        # Test 1
        '''
var x: (-100...200) = 0
var y: bool = true
begin:
        if y == not false
                goto L1;
        else
                goto L2;
L1: x = x * x;
    x = x + 2;
L2: x = 2 * x;
    x = x -3
end
''',
        # Test 2
        '''
vad numero: (-100...200) = 0
        ''',
        # Test 3
        '''
var __: bool = true
''',
    #Test 4
    '''
var x: int = 4
if x == 4 or x >= 5
    x = x * 2

''',
    #Test 5
    ''' 
    var gama: = beta 
befin: 
     if( gama=beta ){
        game != alfa
     }
''',
    #Test 6
    '''
5 > 4 < 14 != 24
''',  
    #Test 7
    '''
@ += var let --
program
''',
    #Test 8
    '''
begin program:
    var v1: 
    8--9+32 === 5
    end
''',
    #Test 9 
    '''
1palabra 
    programa end else: true,not and:: let. ... ;*< >= <= 
    <>,. qjgfquhg
    end
''',
    # Test 10
    '''
begin program:
        var number: (-100...200) = 1
        if number == 1:
                end;
'''
]
f = open("output.txt", "w")
for i in range(len(tests)):
        print(f'=========== TEST N:{i} =========', file=f)
        print(tests[i], file=f)
        print(f'----OUTPUT----', file=f)
        print(tokenizer(tests[i]), file=f)
        print("", file=f)


