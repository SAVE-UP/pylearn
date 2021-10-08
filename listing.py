"""
    Cet module contient une fonction qui transfome des iterables en chaine de caractères
"""

def listing(iter, dot ='-'):
    """Listing permet de renvoyer un iterrable: Liste, chaine de caratère sous forme de string"""
    resp = []
    for x in iter:
        resp.append('%s %s ' % (dot, x))
    return '\n'.join(resp)
# import pdb; pdb.set_trace()  # Debugger python - BreakPoint 
