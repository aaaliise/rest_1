from flask_restful import reqparse, abort, Api, Resource
from flask import Flask
from data import users_resources
from data import jobs_resources
from data import db_session

app = Flask(__name__)
api = Api(app)


def main():
    db_session.global_init("db/blogs.db")
    api.add_resource(users_resources.UsersListResource, '/api/v2/users')
    api.add_resource(users_resources.UsersResource, '/api/v2/users/<users_id>')
    api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')
    api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<jobs_id>')
    app.run()


if __name__ == '__main__':
    main()