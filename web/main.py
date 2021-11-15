# web/main.py
import os

from flask import Flask, render_template
import grpc

from aiscore_pb2 import AISocreRequest
from aiscore_pb2_grpc import ScoreResultStub

app = Flask(__name__)

scoreresult_host = os.getenv("AISCORE_HOST", "localhost")
scoreresult_channel = grpc.insecure_channel(f"{scoreresult_host}:50051")
scoreresult_client = ScoreResultStub(scoreresult_channel)

@app.route("/")
def render_homepage():
    scoreresult_request = AISocreRequest(user_id=1, deposit=0, age=35)
    scoreresult_response = scoreresult_client.GetAISocre(scoreresult_request)
    
    return render_template("index.html",scoreresult=scoreresult_response.score_data)
