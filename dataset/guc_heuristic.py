# === Wayuunaiki specific heuristics BEGIN    

nonprefixes_guc = []
nonprefixes_dict_guc={}

common_suffixes_guc = [
               "a", "chi", 
               "i", "iwa", "ira", "irü", "inja", "inka", "iwa’aya", "ja", "ee",
               "kalaka",
               "le"
               "muyuu", "ma’a",
               "na",
               "püta", "pa", "pütü", "pü",
               "sü", "shi", 
               "tü", "tüjü", 
               "wan", 
               "yü", "ya"]

common_prefixes_guc = ["a", "pü", "ta", "wa"]
common_endings_guc = ["n", "a"]

for v in nonprefixes_guc:
    nonprefixes_dict_guc[v]=1
            
def is_good_root_guc(part,word):
    return len(part)>3 and is_good_part_generic(part)
    
def is_good_postfix_guc(part):
    if len(part)<=3:
        return is_good_ending_guc(part)
    elif len(part)>3:
        return False
    else:
        if not is_good_part_generic(part):
            return False
        return True

def is_good_ending_guc(part):
    return part in common_suffixes_guc
    
def is_good_prefix_guc(part):
    if part in common_prefixes_guc:
        return True
    if len(part)>5:
        return False
    return is_good_part_generic(part)

# === Wayuunaiki specific  heuristics END

