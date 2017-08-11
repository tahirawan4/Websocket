#!/usr/bin/env python

import asyncio
import websockets

id =0
async def createProcess(*args):
    """Run command in subprocess


    Example from:
        http://asyncio.readthedocs.io/en/latest/subprocess.html
    """
    # Create subprocess
    process = await asyncio.create_subprocess_exec(
        *args,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE)

    # Status
    print('Started:', args, '(pid = ' + str(process.pid) + ')')

    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()

    # Progress
    if process.returncode == 0:
        print('Done:', args, '(pid = ' + str(process.pid) + ')')
    else:
        print('Failed:', args, '(pid = ' + str(process.pid) + ')')

    # Result
    result = stdout.decode().strip()

    # Return stdout
    return result

async def hello(websocket, path):
    name = await websocket.recv()

    print("< {}".format(name))
    createProcess()
    id = id + 1
    mesage ="process with name = "+name+"with id:"+id+"created"
    await websocket.send()
    print("> {}".format(mesage))

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
