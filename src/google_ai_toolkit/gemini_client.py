"""Google Gemini API Orchestrator.

Provides a robust interface for interacting with Google Generative AI (Gemini Flash/Pro),
managing system instructions, temperature hyperparameters, and structured JSON parsing.
"""

from typing import Dict, Any, Optional
import os
import json


class GeminiOrchestrator:
    """Wrapper for Google Generative AI API calls."""

    def __init__(self, api_key: Optional[str] = None, model_name: str = "gemini-1.5-flash"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model_name = model_name

    def format_request_payload(
        self,
        prompt: str,
        system_instruction: Optional[str] = None,
        temperature: float = 0.2,
        top_p: float = 0.95
    ) -> Dict[str, Any]:
        """Construct standard Gemini API payload dictionary."""
        payload: Dict[str, Any] = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ],
            "generationConfig": {
                "temperature": temperature,
                "topP": top_p,
                "maxOutputTokens": 2048,
            }
        }
        if system_instruction:
            payload["systemInstruction"] = {
                "parts": [{"text": system_instruction}]
            }
        return payload
