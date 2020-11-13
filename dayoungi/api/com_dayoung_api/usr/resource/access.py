from flask_restful import Resource, reqparse
from com_dayoung_api.usr.model.user_dao import UserDao
from com_dayoung_api.usr.model.user_dto import UserDto, UserVo
class Access(Resource):
    """
    서버와 정보를 주고 받는다.
    """
    @staticmethod
    def post():
        parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
        parser.add_argument('usr_id', type=str, required=True,
                                                help='This field should be a usr_id')
        parser.add_argument('password', type=str, required=True,
                                                help='This field should be a password')
        args = parser.parse_args()
        print(args)
        user = UserVo()
        user.usr_id = args.usr_id
        user.password = args.password

        print("아이디: ", user.usr_id)
        print("비밀번호: ", user.password)
        data = UserDao.login(user)
        return data[0], 200
