from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import config
from app.models import contact
from app.models import member, product

# sqlite 사용시 check_same_thread 추가 - 쓰레드 사용 안함
engine = create_engine(config.db_conn, echo=True,
                       connect_args={'check_same_thread': False})

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 서버시작시 테이블 생성
def db_startup():
    contact.Base.metadata.create_all(engine)
    product.Base.metadata.create_all(engine)
    member.Base.metadata.create_all(engine)
    # board.Base.metadata.create_all(engine)

# 테이블구조를 다시만들어주진않음

