#how to use this 

curl -X POST -F "file=@ips.csv"  http://127.0.0.1:5000/careerbaba/trian

curl -X POST -F "file=@row_data.csv"  http://127.0.0.1:5000/careerbaba/testtrian


curl -X POST -F "file=@ips.csv"  http://127.0.0.1:5000/careerbaba/testtrian

curl -X POST -F "file=@/path/example.gif" http://127.0.0.1:5000/uploadform.cgi

curl -X POST -F "name=user" -F "password=test" http://127.0.0.1:5000/example.php

curl -d "data=example1&data2=example2" http://127.0.0.1:5000/example.cgi

curl -X POST -F "name=user" -F "password=test" http://127.0.0.1:5000/example.php

curl http://127.0.0.1:5000/careerbaba/recommandation