FROM python:3.9

RUN mkdir /service
WORKDIR /service/web
COPY web/requirements.txt /service/web/requirements.txt

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY protobufs/ /service/protobufs/
COPY web/ /service/web/
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/aiscore.proto

EXPOSE 5000
ENV FLASK_APP=main.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
