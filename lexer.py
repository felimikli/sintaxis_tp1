ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "ESTADO NO FINAL"
ESTADO_TRAMPA = "ESTADO TRAMPA" 

# Lista de tuples del nombre de token y su funcion asociada
# PR -> palabra reservada
# SP -> signo de puntuacion
# OM -> operadores matematicos
# OR -> operadores relacionales
          # ("TOKEN_NUM", afd_num),
          # ("TOKEN_ASIGNACION", afd_asignacion),
          # ("TOKEN_ESPACIOBLANCO", afd_espacioblanco),
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

# TOKENS = [("TOKEN_ID", afd_id), ("TOKEN_NUM", afd_num), ("TOKEN_ASIGNACION", afd_asignacion), ("TOKEN_ESPACIOBLANCO", afd_espacioblanco), ("TOKEN_PR_PROGRAMA", afd_pr_programa), ("TOKEN_PR_VAR", afd_pr_var), ("TOKEN_PR_BEGIN", afd_pr_begin), ("TOKEN_PR_END", afd_pr_end), ("TOKEN_PR_IF", afd_pr_if), ("TOKEN_PR_ELSE", afd_pr_else), ("TOKEN_PR_INT", afd_pr_int), ("TOKEN_PR_BOOL", afd_pr_bool), ("TOKEN_PR_TRUE", afd_pr_true), ("TOKEN_PR_FALSE", afd_pr_false), ("TOKEN_PR_NOT", afd_pr_not), ("TOKEN_PR_AND", afd_pr_and), ("TOKEN_PR_OR", afd_pr_or), ("TOKEN_PR_GOTO", afd_pr_goto), ("TOKEN_PR_LET", afd_pr_let), ("TOKEN_SP_PUNTO", afd_sp_punto), ("TOKEN_SP_COMA", afd_sp_coma), ("TOKEN_SP_DOSPUNTOS", afd_sp_dospuntos), ("TOKEN_SP_PUNTOCOMA", afd_sp_puntocoma), ("TOKEN_SP_PARENTESIS_IZQ", afd_sp_parentesis_izq), ("TOKEN_SP_PARENTESIS_DER", afd_sp_parentesis_der), ("TOKEN_SP_TRIPLEPUNTO", afd_sp_triplepunto), ("TOKEN_OM_MAS", afd_om_mas), ("TOKEN_OM_GUION", afd_om_guion), ("TOKEN_OM_ASTERISCO", afd_om_asterisco), ("TOKEN_OR_MAYOR", afd_or_mayor), ("TOKEN_OR_MENOR", afd_or_menor), ("TOKEN_OR_MAYORIGUAL", afd_or_mayorigual), ("TOKEN_OR_MENORIGUAL", afd_or_menorigual), ("TOKEN_OR_IGUAL", afd_or_igual), ("TOKEN_OR_DESIGUAL", afd_or_desigual)] 



# def afd_id(lexema):
#
# def afd_num(lexema):
#
# def afd_asignacion(lexema):
#
# def afd_espacioblanco(lexema):
#
# def afd_pr_programa(lexema):
#
# def afd_pr_var(lexema):
#
# def afd_pr_begin(lexema):
#
# def afd_pr_end(lexema):
#
# def afd_pr_if(lexema):
#
# def afd_pr_else(lexema):
#
# def afd_pr_int(lexema):
#
# def afd_pr_bool(lexema):
#
# def afd_pr_true(lexema):
#
# def afd_pr_false(lexema):
#
# def afd_pr_not(lexema):
#
# def afd_pr_and(lexema):
#
# def afd_pr_or(lexema):
#
# def afd_pr_goto(lexema):
#
# def afd_pr_let(lexema):
#
# def afd_sp_punto(lexema):
#
# def afd_sp_coma(lexema):
#
# def afd_sp_dospuntos(lexema):
#
# def afd_sp_puntocoma(lexema):
#
# def afd_sp_parentesis_izq(lexema):
#
# def afd_sp_parentesis_der(lexema):
#
# def afd_sp_triplepunto(lexema):
#
# def afd_om_mas(lexema):
#
# def afd_om_guion(lexema):
#
# def afd_om_asterisco(lexema):
#
# def afd_or_mayor(lexema):
#
# def afd_or_menor(lexema):
#
# def afd_or_mayorigual(lexema):
#
# def afd_or_menorigual(lexema):
#
# def afd_or_igual(lexema):
#
# def afd_or_desigual(lexema):



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
