import pyarrow as pa
import pyarrow.flight as flight

class FlightServer(flight.FlightServerBase):
    def list_flights(self, context, descriptor):
        # Implementation of listing flights
        return []  # Replace with actual implementation

    def do_get(self, context, ticket):
        # Implementation of handling a ticket request
        return flight.RecordBatchStream(pa.RecordBatch.from_arrays([pa.array([1, 2, 3]), pa.array(['a', 'b', 'c'])], names=['numbers', 'letters']))

    def do_put(self, context, descriptor, reader):
        # Implementation of handling data put requests
        pass  # Replace with actual implementation

    def do_exchange(self, context):
        # Implementation of handling exchanges
        return flight.FlightStreamReader()  # Replace with actual implementation

if __name__ == '__main__':
    server = FlightServer()
    flight.listen(server, 'localhost', 8815)
    print('Flight server is running on localhost:8815')
    flight.run()
