from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class AgentState(BaseModel):
    """
    定義 Agent 的狀態
    
    包含使用者問題、Agent 回答、情緒、記憶內容、搜尋結果、工具使用紀錄等
    以及額外的 metadata 和狀態標記
    """
    question: Optional[str] = Field(None, description="使用者的問題")
    answer: Optional[str] = Field(None, description="Agent 的回答")
    emotion: Optional[str] = Field("neutral", description="Agent 當前情緒")
    persona: Optional[str] = Field("default", description="Agent 人設")

    memory_context: List[str] = Field(default_factory=list, description="從記憶檢索的內容")
    search_results: List[str] = Field(default_factory=list, description="搜尋結果")
    tools_used: List[str] = Field(default_factory=list, description="呼叫過的工具")

    metadata: Dict[str, str] = Field(default_factory=lambda: {
        "timestamp": datetime.now().isoformat()
    }, description="額外資訊，例如時間、session_id")

    status: str = Field("idle", description="Agent 狀態 (idle, processing, error)")