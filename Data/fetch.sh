mkdir "Generated-JSON-Data"
cat $1 | while read i
	echo $i
	do wget "https://maps.googleapis.com/maps/api/geocode/json?address=$i&key=AIzaSyCxmZwaoJo3TW82HylIR2kmVCLCPp7IDV4" -O "Generated-JSON-Data/$i.json"  
	sleep 2
done 