import asyncio
import os

async def run_command():
    """Run command in subprocess

    Example from:
        http://asyncio.readthedocs.io/en/latest/subprocess.html
    """
    # Create subprocess
    process = await asyncio.create_subprocess_exec(
        123,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE)

    # Status
    print('Started:', 123, '(pid = ' + str(process.pid) + ')')


    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()

    # Progress
    if process.returncode == 0:
        print('Done:', 123, '(pid = ' + str(process.pid) + ')')
    else:
        print('Failed:', 123, '(pid = ' + str(process.pid) + ')')

    # Result
    result = stdout.decode().strip()

    # Return stdout
    return result

async def say(what, when):
    await asyncio.sleep(when)
    print("pid %s:" % os.getpid())
    print(what)


    # Create subprocess
    process = await asyncio.create_subprocess_exec(
    123,
    # stdout must a pipe to be accessible as process.stdout
    stdout=asyncio.subprocess.PIPE)

    # Status
    print('Started:', 123, '(pid = ' + str(process.pid) + ')')


