import asyncio
import time


# This is synchronous code where each function waits for other
def endpoint(ep: str) -> str:
    print(f"Request: {ep}")

    time.sleep(1)

    print(f"Response: {ep}")


def server():
    requests = ("GET /teachers", "POST /subjects", "PATCH /students/1")

    start = time.perf_counter()

    for request in requests:
        endpoint(request)

    end = time.perf_counter()

    print(f"Time Taken: {end - start}")


# server()


# This is asynchronous code, where each function runs independently
async def endpoint_async(route: str) -> str:
    print(f"Request: {route}")

    # Because it is running synchronously, therefore it waits becaue moving towards other function
    # time.sleep(1)

    # We can overcome this by making this async as well

    await asyncio.sleep(1)

    print(f"Response: {route}")

    return route


async def server_async():
    tests = ("GET /teachers", "POST /subjects", "PATCH /students/1")

    start = time.perf_counter()

    # requests = [asyncio.create_task(endpoint_async(route)) for route in tests]

    # We can achieve same create_task using task_group

    async with asyncio.TaskGroup() as task_group:
        results = [task_group.create_task(endpoint_async(route)) for route in tests]


    # print (results) outside with because this will give us guaranteed completed tasks
    
    for task in results:
        print(task.result())

    # done, pending = await asyncio.wait(requests)

    # for task in done:
    #     print("Result:", task.result())

    end = time.perf_counter()

    print(f"Time Taken: {end - start}")


# To resolve async function, we use await, but outside the async function, we use asyncio to call that function
# await server_async()

asyncio.run(server_async())
