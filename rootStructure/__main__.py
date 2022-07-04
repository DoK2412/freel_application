import uvicorn


from .settings import setting


uvicorn.run(
    'rootStructure.app:app',
    host=setting.server_host,
    port=setting.server_post,
    reload=True
)
