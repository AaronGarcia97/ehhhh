def getTable(registrationType) :
    if ( registrationType == 'U' ) :
        return "Cliente"
    elif ( registrationType == 'T' ) :
        return "Taxista"
    elif ( registrationType == 'A' ) :
        return "Admin"
    else :
        return "None"
