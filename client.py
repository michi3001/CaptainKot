import capnp, asyncio, argparse
capnp.remove_import_hook()
example_capnp = capnp.load('calculator.capnp')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="HOST:PORT")
    return parser.parse_args()

async def main(connection):
    client = capnp.TwoPartyClient(connection)
    calculator = client.bootstrap().cast_as(example_capnp.Calculator)
    response = await calculator.add(num1 =  5, num2 = 7)
    print(response.result)
    response = await calculator.subtract(num1 =  5, num2 = 7)
    print(response.result)
    response = await calculator.multiply(num1 =  5, num2 = 7)
    print(response.result)
    response = await calculator.divide(num1 =  5, num2 = 7)
    print(response.result)

async def cmd_main(host):
    host,port = host.split(":")
    await main(await capnp.AsyncIoStream.create_connection(host=host, port=port))


if __name__ == "__main__":
    asyncio.run(capnp.run(cmd_main(parse_args().host)))
