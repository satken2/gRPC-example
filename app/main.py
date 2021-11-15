# app/main.py
from concurrent import futures
import random

import grpc

from aiscore_pb2 import (AIScoreData,AIScoreResponse)
import aiscore_pb2_grpc

class AIScoreService(aiscore_pb2_grpc.ScoreResultServicer):

    def GetAISocre(self, request, context):
        random_score = random.uniform(0.0, 99.9)
        score_data = AIScoreData(score=random_score, comment="Hi")
        return AIScoreResponse(score_data=score_data)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    aiscore_pb2_grpc.add_ScoreResultServicer_to_server(AIScoreService(), server)
    server.add_insecure_port("[::]:50051")
    
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
