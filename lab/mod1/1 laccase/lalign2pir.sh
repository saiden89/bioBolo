#!/bin/bash

#########################################################################################################
#													#
#						LALIGN2PIR						#
#													#
#				     A simple lalign to pir converter					#
#													#
#													#
#						  BEWARE						#
#				   This is a proof of concept script.              			#
#			   It's quick and dirty, could work but can have bugs.				#
# 		This script has been created fot the Course of Laboratory of Bioinformatics 1		#
# 			 International Master in Bioinformatics; University of Bologna			#
#													#
# usage:  ./lalign2pir.sh <FileFromLalign> <NameOfFirstProtein> <NameOfSecondProtein> <OutputFile.pir>	#
# example ./lalign2pir.sh lalign.txt 1GYC B0JDP9 output.pir						#
#													#
# Created by: 	Francesco Aggazio 	- 2015								#
# Edited by:	Davide Baldazzi 	- 2019 								#
#													#
#########################################################################################################

LALIGNFILE=$1	# Output from LALIGN saved locally in .txt format
PNAME1=$2	# Target Protein Name
PNAME2=$3	# Template Protein Name
OUTFILE=$4	# Output file (.pir format)

if [ "$1" == '-h' ] || [ "$1" == '--help' ]; then
	echo '#########################################################################################################'
	echo '#													#'
	echo '#						LALIGN2PIR						#'
	echo '#													#'
	echo '#				     A simple lalign to pir converter					#'
	echo '#													#'
	echo '#													#'
	echo '#						  BEWARE						#'
	echo '#				   This is a proof of concept script.              			#'
	echo "#			   It's quick and dirty, could work but can have bugs.				#"
	echo '# 		This script has been created fot the Course of Laboratory of Bioinformatics 1		#'
	echo '# 			 International Master in Bioinformatics; University of Bologna			#'
	echo '#													#'
	echo '# usage:  ./lalign2pir.sh <FileFromLalign> <NameOfFirstProtein> <NameOfSecondProtein> <OutputFile.pir>	#'
	echo '# example ./lalign2pir.sh lalign.txt 1GYC B0JDP9 output.pir						#'
	echo '#													#'
	echo '# Created by: 	Francesco Aggazio 	- 2015								#'
	echo '# Edited by:	Davide Baldazzi 	- 2019 								#'
	echo '#													#'
	echo '#########################################################################################################'
	exit
fi;

# Target Sequence

echo ">P1;"$2 > $4							# Write the Header for the Target Protein
echo "structureX:"$2"::::::::" >> $4					# Write Information line for the Target Protein
cat $LALIGNFILE | grep -E '^'$2'[ ]+[A-Za-z\-]+' | awk '{print $2}' >> $4	# Extract Aligned sequence of the Target Protein and copy to output file

echo >> $4								# Write an empty line

# Template Sequence

echo ">P1;"$3 >> $4							# Write the Header for the Template Protein
echo "structureX:"$3"::::::::" >> $4					# Write Information line for the Template Protein
cat $LALIGNFILE | grep -E '^'$3'[ ]+[A-Za-z\-]+' | awk '{print $2}' >> $4	# Extract Aligned sequence of the Template Protein and copy to output file

