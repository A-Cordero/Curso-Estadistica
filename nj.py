#planchita
#https://www.rcsb.org/structure/1ALU
a)comparacion visual
b)comparacion de angulos de torsion(dihedral angles)
se comparan los angulos de torsion
c)distancia matrix - es la matriz de distancias entre los diferentes aminoacidos de una proteina
d) RMSD =-  se calcula el root mean squeare distance de atomos
correspondiente de 2 proteinas a,b




from datetime import datetime
from os.path import realpath, isfile
from os import name
from os import remove
import sys
from Bio import AlignIO
from Bio import Phylo
from Bio.Align import MultipleSeqAlignment
from Bio.Alphabet import generic_protein
from Bio.Blast import NCBIXML
from Bio.Blast.NCBIWWW import qblast as blast 
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Align.Applications import ClustalwCommandline

import pylab

def CargarFicheroFasta():
    #Carga fichero fasta ''
    
    ret = None, None, None
    
    try:
        #nomfich nombre del fichero
        nomfich = 'protsec.fasta'
       
        # Se abre fichero de proteina en formato FASTA. 
        f = open(nomfich, 'r')
        #una sola secuencia
        proteina = AligIO.read(open("nombre"), "fasta")
        #varias secuencias
        proteina = SeqIO.read(f,"fasta")
        # Recuperamos identificador y la secuencia.        
        prot_id = proteina.id
        print prot_id

        prot_secuencia = proteina.seq
        # Datos.
        ret = prot_id, prot_secuencia, nomfich
        # Info.
        print 'Cargado fichero %s' % nomfich
    
    except:
        print 'Ha habido un error al intentar cargar el fichero FASTA'
    
    # Devolvemos datos.
    return ret
          
def GenerarArbol():
    #Generacion de arbol filogenetico UPGMA 
    alineamientos = AlignIO.read("protsec.aln","clustal")  

    # Calculamos matriz de distancias.
    calculo_matriz = DistanceCalculator('identity')
   
    matriz_distancia = calculo_matriz.get_distance(alineamientos)
    print matriz_distancia
    # Creamos el arbol UPGMA.
    creador_arbol = DistanceTreeConstructor()
    arbol_UPGMA =creador_arbol.nj(matriz_distancia)
    Phylo.draw_ascii(arbol_UPGMA)
    Phylo.draw(arbol_UPGMA)

      
def main():
        
    # Nombre de fichero de proteina.
    F_PROTEINA = None
    # Identificador y secuencia de proteina.
    PROT_ID = None
    PROT_SECUENCIA = None
    
   #  Cargar proteina
    #PROT_ID, PROT_SECUENCIA, F_PROTEINA = CargarFicheroFasta()                
    # Generar arbol filogenetico UPGMA.
    GenerarArbol()        

      
main()


A - u
U - A o G
C - G
G - u o C