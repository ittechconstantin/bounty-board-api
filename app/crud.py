from sqlalchemy import select
from sqlalchemy.orm import Session

from app import models, schemas


def list_tasks(db: Session) -> list[models.Task]:
    statement = select(models.Task).order_by(models.Task.id)
    return list(db.scalars(statement).all())


def get_task(db: Session, task_id: int) -> models.Task | None:
    return db.get(models.Task, task_id)


def create_task(db: Session, data: schemas.TaskCreate) -> models.Task:
    task = models.Task(
        title=data.title,
        language=data.language.value,
        difficulty=data.difficulty.value,
        reward=data.reward,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def complete_task(db: Session, task_id: int) -> models.Task | None:
    task = get_task(db, task_id)
    if task is None:
        return None
    task.completed = True
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int) -> bool:
    task = get_task(db, task_id)
    if task is None:
        return False
    db.delete(task)
    db.commit()
    return True


def reward_summary(db: Session) -> schemas.RewardSummary:
    open_tasks = list(db.scalars(select(models.Task).where(models.Task.completed.is_(False))).all())
    return schemas.RewardSummary(
        open_tasks=len(open_tasks),
        available_reward=sum(task.reward for task in open_tasks),
    )
