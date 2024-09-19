import capnp, asyncio, argparse
capnp.remove_import_hook()
example_capnp = capnp.load('example.capnp')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="HOST:PORT")
    return parser.parse_args()

async def main(connection):
    client = capnp.TwoPartyClient(connection)
    calculator = client.bootstrap().cast_as(example_capnp.Calculator)
    result = calculator.add(num1 =  5, num2 = 7)
    read_promise = result
    response = await read_promise
    print(response.result)

async def cmd_main(host):
    host,port = host.split(":")
    await main(await capnp.AsyncIoStream.create_connection(host=host, port=port))


if __name__ == "__main__":
    asyncio.run(capnp.run(cmd_main(parse_args().host)))
