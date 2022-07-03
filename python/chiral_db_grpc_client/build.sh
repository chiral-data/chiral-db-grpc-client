echo "Download proto file from chiral-db-grpc ..."
curl -O https://raw.githubusercontent.com/chiral-data/chiral-db-grpc/f-docker/proto/chiral_db.proto
echo ""
echo "Generate gPRC code ..."
python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./chiral_db.proto
echo ""
echo "Done!"