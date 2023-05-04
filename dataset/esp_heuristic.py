# === Spanish specific heuristics BEGIN    

nonprefixes_esp = []
nonprefixes_dict_esp={}

common_suffixes_esp = [
               "ar", "ador", "ante", "al", "able", "anza", "ano", "amiento", "ada", "amen", "azo", "ario", "aza"
               "izar", "ificar", "izo", "ino", "ísimo", "idor", "iente", "ente", "il", "ero", "era", "ible", "és", "eño", "ense", "ido", "idad", "ida", "ía", "ismo", "ista", "itud",
               "ecer", "ear", "ecino", "edor", "edor", "eda", "ez", "eza",
               "ción", "cita", "dor", "dora",
               "mente", "mento",
               "na",
               "oso", "ón", "ote", "ota", "ona", 
               "sor", 
               "tor",
               "uzco", "udo", "uda", "ura", "uelo", "uela"
               "yü", "ya"]

common_prefixes_esp = ["a", "an", "ante", "des","de", "pos", "ex", "en", "i", "in", "im"]
common_endings_esp = ["o", "r"]

for v in nonprefixes_esp:
    nonprefixes_dict_esp[v]=1
            
          
def is_good_root_id(part,word):
    return len(part)>3 and is_good_part_generic(part)

def is_good_postfix_id(part):
    if len(part)<=3:
        return is_good_ending_id(part)
    elif len(part)>3:
        return False
    else:
        if not is_good_part_generic(part):
            return False
        return True

def is_good_ending_id(part):
    return part in common_suffixes_id
    
def is_good_prefix_id(part):
    if part in common_prefixes_id:
        return True
    if len(part)>5:
        return False
    return is_good_part_generic(part)
# === Spanish specific  heuristics END

