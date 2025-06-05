ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "ESTADO NO FINAL"
ESTADO_TRAMPA = "ESTADO TRAMPA" 

LETRAS_MIN = set("abcdefghijklmnopqrstuvwxyz")
LETRAS_MAY = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
NUMEROS = set("0123456789")

# Lista de tuples del nombre de token y su funcion asociada
# PR -> palabra reservada
# SP -> signo de puntuacion
# OM -> operadores matematicos
# OR -> operadores relacionales
          # ("TOKEN_ID", afd_id),
          # ("TOKEN_NUM", afd_num),
          # ("TOKEN_ESPACIOBLANCO", afd_espacioblanco),
          # ("TOKEN_ASIGNACION", afd_asignacion),
          #
          # ("TOKEN_PR_PROGRAMA", afd_pr_programa),
          # ("TOKEN_PR_VAR", afd_pr_var),
          # ("TOKEN_PR_BEGIN", afd_pr_begin),
          # ("TOKEN_PR_END", afd_pr_end),
          # ("TOKEN_PR_IF", afd_pr_if),
          # ("TOKEN_PR_ELSE", afd_pr_else),
          # ("TOKEN_PR_INT", afd_pr_int),
          # ("TOKEN_PR_BOOL", afd_pr_bool),
          # ("TOKEN_PR_TRUE", afd_pr_true),
          # ("TOKEN_PR_FALSE", afd_pr_false),
          # ("TOKEN_PR_NOT", afd_pr_not),
          # ("TOKEN_PR_AND", afd_pr_and),
          # ("TOKEN_PR_OR", afd_pr_or),
          # ("TOKEN_PR_GOTO", afd_pr_goto),
          # ("TOKEN_PR_LET", afd_pr_let),
          #
          # ("TOKEN_SP_PUNTO", afd_sp_punto),
          # ("TOKEN_SP_COMA", afd_sp_coma),
          # ("TOKEN_SP_DOSPUNTOS", afd_sp_dospuntos),
          # ("TOKEN_SP_PUNTOCOMA", afd_sp_puntocoma),
          # ("TOKEN_SP_PARENTESIS_IZQ", afd_sp_parentesis_izq),
          # ("TOKEN_SP_PARENTESIS_DER", afd_sp_parentesis_der),
          # ("TOKEN_SP_TRIPLEPUNTO", afd_sp_triplepunto),
          #
          # ("TOKEN_OM_MAS", afd_om_mas),
          # ("TOKEN_OM_GUION", afd_om_guion),
          # ("TOKEN_OM_ASTERISCO", afd_om_asterisco),
          #
          # ("TOKEN_OR_MAYOR", afd_or_mayor),
          # ("TOKEN_OR_MENOR", afd_or_menor),
          # ("TOKEN_OR_MAYORIGUAL", afd_or_mayorigual),
          # ("TOKEN_OR_MENORIGUAL", afd_or_menorigual),
          # ("TOKEN_OR_IGUAL", afd_or_igual),
          # ("TOKEN_OR_DESIGUAL", afd_or_desigual),



def afd_palabra(lexema, palabra):
        length_lexema = len(lexema)
        length_palabra = len(palabra)

        if(length_lexema > length_palabra):
                return ESTADO_TRAMPA
        
        estado = 0
        estados_finales = [length_palabra]
        # Lista de dicts describe funcion de estados
        funcion_estados = []

        for i, c  in enumerate(palabra):
                funcion_estados.append({c: (i + 1)})

        for char in lexema:
                transicion = funcion_estados[estado]
                if char in transicion:
                        estado = transicion[char]
                else:
                        return ESTADO_TRAMPA

        if estado in estados_finales:
                return ESTADO_FINAL
        else:
                return ESTADO_NO_FINAL

def afd_id(lexema):
        estado = 0
        estados_finales = [1]
        funcion_estados = [{},{}]
        for c in LETRAS_MIN | LETRAS_MAY:
                funcion_estados[0][c] = 1
                funcion_estados[1][c] = 1
        for c in NUMEROS:
                funcion_estados[1][c] = 1

        for char in lexema:
                transicion = funcion_estados[estado]
                if char in transicion:
                        estado = transicion[char]
                else:
                        return ESTADO_TRAMPA

        if estado in estados_finales:
                return ESTADO_FINAL
        else:
                return ESTADO_NO_FINAL


def afd_num(lexema):
        estado = 0
        estados_finales = [2]
        funcion_estados = [{}, {}, {}]
        funcion_estados[0]['-'] = 1
        
        for c in NUMEROS:
                funcion_estados[0][c] = 2
                funcion_estados[1][c] = 2
                funcion_estados[2][c] = 2

        for char in lexema:
                transicion = funcion_estados[estado]
                if char in transicion:
                        estado = transicion[char]
                else:
                        return ESTADO_TRAMPA

        if estado in estados_finales:
                return ESTADO_FINAL
        else:
                return ESTADO_NO_FINAL

def afd_espacioblanco(lexema):
        estado = 0
        estados_finales = [1]
        funcion_estados = [{}, {}]
        funcion_estados[0][' '] = 1
        funcion_estados[0]['\n'] = 1
        funcion_estados[0]['\t'] = 1
        funcion_estados[0]['\r'] = 1
        funcion_estados[1][' '] = 1
        funcion_estados[1]['\n'] = 1
        funcion_estados[1]['\t'] = 1
        funcion_estados[1]['\r'] = 1
        

        for char in lexema:
                transicion = funcion_estados[estado]
                if char in transicion:
                        estado = transicion[char]
                else:
                        return ESTADO_TRAMPA

        if estado in estados_finales:
                return ESTADO_FINAL
        else:
                return ESTADO_NO_FINAL


def afd_asignacion(lexema):
        return afd_palabra(lexema, "=")

def afd_pr_programa(lexema):
        return afd_palabra(lexema, "programa")

def afd_pr_var(lexema):
        return afd_palabra(lexema, "var")

def afd_pr_begin(lexema):
        return afd_palabra(lexema, "begin")

def afd_pr_end(lexema):
        return afd_palabra(lexema, "end")

def afd_pr_if(lexema):
        return afd_palabra(lexema, "if")

def afd_pr_else(lexema):
        return afd_palabra(lexema, "else")

def afd_pr_int(lexema):
        return afd_palabra(lexema, "int")

def afd_pr_bool(lexema):
        return afd_palabra(lexema, "bool")

def afd_pr_true(lexema):
        return afd_palabra(lexema, "true")

def afd_pr_false(lexema):
        return afd_palabra(lexema, "false")

def afd_pr_not(lexema):
        return afd_palabra(lexema, "not")

def afd_pr_and(lexema):
        return afd_palabra(lexema, "and")

def afd_pr_or(lexema):
        return afd_palabra(lexema, "or")

def afd_pr_goto(lexema):
        return afd_palabra(lexema, "goto")

def afd_pr_let(lexema):
        return afd_palabra(lexema, "let")

def afd_sp_punto(lexema):
        return afd_palabra(lexema, ".")

def afd_sp_coma(lexema):
        return afd_palabra(lexema, ",")

def afd_sp_dospuntos(lexema):
        return afd_palabra(lexema, ":")

def afd_sp_puntocoma(lexema):
        return afd_palabra(lexema, ";")

def afd_sp_parentesis_izq(lexema):
        return afd_palabra(lexema, "(")

def afd_sp_parentesis_der(lexema):
        return afd_palabra(lexema, ")")

def afd_sp_triplepunto(lexema):
        return afd_palabra(lexema, "...")

def afd_om_mas(lexema):
        return afd_palabra(lexema, "+")

def afd_om_guion(lexema):
        return afd_palabra(lexema, "-")

def afd_om_asterisco(lexema):
        return afd_palabra(lexema, "*")

def afd_or_mayor(lexema):
        return afd_palabra(lexema, ">")

def afd_or_menor(lexema):
        return afd_palabra(lexema, "<")

def afd_or_mayorigual(lexema):
        return afd_palabra(lexema, ">=")

def afd_or_menorigual(lexema):
        return afd_palabra(lexema, "<=")

def afd_or_igual(lexema):
        return afd_palabra(lexema, "==")

def afd_or_desigual(lexema):
        return afd_palabra(lexema, "<>")

TOKENS = [("TOKEN_ID", afd_id), ("TOKEN_NUM", afd_num), ("TOKEN_ASIGNACION", afd_asignacion), ("TOKEN_ESPACIOBLANCO", afd_espacioblanco), ("TOKEN_PR_PROGRAMA", afd_pr_programa), ("TOKEN_PR_VAR", afd_pr_var), ("TOKEN_PR_BEGIN", afd_pr_begin), ("TOKEN_PR_END", afd_pr_end), ("TOKEN_PR_IF", afd_pr_if), ("TOKEN_PR_ELSE", afd_pr_else), ("TOKEN_PR_INT", afd_pr_int), ("TOKEN_PR_BOOL", afd_pr_bool), ("TOKEN_PR_TRUE", afd_pr_true), ("TOKEN_PR_FALSE", afd_pr_false), ("TOKEN_PR_NOT", afd_pr_not), ("TOKEN_PR_AND", afd_pr_and), ("TOKEN_PR_OR", afd_pr_or), ("TOKEN_PR_GOTO", afd_pr_goto), ("TOKEN_PR_LET", afd_pr_let), ("TOKEN_SP_PUNTO", afd_sp_punto), ("TOKEN_SP_COMA", afd_sp_coma), ("TOKEN_SP_DOSPUNTOS", afd_sp_dospuntos), ("TOKEN_SP_PUNTOCOMA", afd_sp_puntocoma), ("TOKEN_SP_PARENTESIS_IZQ", afd_sp_parentesis_izq), ("TOKEN_SP_PARENTESIS_DER", afd_sp_parentesis_der), ("TOKEN_SP_TRIPLEPUNTO", afd_sp_triplepunto), ("TOKEN_OM_MAS", afd_om_mas), ("TOKEN_OM_GUION", afd_om_guion), ("TOKEN_OM_ASTERISCO", afd_om_asterisco), ("TOKEN_OR_MAYOR", afd_or_mayor), ("TOKEN_OR_MENOR", afd_or_menor), ("TOKEN_OR_MAYORIGUAL", afd_or_mayorigual), ("TOKEN_OR_MENORIGUAL", afd_or_menorigual), ("TOKEN_OR_IGUAL", afd_or_igual), ("TOKEN_OR_DESIGUAL", afd_or_desigual)] 

def tokenizer(fuente):
        tokens_return = [] # Lista de tokens final a pasar al parser
        puntero = 0 # apunta a posician actual en el codigo fuente
        while puntero < len(fuente):
                comienzo_lexema = puntero 
                lexema = ""
                trampa = False
                token_candidato = None
                ultimo_puntero = puntero

                while not trampa and puntero < len(fuente):
                        lexema += fuente[puntero]
                        puntero += 1

                        posibles_tokens = [] # por cada lexema, puede haber varios afd en estado no aceptado, pero no trampa. 
                        posibles_tokens_aceptados = [] # por cada lexema, puede haber varios afd en estado.

                        for (token_nombre, afd) in TOKENS:
                                estado_actual = afd(lexema)
                                if estado_actual == ESTADO_NO_FINAL:
                                        posibles_tokens.append(token_nombre)
                                if estado_actual == ESTADO_FINAL:
                                        posibles_tokens_aceptados.append(token_nombre)
                        
                        if(posibles_tokens_aceptados):
                                token_candidato = posibles_tokens_aceptados[-1] # si hay algun afd en estado aceptado, se guarda en token candidato, priorizando todo antes de ID
                                ultimo_puntero = puntero 
                        elif(not posibles_tokens):
                                trampa = True # si no hay ningun afd en estado no aceptado ni en estado aceptado, estan todos en trampa

                if(token_candidato): # si hay un token candidato luego de estar todos en trampa
                        token = (token_candidato, fuente[comienzo_lexema:ultimo_puntero]) # el token candidato y su lexema
                        tokens_return.append(token)
                        # el ultimo puntero no se actualiza si todos los estados pasan a estado trampa
                        puntero = ultimo_puntero # "retrocedemos el puntero al ultimo puntero
                else:
                        raise Exception('Error: token no pertenece al lenguaje' + lexema)
        return tokens_return

print(tokenizer(input("ingresa codigo fuente prueba: ")))
