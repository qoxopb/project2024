from app.models.member import Member
from app.dbfactory import Session
from sqlalchemy import insert


class MemberService():
    @staticmethod
    def member_convert(mdto):
        # 클라이언트에서 전달받은 데이터를 dict형으로 변환
        data = mdto.model_dump()
        mb = Member(**data)
        data = {'userid': mb.userid, 'passwd': mb.passwd, 'zipcode': mb.zipcode, 'address1': mb.address1, 'address2': mb.address2,
                'name': mb.name, 'phone': mb.phone, 'email': mb.email}

        return data

    @staticmethod
    def insert_member(mdto):
        # 변환된 회원정보를 member 테이블에 저장
        data = MemberService.member_convert(mdto)
        with Session() as sess:
            stmt = insert(Member).values(data)
            result = sess.execute(stmt)
            sess.commit()

        return result

