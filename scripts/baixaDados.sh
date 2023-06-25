

for line in $(cat emotiondata.txt); do
    wget $line
done