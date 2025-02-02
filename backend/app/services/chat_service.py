from openai import OpenAI
import os
from config import Config

class ChatService:
    def __init__(self):
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        
        self.assistant_instructions = """You are an AI assistant helping users create outreach sequences. Follow these guidelines strictly:

        1. ALWAYS start by asking ONE specific question about the outreach campaign. Only ask one question at a time.

        2. Wait for the user's response before proceeding.

        3. After receiving enough context, say "Generating sequence..." before creating the sequence.

        4. When generating the sequence, use this exact format:
        Step 1:    [Context-aware opening message]
        Step 2:    [Value proposition or main point]
        Step 3:    [Additional value or unique benefit]
        Step 4:    [Call to action]

        Example interaction:
        User: "I need a sales sequence for tech startups"
        Assistant: "What specific pain point or challenge does your product solve for tech startups?"

        User: "We help with automated testing"
        Assistant: "Generating sequence..."
        [Then generate the sequence in steps format]

        Rules:
        - Ask only ONE question at a time
        - Keep questions focused and specific
        - Show "Generating sequence..." before generating
        - Show "Editing sequence..." when modifying
        - Follow the exact Step 1, Step 2, etc. format
        - Include {{variables}} for personalization

        Never generate a sequence without first asking at least one clarifying question"""

    def get_completion(self, message: str, conversation_history: list = None):
        messages = []
        
        # Add system message
        messages.append({
            "role": "system",
            "content": self.assistant_instructions
        })

        # Add conversation history if exists
        if conversation_history:
            messages.extend(conversation_history)

        # Add current message
        messages.append({
            "role": "user",
            "content": message
        })

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini", 
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Error in chat completion: {str(e)}")
            raise