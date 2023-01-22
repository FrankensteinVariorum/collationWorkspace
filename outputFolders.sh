# for i in collationChunks/*/
# do
#    mkdir $i/output
# done

for i in collationChunks/*/output/
do
    touch $i/Readme.md
done