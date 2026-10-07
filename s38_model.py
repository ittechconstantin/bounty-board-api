from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

user = 'root'
password = 'admin'
engine = create_engine(f"mysql+pymysql://{user}:{password}@localhost:3306/curs")
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "s38_task"

    id:          Mapped[int]   = mapped_column(primary_key=True, autoincrement=True)
    titlu:       Mapped[str]   = mapped_column(String(200))
    limbaj:      Mapped[str]   = mapped_column(String(20))
    dificultate: Mapped[str]   = mapped_column(String(10))
    recompensa:  Mapped[float]
    rezolvat:    Mapped[bool]  = mapped_column(default=False)


def reset_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def adauga_date_initiale(s):
    if not s.scalars(select(Task)).all():
        s.add_all([
            Task(titlu="Fix bug la login",     limbaj="Python",     dificultate="usor",  recompensa=50),
            Task(titlu="Adauga dark mode",      limbaj="JavaScript", dificultate="mediu", recompensa=150),
            Task(titlu="Optimizeaza query SQL", limbaj="Python",     dificultate="greu",  recompensa=300, rezolvat=True),
        ])
        s.commit()


def init_db():
    Base.metadata.create_all(engine)
    with SessionLocal() as s:
        adauga_date_initiale(s)


def adauga_task(s, titlu, limbaj, dificultate, recompensa):
    t = Task(titlu=titlu, limbaj=limbaj, dificultate=dificultate, recompensa=recompensa)
    s.add(t)
    s.commit()
    return t


def toate_task_urile(s):
    rezultat = select(Task).order_by(Task.id)
    return s.scalars(rezultat).all()


def un_task(s, task_id):
    task_cautat = s.get(Task, task_id)
    return task_cautat


def marcheaza_rezolvat(s, task_id):
    task_cautat = s.get(Task, task_id)
    if task_cautat is None:
        return None
    task_cautat.rezolvat = True
    s.commit()
    return task_cautat


def sterge_task(s, task_id):
    task_cautat = s.get(Task, task_id)
    if task_cautat is None:
        return False
    s.delete(task_cautat)
    s.commit()
    return True


def recompensa_disponibila(s):
    nerezolvate = s.scalars(select(Task).where(Task.rezolvat == False)).all()
    return float(sum(t.recompensa for t in nerezolvate))


init_db()
