import grpc

#import the generated files
import cal.calculator_pb2 as calculator_pb2
import cal.calculator_pb2_grpc as calculator_pb2_grpc

#open and connect to the gRPC channel we just created
channel = grpc.insecure_channel('localhost:8000')

#create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

#create a valid request message or just any number in our case
number = calculator_pb2.Number(value=float(input('Input any number:')))

#make the call
response = stub.SquareRoot(number)

#print the results
print(response.value)