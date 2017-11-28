
####For exporting the disk usage data of all directories####

SEPARATOR=","
SIZES=`df -h | awk '{print $1","$2","$3","$4","$5","$6}'`
echo `date +%Z-%Y-%m-%d_%H-%M-%S` "$SIZES" >> test.csv


####For exporting the disk usage data of one directory####

#SEPARATOR=","
#SIZES=`df -h | awk -v SEP="$SEPARATOR" 'FNR == 2 {print SEP$2SEP$3SEP$4}'`
#echo `date +%Z-%Y-%m-%d_%H-%M-%S` "$SIZES" >> test.csv

