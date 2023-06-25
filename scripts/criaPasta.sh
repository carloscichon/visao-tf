PATH2="/home/carlos/UFPR/tcc/tcc-carloscichon/affectnet_data_gray_test/"

DIRS="surprise contempt disgust fear anger sad"

for d in $DIRS; do
rm $PATH2$d/low
rm $PATH2$d/con
rm $PATH2$d/bright
rm $PATH2$d/flip
#mv $PATH2$d/low/* $PATH2$d
#mv $PATH2$d/flip/* $PATH2$d
#mv $PATH2$d/bright/* $PATH2$d
#mv $PATH2$d/con/* $PATH2$d
#mkdir $PATH2$d/con/
#mkdir $PATH2$d/low/
#mkdir $PATH2$d/bright/
#mkdir $PATH2$d/flip/
done