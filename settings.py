import datetime

SERVER_NAME = '127.0.0.1:5000'

post_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'body': {
        'type': 'string',
        'default': 'This post has no body.',
    },
    'upvotes': {
        'type': 'integer',
        'default': 0,
    },
    'downvotes': {
        'type': 'integer',
        'default': 0,
    },
    'views': {
        'type': 'integer',
        'default': 0,
    },
    'active': {
        'type': 'bool',
        'default': True,
    },
}

question_schema = {
    'title': {
        'type': 'string',
        'default': 'This question has no title.',
    },
    'post': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'post',
            'field': '_id',
            'embeddable': True,
        },
    },
    'tags': {
        # TODO
        # should be Many-to-Many
        'type': 'list',
    },
}

answer_schema = {
    'post': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'post',
            'field': '_id',
            'embeddable': True,
        },
    },
    'question': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'question',
            'field': '_id',
            'embeddable': True,
        },
    },
}

comment_schema = {
    'post': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'post',
            'field': '_id',
            'embeddable': True,
        },
    },
    'parent': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'post',
            'field': '_id',
            'embeddable': True,
        },
    },
}

answer_schema = {
    'post': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'post',
            'field': '_id',
            'embeddable': True,
        },
    },
    'question': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'question',
            'field': '_id',
            'embeddable': True,
        },
    },
}

tag_schema = {
    # need to have a get_or_create()
    'body': {
        'type': 'string',
        'default': 'EMPTY TAG',
    },
}

post = {
    'schema': post_schema,
}

question = {
    'schema': question_schema,
}

answer = {
    'schema': answer_schema,
}

tag = {
    'schema': tag_schema,
}

comment = {
    'schema': comment_schema,
}

DOMAIN = {
    'post': post,
    'question': question,
    'tag': tag,
    'answer': answer,
}
# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
#following two lines caused problems. Not sure if will be necessary eventually
#MONGO_USERNAME = 'user'
#MONGO_PASSWORD = 'user'
MONGO_DBNAME = 'beardb'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
