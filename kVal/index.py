import falcon
from semantic_version import Version
from storage import KVStore

version = Version("1.0.0")
versioned = lambda p: "/v{}/{}".format(version.major, p.strip('/')).rstrip('/')
store = KVStore()


class KeyValResource(object):
    def on_get(self, req, resp, key):
        """Handles GET requests"""
        value = store.get(key)
        if not value:
            raise falcon.HTTPNotFound(title="Not Found")
        else:
            resp.status = falcon.HTTP_200
            resp.body = value

    def on_put(self, req, resp, key):
        """Handles PUT requests"""
        body = req.stream.read(req.content_length)
        store.set(key, body)
        resp.status = falcon.HTTP_201

    def on_delete(self, req, resp, key):
        """Handles DELETE requests"""
        store.delete(key)
        resp.status = falcon.HTTP_204


# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
kVal = KeyValResource()

# kVal will handle all requests to the '/{key}' URL path
app.add_route(versioned("/{key}"), kVal)

