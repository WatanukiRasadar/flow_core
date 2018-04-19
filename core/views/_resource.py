from quart.views import View
from quart import request, Quart
from quart.wrappers import Response
from quart.exceptions import NotFound, HTTPStatus
from kylin.extras.factory import Factory
from kylin.extras.provider import Provider


class ResourceView:

    def __init__(self, facotory: Factory, provider: Provider, response_provider: Provider[Response]) -> None:
        self.factory = facotory
        self.provider = provider
        self.response_provider = response_provider

    async def get(self, *args, **kwargs):
        resource = await self.provider.provide(*args, **kwargs)
        if resource is None:
            raise NotFound(HTTPStatus.NOT_FOUND)
        return await self.response_provider.provide(resource=resource)

    async def post(self, resource=None):
        try:
            data = await request.get_json()
        except:
            data = {}
        validation = await self.factory.validate(data)
        if validation is True:
            if resource is None:
                resource = await self.factory.create(**data)
            else:
                resource = await self.factory.create(resource, **data)
        else:
            resource = validation
        if resource is None:
            raise NotFound(HTTPStatus.NOT_FOUND)
        return await self.response_provider.provide(resource=resource)

    async def put(self, *args, **kwargs):
        resource = await self.provider.provide(*args, **kwargs)
        if resource is None:
            raise NotFound(HTTPStatus.NOT_FOUND)
        return await self.post(resource=resource)

    async def delete(self, *args, **kwargs):
        resource = await self.provider.provide(*args, **kwargs)
        if resource is None:
            raise NotFound()
        await resource.delete()
        return await self.response_provider.provide(resource)

    @classmethod
    def as_view(cls, *arguments, **kwarguments):

        class ViewDelegate(View):
            async def dispatch_request(self, *args, **kwargs):
                view = cls()
                handler = getattr(view, request.method.lower(), None)
                if handler is None:
                    raise NotFound(HTTPStatus.NOT_FOUND)
                return await handler(*args, **kwargs)

        return ViewDelegate.as_view('simple', *arguments, **kwarguments)