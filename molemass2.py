def molemass2(sequence):
#Sym=Atomic Symbols
#MW=Molecular Weight
    TotalAtomicMass=0
    Sym=["F","K","S","P","O","N","C","H"]
    MW=[18.9984,39.0983,32.0660,30.9738,15.9994,14.0067,12.0107,1.0079]
    Atoms_dict=dict(zip(Sym,MW))
#use the isdigit() function to figure which parts of the strings are numbers and which are atomic symbols
    for i in range(len(sequence)):
        if sequence[i].isdigit()==True:
            TotalAtomicMass+=Atoms_dict[sequence[i-1]]*(int(sequence[i])-1)
        else:
            TotalAtomicMass+=Atoms_dict[sequence[i]]
    return TotalAtomicMass