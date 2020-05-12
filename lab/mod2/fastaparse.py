fasta = open('/home/stefano/workspace/kunitz/all_kunitz.fasta', 'r')
fastaout = open('/home/stefano/workspace/kunitz/fastaout', 'w')
for line in fasta:
    if line.startswith('>'):
        uniprot = line.split('|')
        uniprot = uniprot[1]
        line = '>' + uniprot + '\n'
        fastaout.writelines(line)
    else:
        fastaout.writelines(line)