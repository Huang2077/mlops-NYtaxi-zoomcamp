mlflow server \
    -h 0.0.0.0 \
    -p 5000 \
    --backend-store-uri 'postgresql://mlflow:N*-tsW#KWDeu6d.$Wj0xnIoXB_it@mlflow-database.c7i8oqsckxyp.ap-northeast-1.rds.amazonaws.com:5432/mlflow_db' \
    --default-artifact-root s3://huangmlops

