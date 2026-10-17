"""Production Prompt Engineering Templates for Google Generative AI.

Implements structured patterns: Persona framing, Chain-of-Thought (CoT),
Few-Shot in-context learning, and SCAMPER brainstorming.
"""

from typing import Dict, List, Optional


def build_cot_prompt(task_instruction: str, context: Optional[str] = None) -> str:
    """Format Chain-of-Thought prompt enforcing step-by-step reasoning."""
    prompt = "You are an expert AI reasoning assistant. Solve the following problem methodically.\n\n"
    if context:
        prompt += f"Context Information:\n{context}\n\n"
    prompt += (
        f"Task:\n{task_instruction}\n\n"
        "Instructions:\n"
        "1. Break down the task into logical steps.\n"
        "2. Formulate your reasoning explicitly before providing the final conclusion.\n"
        "3. Output the final result clearly labeled under '### Final Output'.\n\n"
        "Step-by-step Analysis:\n"
    )
    return prompt


def build_scamper_prompt(product_or_problem: str) -> str:
    """Format SCAMPER creative thinking framework prompt."""
    return f"""
Apply the SCAMPER creative brainstorming methodology to the following topic:
Target: {product_or_problem}

Generate 2 actionable, non-obvious ideas for each SCAMPER dimension:
- **S**ubstitute: What components, materials, or steps can be swapped?
- **C**ombine: What adjacent services, technologies, or concepts can be merged?
- **A**dapt: What existing mechanisms from other domains can be repurposed?
- **M**odify / Magnify / Minify: What attributes can be exaggerated or minimized?
- **P**ut to another use: How can this serve an entirely different customer segment?
- **E**liminate: What friction, steps, or overhead can be completely stripped away?
- **R**everse / Rearrange: How does the workflow look inverted or run backwards?
""".strip()
