from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class Language(str, Enum):
    PYTHON = "Python"
    JAVASCRIPT = "JavaScript"
    GO = "Go"
    RUST = "Rust"


class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    language: Language
    difficulty: Difficulty
    reward: float = Field(gt=0)


class TaskResponse(TaskCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    completed: bool


class RewardSummary(BaseModel):
    open_tasks: int
    available_reward: float
