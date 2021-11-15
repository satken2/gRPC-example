FROM python:3.9

RUN mkdir /service
WORKDIR /service/app
COPY app/requirements.txt /service/app/requirements.txt

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY protobufs/ /service/protobufs/
COPY app/ /service/app/
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/aiscore.proto

EXPOSE 50051
ENTRYPOINT [ "python", "main.py" ]