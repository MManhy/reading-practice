import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Literal, Union
from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import ChatPromptTemplate

# 加载 .env 文件中的环境变量
load_dotenv()

# 定义实体 Pydantic 模板
class Person(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str = Field(description="人名，例如：白居易、李白")
    type: Literal["Person"] = Field(default="Person")

class Date(BaseModel):
    model_config = ConfigDict(extra="forbid")
    date: str = Field(description="日期或年份，如：772年、天宝年间")
    type: Literal["Date"] = Field(default="Date")

class Location(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str = Field(description="地名，如：长安、江州")
    type: Literal["Location"] = Field(default="Location")

class Title(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str = Field(description="作品名称，如：长恨歌、琵琶行")
    type: Literal["Title"] = Field(default="Title")

# 汇总所有实体类型
Entity = Union[Person, Date, Location, Title]

class EntityList(BaseModel):
    entities: List[Entity] = Field(
        description="从用户查询中识别出的所有实体"
    )

# 初始化 DeepSeek 模型
llm = ChatDeepSeek(model="deepseek-chat", temperature=0)

# 强制结构化输出
structured_llm = llm.with_structured_output(EntityList)

# 构造提示词模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个命名实体识别专家。请从用户关于中国古代诗人及作品的查询中，"
               "抽取出所有实体：人名、日期、地名、作品名。如果没有某类实体不要凭空编造。"),
    ("human", "{query}")
])

# 组建链
chain = prompt | structured_llm

# 测试查询
if __name__ == "__main__":
    test_queries = [
        "白居易在江州时期写了哪些作品？",
        "李白于天宝年间在长安创作了《清平调》",
        "杜甫在成都草堂是否见过岑参？"
    ]
    
    for q in test_queries:
        result = chain.invoke({"query": q})
        print(f"查询：{q}")
        print(f"抽取实体：{result}")

# 这是第二次修改添加的注释