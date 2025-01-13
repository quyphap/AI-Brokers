
from langchain_core.messages import HumanMessage

from agents.state import AgentState, show_agent_reasoning

import pandas as pd

import numpy as np

import json

##### Sentiment Agent #####
def sentiment_agent(state: AgentState):
    """Analyzes market sentiment and generates trading signals."""
    data = state["data"]
    bullish_signals, bearish_signals = data["insider_trades"]
    show_reasoning = state["metadata"]["show_reasoning"]


    
    


    # Determine overall signal
    
    LSRatio = bullish_signals/ bearish_signals 
    
    if LSRatio > 1:
        overall_signal = "bullish"
    elif LSRatio < 1:
        overall_signal = "bearish"
    else:
        overall_signal = "neutral"

    # Calculate confidence level based on the proportion of indicators agreeing
    confidence = max(bullish_signals, bearish_signals) 

    message_content = {
        "signal": overall_signal,
        "confidence": f"{round(confidence * 100)}%",
        "reasoning": f"Bullish signals: {bullish_signals}, Bearish signals: {bearish_signals}"
    }

    # Print the reasoning if the flag is set
    if show_reasoning:
        show_agent_reasoning(message_content, "Sentiment Analysis Agent")

    # Create the sentiment message
    message = HumanMessage(
        content=json.dumps(message_content),
        name="sentiment_agent",
    )

    return {
        "messages": [message],
        "data": data,
    }
