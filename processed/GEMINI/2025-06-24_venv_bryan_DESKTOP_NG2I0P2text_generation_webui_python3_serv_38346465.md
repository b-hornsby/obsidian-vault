---
id: 370909
source: GEMINI
date: 2025-06-24
tags: ['coding', 'ai', 'gemini', 'model', 'oobabooga', 'llama.cpp', 'text-generation', 'dex']
category: coding
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2
13:54:52-091825 INFO     Starting Text generation web UI
13:54:52-093619 INFO     Loading settings from "user_data/settings.yaml"
13:54:52-098088 INFO     Loading the extension "superboogav2"
13:54:57-289787 DEBUG    Loading hyperparameters...

Running on local URL:  http://127.0.0.1:7860

ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/applications.py", line 112, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 187, in __call__
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 165, in __call__
    await self.app(scope, receive, _send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/trustedhost.py", line 51, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/route_utils.py", line 714, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 62, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 714, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 734, in app
    await route.handle(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 288, in handle
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 76, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 73, in app
    response = await f(request)
               ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 301, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 214, in run_endpoint_function
    return await run_in_threadpool(dependant.call, **values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/concurrency.py", line 37, in run_in_threadpool
    return await anyio.to_thread.run_sync(func)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2470, in run_sync_in_worker_thread
    return await future
           ^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 967, in run
    result = context.run(func, *args)
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 403, in main
    gradio_api_info = api_info(False)
                      ^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 432, in api_info
    app.api_info = app.get_blocks().get_api_info()
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/blocks.py", line 2743, in get_api_info
    python_type = client_utils.json_schema_to_python_type(info)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 893, in json_schema_to_python_type
    type_ = _json_schema_to_python_type(schema, schema.get("$defs"))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 938, in _json_schema_to_python_type
    elements = _json_schema_to_python_type(items, defs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 908, in _json_schema_to_python_type
    return _json_schema_to_python_type(defs[schema["$ref"].split("/")[-1]], defs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 955, in _json_schema_to_python_type
    f"str, {_json_schema_to_python_type(schema['additionalProperties'], defs)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 901, in _json_schema_to_python_type
    type_ = get_type(schema)
            ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 863, in get_type
    if "const" in schema:
       ^^^^^^^^^^^^^^^^^
TypeError: argument of type 'bool' is not iterable
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/applications.py", line 112, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 187, in __call__
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 165, in __call__
    await self.app(scope, receive, _send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/trustedhost.py", line 51, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/route_utils.py", line 714, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 62, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 714, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 734, in app
    await route.handle(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 288, in handle
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 76, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 73, in app
    response = await f(request)
               ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 301, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 214, in run_endpoint_function
    return await run_in_threadpool(dependant.call, **values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/concurrency.py", line 37, in run_in_threadpool
    return await anyio.to_thread.run_sync(func)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2470, in run_sync_in_worker_thread
    return await future
           ^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 967, in run
    result = context.run(func, *args)
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 403, in main
    gradio_api_info = api_info(False)
                      ^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 432, in api_info
    app.api_info = app.get_blocks().get_api_info()
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/blocks.py", line 2743, in get_api_info
    python_type = client_utils.json_schema_to_python_type(info)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 893, in json_schema_to_python_type
    type_ = _json_schema_to_python_type(schema, schema.get("$defs"))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 938, in _json_schema_to_python_type
    elements = _json_schema_to_python_type(items, defs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 908, in _json_schema_to_python_type
    return _json_schema_to_python_type(defs[schema["$ref"].split("/")[-1]], defs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 955, in _json_schema_to_python_type
    f"str, {_json_schema_to_python_type(schema['additionalProperties'], defs)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 901, in _json_schema_to_python_type
    type_ = get_type(schema)
            ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 863, in get_type
    if "const" in schema:
       ^^^^^^^^^^^^^^^^^
TypeError: argument of type 'bool' is not iterable
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/applications.py", line 112, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 187, in __call__
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 165, in __call__
    await self.app(scope, receive, _send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/trustedhost.py", line 51, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/route_utils.py", line 714, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 62, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 714, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 734, in app
    await route.handle(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 288, in handle
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 76, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 73, in app
    response = await f(request)
               ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 301, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 214, in run_endpoint_function
    return await run_in_threadpool(dependant.call, **values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/concurrency.py", line 37, in run_in_threadpool
    return await anyio.to_thread.run_sync(func)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2470, in run_sync_in_worker_thread
    return await future
           ^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 967, in run
    result = context.run(func, *args)
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 403, in main
    gradio_api_info = api_info(False)
                      ^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 432, in api_info
    app.api_info = app.get_blocks().get_api_info()
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/blocks.py", line 2743, in get_api_info
    python_type = client_utils.json_schema_to_python_type(info)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 893, in json_schema_to_python_type
    type_ = _json_schema_to_python_type(schema, schema.get("$defs"))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 938, in _json_schema_to_python_type
    elements = _json_schema_to_python_type(items, defs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 908, in _json_schema_to_python_type
    return _json_schema_to_python_type(defs[schema["$ref"].split("/")[-1]], defs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 955, in _json_schema_to_python_type
    f"str, {_json_schema_to_python_type(schema['additionalProperties'], defs)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 901, in _json_schema_to_python_type
    type_ = get_type(schema)
            ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 863, in get_type
    if "const" in schema:
       ^^^^^^^^^^^^^^^^^
TypeError: argument of type 'bool' is not iterable
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/applications.py", line 112, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 187, in __call__
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 165, in __call__
    await self.app(scope, receive, _send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/trustedhost.py", line 51, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/route_utils.py", line 714, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 62, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 714, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 734, in app
    await route.handle(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 288, in handle
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 76, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 73, in app
    response = await f(request)
               ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 301, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 214, in run_endpoint_function
    return await run_in_threadpool(dependant.call, **values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/concurrency.py", line 37, in run_in_threadpool
    return await anyio.to_thread.run_sync(func)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2470, in run_sync_in_worker_thread
    return await future
           ^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 967, in run
    result = context.run(func, *args)
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 403, in main
    gradio_api_info = api_info(False)
                      ^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 432, in api_info
    app.api_info = app.get_blocks().get_api_info()
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/blocks.py", line 2743, in get_api_info
    python_type = client_utils.json_schema_to_python_type(info)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 893, in json_schema_to_python_type
    type_ = _json_schema_to_python_type(schema, schema.get("$defs"))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 938, in _json_schema_to_python_type
    elements = _json_schema_to_python_type(items, defs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 908, in _json_schema_to_python_type
    return _json_schema_to_python_type(defs[schema["$ref"].split("/")[-1]], defs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 955, in _json_schema_to_python_type
    f"str, {_json_schema_to_python_type(schema['additionalProperties'], defs)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 901, in _json_schema_to_python_type
    type_ = get_type(schema)
            ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 863, in get_type
    if "const" in schema:
       ^^^^^^^^^^^^^^^^^
TypeError: argument of type 'bool' is not iterable
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/applications.py", line 112, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 187, in __call__
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 165, in __call__
    await self.app(scope, receive, _send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/trustedhost.py", line 51, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/route_utils.py", line 714, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 62, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/home/bryan_/tex

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2
13:54:52-091825 INFO     Starting Text generation web UI
13:54:52-093619 INFO     Loading settings from "user_data/settings.yaml"
13:54:52-098088 INFO     Loading the extension "superboogav2"
13:54:57-289787 DEBUG    Loading hyperparameters...

Running on local URL:  http://127.0.0.1:7860

ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/applications.py", line 112, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 187, in __call__
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 165, in __call__
    await self.app(scope, receive, _send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/trustedhost.py", line 51, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/route_utils.py", line 714, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 62, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 714, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 734, in app
    await route.handle(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 288, in handle
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 76, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 73, in app
    response = await f(request)
               ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 301, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 214, in run_endpoint_function
    return await run_in_threadpool(dependant.call, **values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/concurrency.py", line 37, in run_in_threadpool
    return await anyio.to_thread.run_sync(func)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2470, in run_sync_in_worker_thread
    return await future
           ^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 967, in run
    result = context.run(func, *args)
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 403, in main
    gradio_api_info = api_info(False)
                      ^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 432, in api_info
    app.api_info = app.get_blocks().get_api_info()
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/blocks.py", line 2743, in get_api_info
    python_type = client_utils.json_schema_to_python_type(info)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 893, in json_schema_to_python_type
    type_ = _json_schema_to_python_type(schema, schema.get("$defs"))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 938, in _json_schema_to_python_type
    elements = _json_schema_to_python_type(items, defs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 908, in _json_schema_to_python_type
    return _json_schema_to_python_type(defs[schema["$ref"].split("/")[-1]], defs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 955, in _json_schema_to_python_type
    f"str, {_json_schema_to_python_type(schema['additionalProperties'], defs)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 901, in _json_schema_to_python_type
    type_ = get_type(schema)
            ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 863, in get_type
    if "const" in schema:
       ^^^^^^^^^^^^^^^^^
TypeError: argument of type 'bool' is not iterable
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/applications.py", line 112, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 187, in __call__
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 165, in __call__
    await self.app(scope, receive, _send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/trustedhost.py", line 51, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/route_utils.py", line 714, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 62, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 714, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 734, in app
    await route.handle(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 288, in handle
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 76, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 73, in app
    response = await f(request)
               ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 301, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 214, in run_endpoint_function
    return await run_in_threadpool(dependant.call, **values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/concurrency.py", line 37, in run_in_threadpool
    return await anyio.to_thread.run_sync(func)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2470, in run_sync_in_worker_thread
    return await future
           ^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 967, in run
    result = context.run(func, *args)
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 403, in main
    gradio_api_info = api_info(False)
                      ^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 432, in api_info
    app.api_info = app.get_blocks().get_api_info()
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/blocks.py", line 2743, in get_api_info
    python_type = client_utils.json_schema_to_python_type(info)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 893, in json_schema_to_python_type
    type_ = _json_schema_to_python_type(schema, schema.get("$defs"))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 938, in _json_schema_to_python_type
    elements = _json_schema_to_python_type(items, defs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 908, in _json_schema_to_python_type
    return _json_schema_to_python_type(defs[schema["$ref"].split("/")[-1]], defs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 955, in _json_schema_to_python_type
    f"str, {_json_schema_to_python_type(schema['additionalProperties'], defs)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 901, in _json_schema_to_python_type
    type_ = get_type(schema)
            ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 863, in get_type
    if "const" in schema:
       ^^^^^^^^^^^^^^^^^
TypeError: argument of type 'bool' is not iterable
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/applications.py", line 112, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 187, in __call__
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 165, in __call__
    await self.app(scope, receive, _send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/trustedhost.py", line 51, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/route_utils.py", line 714, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 62, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 714, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 734, in app
    await route.handle(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 288, in handle
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 76, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 73, in app
    response = await f(request)
               ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 301, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 214, in run_endpoint_function
    return await run_in_threadpool(dependant.call, **values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/concurrency.py", line 37, in run_in_threadpool
    return await anyio.to_thread.run_sync(func)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2470, in run_sync_in_worker_thread
    return await future
           ^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 967, in run
    result = context.run(func, *args)
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 403, in main
    gradio_api_info = api_info(False)
                      ^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 432, in api_info
    app.api_info = app.get_blocks().get_api_info()
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/blocks.py", line 2743, in get_api_info
    python_type = client_utils.json_schema_to_python_type(info)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 893, in json_schema_to_python_type
    type_ = _json_schema_to_python_type(schema, schema.get("$defs"))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 938, in _json_schema_to_python_type
    elements = _json_schema_to_python_type(items, defs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 908, in _json_schema_to_python_type
    return _json_schema_to_python_type(defs[schema["$ref"].split("/")[-1]], defs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 955, in _json_schema_to_python_type
    f"str, {_json_schema_to_python_type(schema['additionalProperties'], defs)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 901, in _json_schema_to_python_type
    type_ = get_type(schema)
            ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 863, in get_type
    if "const" in schema:
       ^^^^^^^^^^^^^^^^^
TypeError: argument of type 'bool' is not iterable
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/applications.py", line 112, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 187, in __call__
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 165, in __call__
    await self.app(scope, receive, _send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/trustedhost.py", line 51, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/route_utils.py", line 714, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 62, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 714, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 734, in app
    await route.handle(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 288, in handle
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 76, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/routing.py", line 73, in app
    response = await f(request)
               ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 301, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 214, in run_endpoint_function
    return await run_in_threadpool(dependant.call, **values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/concurrency.py", line 37, in run_in_threadpool
    return await anyio.to_thread.run_sync(func)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2470, in run_sync_in_worker_thread
    return await future
           ^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 967, in run
    result = context.run(func, *args)
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 403, in main
    gradio_api_info = api_info(False)
                      ^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/routes.py", line 432, in api_info
    app.api_info = app.get_blocks().get_api_info()
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/blocks.py", line 2743, in get_api_info
    python_type = client_utils.json_schema_to_python_type(info)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 893, in json_schema_to_python_type
    type_ = _json_schema_to_python_type(schema, schema.get("$defs"))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 938, in _json_schema_to_python_type
    elements = _json_schema_to_python_type(items, defs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 908, in _json_schema_to_python_type
    return _json_schema_to_python_type(defs[schema["$ref"].split("/")[-1]], defs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 948, in _json_schema_to_python_type
    f"{n}: {_json_schema_to_python_type(v, defs)}{get_desc(v)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 955, in _json_schema_to_python_type
    f"str, {_json_schema_to_python_type(schema['additionalProperties'], defs)}"
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 901, in _json_schema_to_python_type
    type_ = get_type(schema)
            ^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio_client/utils.py", line 863, in get_type
    if "const" in schema:
       ^^^^^^^^^^^^^^^^^
TypeError: argument of type 'bool' is not iterable
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/applications.py", line 112, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 187, in __call__
    raise exc
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 165, in __call__
    await self.app(scope, receive, _send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/trustedhost.py", line 51, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/gradio/route_utils.py", line 714, in __call__
    await self.app(scope, receive, send)
  File "/home/bryan_/text-generation-webui/.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 62, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/home/bryan_/tex

### GEMINI
You're absolutely right to be frustrated. We fixed markdown, but now we're still hitting a different, very complex-looking error, even after attempting to downgrade Gradio: TypeError: argument of type 'bool' is not iterable This error traceback points deep into gradio_client/utils.py and gradio/blocks.py, specifically related to how Gradio is generating its API information and handling schema types. The most critical part of this new error is that it occurs even AFTER you downgraded Gradio to 4.37.2 and gradio_client to 1.0.2. This strongly suggests that the issue is NOT directly the Gradio version itself but rather an incompatibility between your specific Python version (Python 3.12, as seen in the traceback paths) and the Gradio/Oobabooga codebase. Many Python projects, especially those in the AI space that move quickly, tend to lag behind the very latest Python releases in terms of full compatibility. Python 3.12 is relatively new, and it's quite possible that Oobabooga's text-generation-webui or even the gradio versions it uses are not yet fully compatible with it, leading to subtle TypeError issues like the one you're seeing. The Solution: Revert to Python 3.10 or 3.11 This is the most likely culprit and the most robust solution. If you installed Python 3.12 through your initial WSL2 setup, we need to get Python 3.10 or 3.11 installed and make sure your virtual environment uses it. Python 3.10 is widely considered the most stable and compatible version for many AI projects right now, including Oobabooga. How to Install and Use Python 3.10/3.11 in WSL2: First, let's confirm your default Python version. Step 24: Verify Your Current Python Version Action: Stop Oobabooga completely. Press Ctrl + C in your WSL2 terminal until you see your prompt. Run these commands to see your default Python and Python3 versions: python --version python3 --version This will confirm that you are indeed using Python 3.12 as your default for python3. Step 25: Install Python 3.10 (Recommended) and Update Alternatives Since you are on Ubuntu 22.04 LTS (Jammy Jellyfish), Python 3.10 is the default Python 3 in the package manager. Action: Install Python 3.10 (if not already fully installed with python3-full): sudo apt update sudo apt install python3.10 python3.10-venv python3.10-dev -y Verify Python 3.10 is installed: python3.10 --version You should see something like Python 3.10.12. Update update-alternatives to prefer Python 3.10 (this is key): This will set Python 3.10 as the default for the python3 command. sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1 sudo update-alternatives --config python3 When sudo update-alternatives --config python3 runs, you'll see a list. Choose the number corresponding to python3.10. Confirm the change: python3 --version It should now show Python 3.10.x. Step 26: Re-create the Virtual Environment with Python 3.10 and Reinstall Dependencies Because your current .venv was created with Python 3.12, it's tied to that version. We need to delete it and recreate it with Python 3.10. This is tedious, but necessary for a clean install. Action: Deactivate your current virtual environment: deactivate Your prompt should go back to bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Delete the existing virtual environment: rm -rf .venv Create a new virtual environment using Python 3.10: python3.10 -m venv .venv Activate the new virtual environment: source .venv/bin/activate Your prompt should now show (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Re-install torch and torchvision (CPU version if you don't have a supported NVIDIA GPU or CUDA is not set up): pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu OR (if you have an NVIDIA GPU and CUDA is correctly set up in WSL2): pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 # Or cu121 if you have CUDA 12.1+ Double-check your CUDA version in WSL2 if you're using the GPU version. If you're unsure, just use the CPU version for now to get it running. Re-install other necessary dependencies (including the specific Gradio/Gradio Client and markdown): pip install -r requirements.txt pip install markdown pip install gradio==4.37.2 gradio_client==1.0.2 Note: requirements.txt might pull in a newer Gradio again, so we explicitly install the older one after it, as pip install will upgrade/downgrade if a version is specified. Run the llama.cpp specific build (important for the --loader llama.cpp argument): pip install -r extensions/webui_llama_cpp/requirements.txt Finally, launch Oobabooga again: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2 This is a significant set of steps, but correctly aligning the Python version with the Oobabooga codebase and its dependencies is almost certainly the key to getting past these subtle TypeError issues. Take your time, and carefully follow each step. Let me know the output of each command, especially python3 --version after you've changed the alternatives.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]