from typing import Callable, Any

# The decorator function which will be added on top of the functon which we want to be decorated
# It can perform things before and after that function


# Taking custom inputs in decorator. Just wrap the old decorator with the custom decorator and return the old decorator.
def custom_decorate(dec: str):

    def decorate(fun: Callable):

        # It will give error 'NoneType' object is not callable if we don't return a function in the decorator, on the line which is calling the function that is using decorator
        # However the decorator will be executed by the python interpreter anyways

        # print("@" * 10)
        # fun()
        # print("@" * 10)

        # But if we wrap our processings within a wrapper and return it, the error will be resolved

        # return wrapper
        # def wrapper():
        #     print("@" * 10)
        #     fun()
        #     print("@" * 10)

        # return wrapper

        # We passed the text as argument to the wrapper because our function is taking an argument, the decorator is picking
        # that argument, and passing the function to the wrapper, but if the wrapper won't be taking any argument, it will give
        # error: TypeError: decorate.<locals>.wrapper() takes 0 positional arguments but 1 was given
        # because the argument from our function is being passed to the wrapper as argument because wrapper is calling our function

        # We used None as default so that the wrapper works if no arguments are passed
        # def wrapper_with_argument(text: str | None = None):
        #     if text is None:
        #         print("@" * 10)
        #         fun()
        #         print("@" * 10)
        #     else:
        #         print("@" * len(text))
        #         fun(text)
        #         print("@" * len(text))

        # return wrapper_with_argument

        # We can use *args and **kwargs if we have unknown arguments. *args looks for directly passed arguments like (a,b,2)
        # and **kwargs looks for keyboard arguments like (a=2,b=5)
        def wrapper_with_arguments(*args, **kwargs):
            # Checking if the kwargs and kwargs are not present
            if not args and not kwargs:
                print(dec * 10)
                fun()
                print(dec * 10)
            else:
                length = 0
                # Checking if args is present and the first arg is string, and then taking length of the first arg
                if args and isinstance(args[0], str):
                    length = len(args[0])

                print(dec * length)
                fun(*args, **kwargs)
                print(dec * length)

        return wrapper_with_arguments

    return decorate


# The function on which the decorator will work


@custom_decorate("$")
def log(text: str = "test"):
    print(text)


log("Anas")
log()

### Mimicing the FastAPI and role of decorators

# ... tells python that it can have any arguments, or no arguments at all
routes: dict[str, Callable[..., Any]] = {}


# Will allow to add custom paths
def route(path: str):
    # Will take the function which will be processed on the specific route
    def def_route(func):
        routes[path] = func
        # To run the function that will be processed on the specific route
        return func

    return def_route


# Similar to FastAPI
@route("/teacher")
def get_teachers():
    json = {"id": 1, "name": "Anas"}, {"id": 2, "name": "Hamza"}
    # Wrap it in [] because otherwise it will assume that we are making dictionary in a set
    return json

# Mimicing request

request: str = ""

while request != "quit":
    request = input("> ")

    if request in routes:
        response = routes[request]()
        print(response, end="\n\n")
    else:
        response = "detail: not found"
        print (response)
