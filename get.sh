fname=kct-$(date +%F_%H:%M)
echo "Start stream download"
mimms -t 684 "mms://121.167.43.161/chosun" $fname
echo "End stream download"
echo "Start chunking"
./chunk.sh $fname
