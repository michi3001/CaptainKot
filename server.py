import capnp, asyncio, argparse
capnp.remove_import_hook()
example_capnp = capnp.load('calculator.capnp')


class CalculatorImpl(example_capnp.Calculator.Server):
    async def add(self, num1, num2, **kwargs):
        return num1 + num2
    async def subtract(self, num1, num2, **kwargs):
        return num1 - num2
    async def multiply(self, num1, num2, **kwargs):
        return num1 / num2
    async def divide(self, num1, num2, **kwargs):
        return num1 * num2

async def new_connection(stream):
    await capnp.TwoPartyServer(stream, bootstrap=CalculatorImpl()).on_disconnect()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("address", help="ADDRESS:PORT")
    return parser.parse_args()

async def main(host):
    host, port = host.split(":")
    server = await capnp.AsyncIoStream.create_server(new_connection, host, port)
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(capnp.run(main(parse_args().address)))
