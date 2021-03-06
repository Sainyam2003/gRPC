import grpc
from concurrent import futures
import time

#import the generated files
import cal.calculator_pb2 as calculator_pb2
import cal.calculator_pb2_grpc as calculator_pb2_grpc

#import the function files
import calculator

#create a class to define the server functions derived from calculator_pb2_grpc (or the server and client classes)
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    #calculator.square_root is exposed here
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response


#create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

#use the function "add_CalculatorServicer_to_server" to add the defined class to the created server
calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)

#listen on port 50051
print('Starting server. Listening on port 8000.')
server.add_insecure_port('[::]:8000')
server.start()

# since server.start() will not block be blocked ever, a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)