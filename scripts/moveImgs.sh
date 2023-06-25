#mkdir ../data_emotionet/test/
EXP="anger"
for file in $(ls /home/carlos/UFPR/tcc/tcc-carloscichon/affectnet_data_gray/$EXP | shuf -n 1000); do
    mv /home/carlos/UFPR/tcc/tcc-carloscichon/data2/$EXP/$file /home/carlos/UFPR/tcc/tcc-carloscichon/affectnet_data_test/$EXP/$file
done