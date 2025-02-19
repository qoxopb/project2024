# import requests
# from sqlalchemy import insert, select, update, func, or_
# from app.dbfactory import Session
# from app.models.contact import Notice
# from app.models.contact import Qna
#
#
# class QnaService:
#     @staticmethod
#     def board_convert(bdto):
#         data = bdto.model_dump()
#         data.pop('response')   # captcha 확인용 변수 response는 제거
#         bd = Board(**data)
#         data = {'userid': bd.userid, 'title': bd.title,
#                 'contents': bd.contents}
#         return data
#
#
#     @staticmethod
#     def insert_board(bdto):
#         data = BoardService.board_convert(bdto)
#         with Session() as sess:
#             stmt = insert(Board).values(data)
#             result = sess.execute(stmt)
#             sess.commit()
#
#         return result
#
#
#     @staticmethod
#     def select_board(cpg):
#         stnum = (cpg - 1) * 25
#         with Session() as sess:
#             cnt = sess.query(func.count(Board.bno)).scalar() # 총게시글수
#
#             stmt = select(Board.bno, Board.title, Board.userid,
#                       Board.regdate, Board.views)\
#             .order_by(Board.bno.desc()).offset(stnum).limit(25)
#             result = sess.execute(stmt)
#
#         return result, cnt
#
#
#     @staticmethod
#     def selectone_board(bno):
#         with Session() as sess:
#             stmt = select(Board).filter_by(bno=bno)
#             result = sess.execute(stmt).first()
#
#         return result
#
#
#     @staticmethod
#     def update_count_board(bno):
#         with Session() as sess:
#             stmt = update(Board).filter_by(bno=bno)\
#                 .values(views=Board.views+1)
#             result = sess.execute(stmt)
#             sess.commit()
#
#         return result
